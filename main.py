from cryptography.fernet import Fernet

# def create_key():
#     key = Fernet.generate_key()
#     with open('key.key', 'wb') as file:
#         file.write(key)

# create_key()

def get_key():
    with open('key.key', 'r') as file:
        key = file.read()
    return key

key = get_key()
f = Fernet(key)

def view():
    with open('passwords.txt', 'r') as file:
        for line in file.readlines():
            name, passw = line.rstrip().split("|")
            passw = f.decrypt(passw.encode()).decode()
            print(f"Account name: {name} | Password: {passw}")

def add():
    with open('passwords.txt', 'a') as file:
        account_name = input("Account name: ")
        password = input("Password: ")
        token = f.encrypt(password.encode()).decode()
        file.write(f"{account_name}|{token}\n")

while True:
    mode = input("Would you like to add new password or view existing ones (add/view/quit)? ")
    if mode == "add":
        add()
    elif mode == "view":
        view()
    elif mode == "quit":
        break
    else:
        "Wrong mode. Try again."
