import json
from datetime import datetime
import bcrypt


def hashing(data):  # noqa
    data = data.encode('ASCII')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(data, salt)
    hashed = hashed.decode('ASCII')
    return hashed


def hashing_read(data, password):
    data = data.encode('ASCII')
    password = password.encode('ASCII')
    if bcrypt.checkpw(password, data):
        return True
    else:
        return False


def count_user():
    number = File('users.json').read()
    count = 0
    for _ in number:
        count += 1
    return count


class File:
    def __init__(self, filename):  # noqa
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as file:
            try:
                data = json.load(file)
            except:  # noqa
                data = []
        return data

    def write(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=3)


def check_admin(data):
    if data == 'admin':
        return True
    else:
        return False


class User:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = hashing(password)
        self.admin = check_admin(username)
        self.id = count_user()

    def login(self, password):
        obj = File('users.json')
        request = obj.read()
        for i in request:
            if i['username'] == self.username and hashing_read(i['password'], password):
                return True
        else:
            return False

    def check_admin(self):# noqa
        obj = File('users.json')
        request = obj.read()
        for i in request:
            if i['username'] == self.username:
                return i['admin']
        else:
            return False


    def add_admin(self, username):# noqa
        obj = File('users.json')
        request = obj.read()
        for i in request:
            if i['username'] == username:
                i['admin'] = True
                obj.write(request)
                return True
        else:
            print('Bunday username mavjud emas!')

    def register(self):
        obj = File('users.json')
        request = obj.read()
        request.append(self.__dict__)
        obj.write(request)

    def check_user(self):
        obj = File('users.json')
        request = obj.read()
        for i in request:
            if i['username'] == self.username:
                return False
        else:
            return True

    def get_id(self, username):  # noqa
        obj = File('users.json')
        info = obj.read()
        for i in info:
            if i['username'] == username:
                return i['id']
        else:
            return None

    def add_product(self, order, id):  # noqa
        obj = File('my_products.json')
        request = obj.read()
        order['time'] = datetime.now().strftime('%Y:%m:%d %H:%M')
        for i in request:
            if i['id'] == id:
                for j in i['products']:
                    if j['name'] == order['name']:
                        j['count'] += order['count']
                        obj.write(request)
                        return
                else:
                    i['products'].append(order)
                    break
        else:
            request.append({"id": id, "products": [order]})
        obj.write(request)

    def get_road(self, id):  # noqa
        obj = File('my_products.json')
        request = obj.read()
        summa = 0
        for i in request:
            if i['id'] == id:
                for j in i['products']:
                    summa += j['price']
        return summa

    def my_products(self, id):  # noqa
        obj = File('my_products.json')
        request = obj.read()
        for i in request:
            if i['id'] == id:
                linked = [[j['name'], j['count'], j['time']] for j in i['products']]
                return linked
        else:
            return False


class Product:
    def __init__(self, name=None, price=None, count=None):
        self.name = name
        self.price = price
        self.count = count

    def add_products(self):
        obj = File('products.json')
        list_ = obj.read()
        for i in list_:
            if i['name'] == self.name:
                i['count'] += self.count
                i['price'] = self.price
                break
        else:
            list_.append(self.__dict__)
        obj.write(list_)

    def get_products(self):  # noqa
        obj = File('products.json')
        list_ = obj.read()
        if list_:
            for i in list_:
                print(f'Name: {i["name"]}\nPrice: {i["price"]}\nCount: {i["count"]}\n<------------------>')
        else:
            print('Product not found!')

    def remove_product(self, name, count):  # noqa
        obj = File('products.json')
        list_ = obj.read()
        dicts = {}
        for i in list_:
            if i['name'] == name and count <= i['count']:
                dicts['name'] = name
                dicts['price'] = count * i['price']
                dicts['count'] = count
                i['count'] -= count
                obj.write(list_)
                return dicts
        else:
            return False
