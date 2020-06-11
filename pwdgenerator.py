# 3.Write a password generator in Python. Be creative with how you generate passwords - strong
# passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The
# passwords should be random, generating a new password every time the user asks for a new
# password. Include your run-time code in a main method.

# Minimum length of pwd = 8
# Atleast 1 lowercase
# Atleast 1 Uppercase
# Atleast 1 Number
# Atleast 1 special character from ~`!@#$%^&*';:/\?><,
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choice, randrange, shuffle

def pwdgen(l=8):
    if l < 8:
        l = 8
    while True:
        pwd=[choice(ascii_lowercase), choice(ascii_uppercase), choice(digits), choice(punctuation)]
        while len(pwd) <= l:
            x = randrange(4)
            if x == 0:
                pwd.append(choice(ascii_lowercase))
            elif x == 1:
                pwd.append(choice(ascii_uppercase))
            elif x == 2:
                pwd.append(choice(digits))
            else:
                pwd.append(choice(punctuation))
        
        shuffle(pwd)
        return ''.join(pwd)

if __name__ == "__main__":
    pwdlen = 0
    while not pwdlen >= 8:
        pwdlen = int(input("Type password length (has to be >= 8): "))
        if not pwdlen >= 8:
            print("Length of pasword has to more than 8. Please provide a valid length.")

    # a = pwdgen(pwdlen)
    # print(next(a))
    # print(next(a))
    # print(next(a))
    print(pwdgen(pwdlen))
    print(pwdgen(pwdlen))
    print(pwdgen(pwdlen))
