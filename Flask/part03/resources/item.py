from flask import request
from flask_restful import Resource

items = [] # DB 예시

class Item(Resource):

    # 조회
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {"msg": "Item not found"}, 404 # msg code

    # 생성
    def post(self, name):
        for item in items:
            if item['name'] == name:
                return {"msg": "Item Already exists"}, 400
            
        data = request.get_json()
        new_item = {'name': name, 'price':data['price']}
        items.append(new_item)

        print(new_item, data)
        return new_item

    # 수정
    def put(self, name):
        data = request.get_json()
        
        for item in items:
            if item['name'] == name:
                item['price'] = data['price']
                return item
            
        # 업데이트 할 아이템이 없다면 -> 추가한다고 기획했다면,
        print("put -> post")
        self.post(name)
        return data

    # 삭제
    def delete(self, name):
        global items

        items = [item for item in items if item['name'] != name]
        return {"msg": "Item deleted"}
