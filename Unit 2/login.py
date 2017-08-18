# Author:Tespera
# Date:2017.8.14


_username = 'Tespera'
_password = 'abc123'
username = input("username:")
# password = getpass.getpass("password:")
password = input("password:")

if _username == username and _password == password:
    print("Welcome user {name} login..." .format(name=username))
else:
    print("Invalid username or password!")
