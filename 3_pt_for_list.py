# caesar cypher
# https://www.youtube.com/watch?v=sMOZf4GN3oc

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

secret = "abc"
# 1. loop through secret
# for x in secret:
#     print(x)


# 2. next we want to check if character of secret is available in alphabet list
# for x in secret:
#     if x in alphabet:
#         # if secret character found, print "yes"
#         print("yes")

# 3. check index number of secret character in alphabet
# for x in secret:
#     if x in alphabet:
#         # print(alphabet.index(x))

#         # shift alphabet index by 3
#         shift_index = alphabet.index(x)+3
#         print(alphabet[shift_index])

# 4. create new encrypt_secret
# encrypt_secret = ""
# for x in secret:
#     if x in alphabet:
#         # print(alphabet.index(x))

#         # shift alphabet index by 3
#         shift_index = alphabet.index(x)+3
#         encrypt_secret += alphabet[shift_index]

# print(encrypt_secret)
