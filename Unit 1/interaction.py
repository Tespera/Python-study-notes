# Author:Tespera

# ---1---
username = input("username:")
password = input("password:")
print(username,password)

# ---2---
name = input("name:")
age = int(input("age:"))
print(type(age) , type( str(age)))
job = input("job:")
salary = input("salary:")

#格式化输出--1--
info = '''
--------info of %s  --------
Name:%s
Age:%s
Job:%s
Salary:%s
'''%(name,name,age,job,salary)


#格式化输出--2--
info2 = '''
--------info of {_name}  --------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
'''.format(_name=name,
           _age=age,
           _job=job,
           _salary=salary)


#格式化输出--3--
info3 = '''
--------info of {0}  --------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
'''.format(name,age,job,salary)
print(info3)


