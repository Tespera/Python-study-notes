# Author:Tespera
# Date:2017.8.15

_username = 'Tespera'
_password = 'abc123'

print("----- Please login... -----")
username = input("Please input your username:")
password = input("Please input your password:")

if _username == username and _password == password:
    print("Welcome {name} login...".format(name = username))
else:
    print("Invalid username or password!")


product_list = [
    ('iPhone',5800),
    ('Mac Pro',9800),
    ('Bike',800),
    ('Watch',1060),
    ('Coffee',120),
    ('Book',50),
    ]
shopping_list = []
salary = input("Please input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index, item in enumerate(product_list):
            print(index,item)

        user_choice = input("Select what you want to buy >>>:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                product_item = product_list[user_choice]
                if product_item[1] <= salary:  #买得起
                    shopping_list.append(product_item)
                    salary -= product_item[1]
                    print("Added %s into shopping cart ,your current balance is \033[31;1m%s\033[0m" %(product_item,salary) )
                else:
                    print("\033[45;1m你的余额只剩[%s]啦，请充值后继续购买！\033[0m" % salary)
                    break
            else:
                print("product code [%s] is not exist!" % user_choice)
        elif user_choice == 'q':
            print("--------shopping list------")
            for p in shopping_list:
                print(p)
            print("Your current balance:", salary)
            exit()
        else:
            print("invalid option")




