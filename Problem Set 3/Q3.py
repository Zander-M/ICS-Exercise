import random
import string

# Encodes characters according to a given offset
# DO NOT EDIT THIS
def cipher(c,offset):
    if c in string.ascii_lowercase:
        if ord(c) + offset <= 122:
            return chr( ord(c) + offset )
        else:
            return chr( ord(c) + offset - 26 )
    elif c in string.ascii_uppercase:
        if ord(c) + offset <= 90:
            return chr( ord(c) + offset )
        else:
            return chr( ord(c) + offset - 26 )
    else:
        return c

# Generates a random encoded message with a random offset
# DO NOT EDIT THIS
def generate_encoded_msg(message_list):
    message = random.choice(message_list)
    offset = random.randint(1,25)
    encoded_message = ""
    for c in message:
        encoded_message += cipher(c,offset)
    return encoded_message
    
        
"""
 Your job is to implement this function
 Your are given the following arguments:
 (1) The encoded message with a random Caesar cipher offset
 (2) The list of all decoded messages

 Use this information to get your function to return the decoded message & the original offset
 Use any approach you deem fit to solve the problem.
 Brute force (IE, trying every offset & seeing if you get a match) is a good first point of approach.
 You are encouraged to write any additional function(s) you may need
 HOWEVER, you may NOT edit any other part of this code.
"""
def decode_msg(message, message_list):
    return (message, 0)

# Main code - DO NOT EDIT THIS    
if __name__ == "__main__":
    try:
        message_list = open("messagelist.txt","r").read().split("\n")
    except FileNotFoundError:
        print("messagelist.txt not found. Make sure it is in the same directory!")
        input("Press any key to terminate the program.")
        exit(0)

    encoded_msg = generate_encoded_msg(message_list)
    print("Your encoded message is:\n>>> " + encoded_msg)

    print()
    
    decoded_msg, offset = decode_msg(encoded_msg, message_list)
    print("The decoded message is:\n>>> " + decoded_msg + "\nThe substitution offset =", offset)
