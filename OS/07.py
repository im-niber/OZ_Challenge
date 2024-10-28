# 문자열 객체를 변수 my_name이 참조했다
# 이때 ref count는 1인 상태.
my_name = "Gookhee"

# ref count가 2인 상태
your_name = my_name


# 참조하는 대상이 없어지면 카운트가
# 0이 되고 이는 소멸대상이다.
my_name = 1
your_name = 2
