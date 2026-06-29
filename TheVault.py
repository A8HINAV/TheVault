# Landing
print("\n\tTheVault")

# Main Variables
database = {}
gbpass = ""
enc_gb = ""
decgb = ""

# Loads saved data back into Variables
with open("secrets.txt", "a", encoding="utf-8") as f:
    pass

with open("secretgb.txt","a"):
    pass

with open("secretgb.txt") as o:
    gbpass = o.read()

with open("secrets.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if ":" in line:
            title, secret = line.split(":", 1)
            database[title] = secret

# User Choice
try:
    choice = int(input("\nPress : \n0 > For New Users \n1 > Store\n2 > Retrieve\n3 > Settings\n\n"))
except Exception:
    print("Make Sure the Value matches the Given Menu Numbers.")

# Cases
match choice:
    case 0:
        print("\n\n Hi, Thank You for Using TheVault \n This page is an essential to-do for the New users ! \n You have to make a Global Password to access your Stored Data, \n **Once set, you cannot change it,so choose it wisely and keep it in your Mind or you will lose all the Stored Data (if any)** ")
        gbpass = input("\n Setup a Global Password : ")
        for char in gbpass:
            value = ord(char) + 3
            enc_char = chr(value)
            enc_gb += enc_char

        with open("secretgb.txt","w") as g:
            g.write(enc_gb)
            print(f"You set <{gbpass}> as Password, Keep it in your Mind \n Continue Using!")
            gbpass = "null"
    case 1:
        print("\nStoring...\n")
        title = input("Add a Name as an Identifier for the Secret : ")
        secret = input("Add the Secret to Encrypt and Store : ")
        enc_secret = ""

        # Encryption
        for char in secret:
            value = ord(char) + 3
            enc_char = chr(value)
            enc_secret += enc_char

        # Store in Dictionary
        database[title] = enc_secret

        # Save to File
        with open("secrets.txt", "a", encoding="utf-8") as ap:
            ap.write(title + ":" + enc_secret + "\n")
        print("\nData Saved Successfully!")
    case 2:
        print("\nRetrieving...\n")
        if len(database) == 0:
            print("No Data Found!")
        else:
            with open("secretgb.txt") as gb:
                gb = gb.read()
            for char in gb:
                temp = ord(char) - 3
                temp2 = chr(temp)
                decgb += temp2

            uspass = input("Enter the Global Password to access :")
            if uspass != decgb:
                print("Wrong Global Password ! You cannot access TheVault without it.\nIf you haven't created any Password in here, make sure to check out <For New users> from menu")
            elif uspass == decgb:
                print("\nChoose a Secret to Reveal :\n")                     
                
                # Show only identifiers
                for key in database.keys():
                    print(">", key)

                # User selects identifier
                n = input("\nType Identifier : ")

                # Check if identifier exists
                if n in database:
                    value = database[n]
                    decchar = ""
                # Decryption
                for char in value:
                    temp = ord(char) - 3
                    temp2 = chr(temp)
                    decchar += temp2
                print("\n Secret :")
                print(n, ":", decchar)
            else:
                print("Identifier not found!")
        print("\nThank You!")

    case 3:
        try:
            choice2 = int(input("\nSettings \n 4 > Delete all Data\n 5 > Info \n"))
        except Exception:
            print("Make Sure the Value matches the Given Menu Numbers.")
        match choice2:
            case 4:
                with open("secrets.txt","w") as w:
                    w.write("")
                    print("Data wiped Successfully !")
            case 5:
                print("\n\n Info : \n Dev : Abhinav Tiwari \n Version Info : 1.7 (10:22:47;23.5.26) \n Support : +91 9565659899 \n Discord : @a8hinav \n\n Feel free to Reach out !\n")
            case _:
                print("Invalid Choice !")
    case _:
        print("Invalid Selection, Maybe Try next time.")