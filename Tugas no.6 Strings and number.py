while(True):
 message = input("What would you like the message to say? ").lower()
 newmessage = ""
 for i in range(0,26):
    for letter in message:
        decimal = (ord(letter))
        decimal = decimal + i
        newmessage += (chr(decimal))

    print (newmessage)
    newmessage = ""