# '''def greet(name):
#     print(f"hello {name}")
#     print(f"how are you {name}")
 
# x = input("enter your name: ") 
   
# greet (x)'''

# def greetWith(name,location):
#     print(f"hello {name}")
#     print(f"what is it like in {location}")
    
# name = input("enter your name: ")
# location = input("enter your location: ")    
# greetWith(name,location)

# def paintCalc(height,weight,cover):
#     numsCans = (height+weight)/cover
#     print(f"you will need {numsCans} cans of paint")
# code = input("enter the code: ")
# def caeser():
#     for i in code:
#         if i.isalpha():
#             if i.islower():
#                 print(chr((ord(i)+3-97)%26+97),end="")
#             else:
#                 print(chr((ord(i)+3-65)%26+65),end="")
#         else:
#             print(i,end="")
            
# caeser()
        
# h = int(input("height:"))
# w = int(input("width:"))
# c = int(input("area:"))

# coverage_area = round((h*w)/c)
# print(f"paints of can you need {coverage_area}")

# def paint_cans(h,w,c):
#     coverage_area = round((h*w)/c)
#     print(f"paints of can you need {coverage_area}")

# h = int(input("height:"))
# w = int(input("width:"))
# c = int(input("area:"))
# paint_cans(h,w,c)
    
# def prime_no(no):
#     is_prime = True
#     for i in range(2,no):
#         if no % i == 0:
#             is_prime = False
#     if is_prime == True :
#         print(f"{no} is prime number")
#     else: 
#         print("its not prime number")
    
   
    
# no = int(input("no"))
# prime_no(no)


# alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# #direction = input("type 'encode' to encrypt, type 'decode' to decrypt:\n")

# def encrypt(plain_text,shift_amount):
#     cipher_list = ""
#     for letter in plain_text :
#         position = alphalist.index(letter)
#         new_position = (position + shift_amount) % 26
#         new_letter = alphalist[new_position]
#         cipher_list += new_letter
#         print(f"encrypted text is {cipher_list}")
        
# text = input("Type your message:\n ").lower()
# shift = int(input("type the shift no:"))

# encrypt(text,shift)
    
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet_list.index(letter)
        new_position = (position + shift_amount) 
        new_letter = alphabet_list[new_position]
        cipher_text += new_letter
    print(f"The encrypted text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position  = alphabet_list.index(letter)
        new_position = (position - shift_amount) 
        new_letter = alphabet_list[new_position]
        plain_text += new_letter
    print(f"The decrypted text is {plain_text}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n ").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(cipher_text=text, shift_amount=shift)


    