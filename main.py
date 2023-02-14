#1

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
valid = {"username": "admin", "password": "admin"}
if username != valid['username'] and password != valid['password']:
    print("Credentials are invalid")
else:
    print(f"Welcome, {username}!") 
    
#2

from datetime import datetime

def isweekend(date = datetime.now()):
    if date.weekday() == 5 or date.weekday() == 6:
        return True
    else:
        return False

today = datetime(2021, 8, 9)
print(isweekend(today))

#3

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
valid = {"username": "admin", "password": "admin"}
today = datetime(2021, 8, 6)
if (username == valid['username'] and password == valid['password']) or isweekend(today) :
    print(f"Welcome, {username}!")
else:
     print("Credentials are invalid!")

#4

def get_user(username,password):
    for user in users:
        if username == user['name'] and password == user['password']:
            return user
    return None
    
users = [
    {
        "name": "Holly",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "password": "pan"
    },
    {
        "name": "Janis",
        "password": "joplin"
    }
]

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")

if get_user(username,password):
    print(get_user(username,password))
else:
    print("An error occurred. You are not authorized.")

#5

def is_student_or_anonymous(user):
    return user['type'] in ['Student', 'Anonymous']

def show_offers(username, password):
    for user in users:
        if username == user['name'] and password == user['password'] and user['type'] == "Student":
            print("We have great courses to offer you!")
        elif username == "Anonymus" and password != user['password']:
            print("We have great courses to offer you!")
            break
    return None
users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan"
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
show_offers(username, password)