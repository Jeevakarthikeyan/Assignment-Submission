count = 0
count = count+1
username = input("Enter your username: ")
password = input("Enter your password: ")
while username == username and password == password:
    if count==5:
        print("Hey! Your account will Blocked for next 24 hours")
        break
    elif username == "india" and password == "ind":
        print("Congratulation! your login succesfully")
        break 
    elif username == "india" and password!="ind":
        print("your password is wrong try again")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        count+=1
        continue
    elif username!= "india" and password =="ind":
        print("your username is wrong try again")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        count+=1
        continue
    elif username!= "india" and password!="ind":
        print("both username and password is wrong again try it")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        count+=1
        continue