import encryption as en

def decryption(msg,key):
    if(len(key)<len(msg)):
        print("Error, key is shorter than msg.")
        return 0
    dict = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,
                     'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    reverse_dict = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',
                    13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}           
    msg_num = []
    key_num = []
    for var in msg:
        msg_num.append(dict[var])
    for var in key:
        key_num.append(dict[var])
    k = 0
    for _ in msg_num:
        msg_num[k] = (msg_num[k] - key_num[k]) % len(dict) 
        k += 1
    encrypted_word = []
    for num in msg_num:
         encrypted_word.append(reverse_dict[num])
    return ''.join(encrypted_word) #convert list to string

def main():
    word = input("Insert a word: ")
    key = input("Insert a key: ")
    print(f"word: {word}")
    print(f"key: {key}")
    encrypted_word = en.encryption(word,key)
    print(f"encrypted word: {encrypted_word}")
    decrypted_word = decryption(encrypted_word,key)
    print(f"decrypted word: {decrypted_word}")

if __name__ == "__main__":
    main()