from functions import User, Product


def login_menu(users, user, username):
    admin = users.check_admin()
    if user and not admin:
        while True:
            print('1) Add product: \n2) My Products: \n3) Statistic: \n4) Logout: ')
            basic = input('>>> ')
            if basic == '1':
                out = Product()
                out.get_products()
                add = input('Name: ')
                count = int(input('Count: '))
                if count >= 0:
                    result = out.remove_product(add, count)
                    if result:
                        id = users.get_id(username) # noqa
                        users.add_product(result, id)
                        print('Job Done!\n')
                    else:
                        print('Something went wrong!\n')
                else:
                    print('Page Not found!')
            elif basic == '2':
                id = users.get_id(username)# noqa
                linked = users.my_products(id)
                if linked:
                    print('Your Products!\n<------------------>')
                    for i in linked:
                        print(f"Name: {i[0]}\nCount: {i[1]}\nTime: {i[2]}\n<------------------>")
                    print('Job Done!\n')
                else:
                    print('Something went wrong!\n')
            elif basic == '3':
                id = users.get_id(username)# noqa
                user = users.get_road(id)
                print('Your report: ', user)
                print('Job Done!\n')
                continue
            elif basic == '4':
                print('Logout was successful!\n')
                main()
                break
            else:
                print('No such entry!\n')
                continue

    elif user and admin:
        while True:
            print('1) Products: \n2) Add Product: \n3) Add admin: \n4) Logout')
            basic = input('>>> ')
            if basic == '1':
                product = Product()
                product.get_products()
                print('Job Done!\n')
                continue
            elif basic == '2':
                name = input('Name: ')
                price = int(input('Price: '))
                count = int(input('Count: '))
                if count >= 0 and price >= 0:
                    Product(name, price, count).add_products()
                    print('Job Done!\n')
                    continue
                else:
                    print('Page Not found!')
            elif basic == '3':
                username = input('Username: ')
                users.add_admin(username)
                print('Job Done!')
            elif basic == '4':
                print('Logout was successful!\n')
                main()
                break
            else:
                print('No such entry!')
                continue
    else:
        print('No such user found!')
        main()


def main():
    print("\nSuper Merket\n")  # noqa
    print('1) Login: \n2) Register: \n3) Exit: ')
    response = input('>>> ')
    if response == '1':
        username = input('Username: ')
        password = input('Password: ')
        users = User(username, password)
        user = users.login(password)
        login_menu(users, user, username)
    elif response == '2':
        username = input('Username: ')
        password = input('Password: ')
        user = User(username, password).check_user()
        if user:
            User(username, password).register()
            print('Job Done!\n')
            main()
        else:
            print('Such a username exist!\n')
            main()
    elif response == '3':
        print('Logout was successful!\n')
        return
    else:
        print('No such section exists!\n')


main()
