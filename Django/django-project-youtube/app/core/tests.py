from django.test import SimpleTestCase
from unittest.mock import patch # 연결 시도하는 부분을 가로채는 기능
from django.core.management import call_command
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OPsycopgpError

# 아래 함수를 가로챘다 의 의미
@patch('django.db.utils.ConnectionHandler.__getitem__')
class CommandsTest(SimpleTestCase):
    
    # DB가 준비되었을 때 wait_for_db 잘 동작하는지 체크하는 함수
    def test_wait_for_db_ready(self, patched_getitem):
        patched_getitem.return_value = True

        call_command('wait_for_db')
        self.assertEqual(patched_getitem.call_count, 1)
        
    # DB 연결에 오류가 발생했다고 가정을 하고 테스트
    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_getitem):
        # 오류 상황을 만드는 코드
        patched_getitem.side_effect = [Psycopg2OPsycopgpError] + \
                    [OperationalError] * 5 + [True]
        
        call_command('wait_for_db')
        
        # 총 7회 시도 하는지 체크
        self.assertEqual(patched_getitem.call_count, 7)


# docker-compose run --rm app sh -c 'python manage.py test core'
# core 모듈만 test 하는 명령어