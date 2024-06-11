import random, string, time
Vault = dict()

def main():
   
    while(True):
        
        print("Loading Menu...", end='\r')
        time.sleep(1.5)
     
        menu = int(input("Enter 1 to Encrypt Your Code\nEnter 2 to Decrypt Your Code \n: ",))
        if(menu == 1): 

            code = str(input("Enter Your Code: "))

            PersonalKey = int(input("Assign a key in Number: "))
            time.sleep(3)
    
            if ' ' in code:
                    
                
                print("Your code shouldn't contain any space!")
                
            else:
                print("\nStoring your code....", end='\r')

                time.sleep(2.5)

                Encryptedcode = Encryptor(PersonalKey, code)

                print("Your Code has been Stored Successfully! \n")
                print(f"Here is your encrypted code: {Encryptedcode}\n")

            time.sleep(3)

        elif(menu == 2):
            
            print("\nLoading Screen....", end='\r')

            Encryptedcode = input("Enter your encrypted code: ")
            EncryptedKey = int(input(f"Enter The key for {Encryptedcode}: "))
         
            
            time.sleep(3)
            Decryptor(EncryptedKey, Encryptedcode)
            print()
       

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

def EncryptVault(newkey, encryptedcode):

    
    global Vault
    Vault[newkey] = encryptedcode

def Encryptor(personalkey, code):

    if(len(code) >= 3 or code.isspace() != True):
        
        FirstEncryption = code[1:] + code[0]
        FinalEncryption =  (randomword(3) + FirstEncryption + randomword(3))[::-1]

    else:
        FinalEncryption = code[::-1]

    EncryptVault(personalkey, FinalEncryption)
    return FinalEncryption
  
    
def Decryptor(key, encryptedcode):

    if key in Vault:
        if(Vault.get(key) == encryptedcode):


            FirstDecryption = (encryptedcode[::-1])[3:-3]
            FinalDecryption = FirstDecryption[-1] + FirstDecryption[:-1]

            time.sleep(3)
            print(f"\nHere is your Decrypted Message: {FinalDecryption}\n")
            
        else:
            print(f"No such code like {encryptedcode}")
            
    else:
        print(f"No key found") 

main()
