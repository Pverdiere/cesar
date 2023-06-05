def chiffrement(msg:str,key:list):
    new_msg = ""
    i=0
    for char in msg:
        new_msg += chr(ord(char) + key[i])
        if(i==len(key)-1):
            i=0
        else:
            i +=1
    return new_msg

def dechiffrement(msg:str,key:list):
    new_msg = ""
    i=0
    for char in msg:
        new_msg += chr(ord(char) - key[i])
        if(i==len(key)-1):
            i=0
        else:
            i +=1
    return new_msg

msg = "C'est un incroyable message! Et puis en plus, imagine tous les avantage possible avec ce type de message."
key = [4,7,3,1,9]

#msg_chiffre = chiffrement(msg,key)
#print(msg_chiffre)
#msg_dechiffre = dechiffrement(msg_chiffre,key)
#print(msg_dechiffre)