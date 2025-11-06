# name = input("Enter your full name:  ")

# phone_number = input(("Enter your phone #: "))

# result = len(name)

# result = name.find("M")

# name = name.capitalize()

# name = name.upper()

# name = name.lower()

# result = name.isdigit() ## denna returnerar bara "True" om alla tecken i strängen är siffror

# result = name.isalpha() # returnerar bara true om det är enbart bokstäver i strängen

# result = phone_number.count("-")

# phone_number = phone_number.replace("-", " ")

# print(phone_number)


# validate user input exercise

# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

# username = input("Enter your user name: ")

# if len(username) > 12 or not username.isalpha() or " " in username:
#     print("Not valid username")
# else:
#     print("Valid username")

# indexing  = accessing elements of a seqeunce using [] (indexing operator)
#             [start: end : step]
# 
#  

credit_number = "3456-4546-4545"



# print(credit_number[0])

# print(credit_number[0:4])

# print(credit_number[5:9])

# print(credit_number[5:])

# print(credit_number[-4:])


# last_digits = credit_number[-4:]

# print(f"xxxx-xxxx-{last_digits}")

# try:
        
#     number = int(input("Enter a number " ))

#     print(1/number)

# except ZeroDivisionError:
#     print("You cant divide by zero IDIOT!")
# except ValueError:
#     print("Enter only numbers!")
# except Exception:
#     print("Something went wrong!")
# finally:
#     print("Do some clean up here")


principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("principle cant be less than or equal to zero")

while rate <=0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest cant be less than or equal to zero")
        
while time <= 0:
    time = int(input("Enter the time in years:  "))
    if time <= 0:
        print("Time cant be less than or equal to zero")

total = principle * pow((1+ rate / 100), time)

print(f"Balance after {time} year/s: ${total:.2f} ")

