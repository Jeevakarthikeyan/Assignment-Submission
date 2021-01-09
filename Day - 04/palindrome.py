
def funct():
    s = input("Enter your String: ")
    print(s[::-1])
    if s==s[::-1]:
        print("Yeah! It's a palindrome")
    else:
        print("Isn't palindrom")
        
funct()
