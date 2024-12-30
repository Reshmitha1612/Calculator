import hashlib
import os

def create_salt():
    return os.urandom(16).hex()

def generate_hash(password,salt):
    iterations = 100000
    encoded_password = password.encode()
    hash_name = 'sha256'
    salt_bytes = bytes.fromhex(salt)
    return hashlib.pbkdf2_hmac(hash_name,encoded_password,salt_bytes,iterations)

users = []

def sign_up(username, password):
    for user in users:
        if user["username"] == username:
            print("This name is already taken. Please try a different one.")
            return
    salt = create_salt()
    hashed_password = generate_hash(password, salt)
    users.append({'username': username, 'password': hashed_password, 'salt': salt})
    print("Your sign up is successful! \U0001F973 \U0001F973....")


def login(username,password):
    user_found = False
    for user in users:
        if user["username"] == username:
            user_found = True
            stored_hashed_password = user['password']
            salt = user['salt']
            hashed_password = generate_hash(password,salt)
            if hashed_password == stored_hashed_password:
                print("successfully logged in! \U0001F603 \U0001F603")
            else :
                print("Incorrect password!Please enter correct password \U0001F9D0 \U0001F9D0...")
            break
    if not user_found:
            print("No such username is found \U0001F643 \U0001F643...")
        


def main():
    print("Welcome to the authentication sysytem \U0001F603 \U0001F603...")
    while True:
        print("\nSelect one of three choices: ")
        print("[1]sign up")
        print("[2]login")
        print("[3]Leave site")
        select = input("Select your choice: ")
        if select == '1' :
            username = input("USERNAME:")
            password = input("PASSWORD:")
            sign_up(username,password)
        elif select == '2' :
            username = input("USERNAME:")
            password = input("PASSWORD:")
            login(username,password)
        elif select == '3' :
            print("Leaving site! Bye Bye \U0001F61E \U0001F61E \U0001F61E....")
            print("See you again \U0001F600 \U0001F600")
            break
        else:
            print("Invalid input!Please try again \U0001F605....")

if __name__=="__main__":
    main()