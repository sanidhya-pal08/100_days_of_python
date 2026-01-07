word_list=[
 'a','b','c','d','e','f','g','h','i','j','k','l','m',
 'n','o','p','q','r','s','t','u','v','w','x','y','z',
 'a','b','c','d','e','f','g','h','i','j','k','l','m',
 'n','o','p','q','r','s','t','u','v','w','x','y','z'
]
# def encrypt_the_code(original_message,shift_number):
#     leng=len(original_message)
#     encrypted_list=["_"]*leng
#     for i in range(0,leng):
#          index=0
#          found=False
#          for j in word_list:
#             if original_message[i]==j:
#                 encrypted_list[i]=word_list[index+shift_number]
#                 found=True
#                 break
#             index+=1
#          if not found:
#             encrypted_list[i]==original_message[i]
#     encrypted_code="".join(encrypted_list)
#     print(encrypted_code)




#encryption function using ord()=> converts letters into ascii values
def encrypt_the_code(original_message,shift_number):
    encrypted_list=[]
    leng=len(original_message)
    for i in range(0,leng):
        num=ord(original_message[i])
        if 97<=num<=122:
            encrypted_list.append(chr((num-97 + shift_number)%26 + 97))
        else:
            encrypted_list.append(original_message[i])
    encrypted_code="".join(encrypted_list)
    return encrypted_code

def decrypt_the_code(code,shift_number):
    decrypted_list=[]
    leng=len(code)
    for i in code:
        num=ord(i)
        if 97<=num<=122:
            decrypted_list.append(chr((num-97-shift_number)%26+97))
        else:
            decrypted_list.append(i)
    decrypted_code=''.join(decrypted_list)
    return decrypted_code

message=str(input("enter the original message"))
shift=int(input("enter the shift number"))
coded_message=input("enter the coded message")
code=encrypt_the_code(message,shift)
print(code)
original=decrypt_the_code(coded_message,shift)
print(original)
