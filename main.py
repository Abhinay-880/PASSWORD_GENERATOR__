# PASSWORD GENERATOR
import random
password_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',0, 1, 2, 3, 4, 5, 6, 7, 8, 9,'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', ':', ';', ',', '.', '?', '/', '-', '_', '+', '=', '<', '>', '|']

password_length = int(input("Enter the length of password you want : "))
final_password_list = []
b = 0
start = True
while start:

    if b <= password_length:
        letter = random.choice(password_characters)
        final_password_list.append(letter)
        b += 1
    else:
        print("YOUR PASSWORD IS : ", end=" ")
        for i in final_password_list:
            print(i, end=' ')
            start = False
