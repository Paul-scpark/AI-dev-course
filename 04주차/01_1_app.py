import mysql
from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id": 1, "name": "Espresso", "price": 3800},
    {"id": 2, "name": "Americano", "price": 4100},
    {"id": 3, "name": "CafeLatte", "price": 4600}
]

### Core mission: 메뉴 관리 CRUD 구현

@app.route('/')
def hello_flask():
    return "Hello, world!"

# GET /menus | 자료를 가지고 오기
@app.route('/menus')
def get_menus():
    conn = mysql.connector.connect(
        user='root', password='1234', host='127.0.0.1', database='menu', auth_plugin='mysql_native_pass'
    )
    cursor = conn.cursor()
    
    query = ("SELECT * FROM menus")
    cursor.execute(query)
    DB_menus = []
    
    for (id, name, price) in cursor:
        print(f"{id}, {name}, {price}")
        DB_menus.append({'id': id, 'name': name, 'price': price})
        
    cursor.close()
    conn.close()
    
    return jsonify(DB_menus)

# POST /menus | 자료를 자원에 추가하기
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json()
    new_menu = {
        "id": 4, 
        "name": request_data["name"], 
        "price": request_data["price"]
    }
    menus.append(new_menu)
    return jsonify(new_menu)

### PUT /menu/<int:id> | 해당하는 id에 해당하는 데이터를 갱신 (HTTP Request의 Body에 갱신할 내용이 json으로 전달)
@app.route('/menu/<id>', methods=['PUT']) # URL에 <>를 붙여서 이를 함수의 인자로 대입할 수 있음
def update_menu(id):
    request_data = request.get_json()
    new_menu = {
        "id": id,
        "name": request_data["name"],
        "price": request_data["price"]
    }
    menus[find_index_by_id(menus, id)] = new_menu
    return jsonify(new_menu)

### DELETE /menu/<int:id> | 해당하는 id에 해당하는 데이터를 삭제
@app.route('/menus/<id>', methods=['DELETE'])
def delete_menu(id):
    del_index = find_index_by_id(menus, id)
    del_menu = menus[del_index]
    del(menus[del_index])
    return del_menu

@app.route('/menu', methods=['POST'])
def create_menu():
    request_data = request.get_json()
    new_menu = {
        "id": counter["id"],
        "name": request_data["name"], 
        "price": request_data["price"]
    }
    counter['id'] += 1
    menus.append(new_menu)
    return jsonify(new_menu)

if __name__ == '__main__':
    app.run()