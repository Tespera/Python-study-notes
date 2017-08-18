# Author:Tespera

age_of_Tespera = 22

count = 0
while count < 3:
# for i in range(3)：
    guess_age = int(input("guess age:"))
    if  guess_age == age_of_Tespera:
        print("Yes,you got it. ")
        break
    elif guess_age > age_of_Tespera:
        print("Think smaller... ")
    else:
        print("Think bigger...")

    count +=1

else:
    print("You have tried too many times...")






