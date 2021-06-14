import csv
from datetime import datetime
from os import path
from getters import get_users, get_parts


def make_order(user, selected_parts, total_price, profit):
    order = dict()
    order["date"] = datetime.now()
    order["user"] = user.first_name
    order["ordered_parts"] = ",".join([x.product_name for x in selected_parts])
    order["total_costs"] = total_price
    order["profit"] = profit
    file_exist = path.isfile("csv_data/orders.csv")
    with open("csv_data/orders.csv", "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=order.keys(), delimiter=",")
        if not file_exist:
            writer.writeheader()
        writer.writerow(order)
    print("Your order was successfully completed")


def show_parts(user):
    parts = get_parts()
    print("Available parts")
    print("Code, Name, Application, Manufacturer")
    for part in parts:
        print(f"{part.code}, {part.product_name}, {part.application}, {part.manufacturer}")
    user_picks = input("Please enter part(s) code to view more details(example 1, 2, 3....)\n-->").split()
    selected_parts = []
    for part in parts:
        for pick in user_picks:
            if part.code == pick:
                selected_parts.append(part)
    for part in selected_parts:
        part.print_info()
        print(25 * "*")
    print(25 * "=")
    user_menu(user)


def buy_parts(user):
    parts = get_parts()
    print("Available parts")
    print("Code, Name, Application Price")
    for part in parts:
        print(f"{part.code}, {part.product_name}, {part.application}, {part.client_price}")
    user_choice = input("Please select part(s) to buy using code(example 1, 2, 3..)\n-->").split()
    selected_parts = []
    for part in parts:
        for choice in user_choice:
            if part.code == choice:
                selected_parts.append(part)

    total_price = 0
    profit = 0
    for part in selected_parts:
        part.print_info()
        total_price += part.sell_price()
        profit += part.sell_price() - part.buy_price()
        print(25 * "*")
    print(f"Total price is {total_price:.2f}$")
    action = input("Confirm the order(y)\n-->").lower()
    if action == "y" or "yes":
        make_order(user, selected_parts, total_price, profit)
    else:
        buy_parts(user)


def user_menu(user):
    print(f"Welcome {user.first_name}".upper())
    print("Please enter action:\n1.To view all parts\n2.To buy parts\n3.Logout")
    if user.role == "admin":
        print('0.Admin menu\n-->')
    action = input()
    if action == "1":
        show_parts(user)
    elif action == "2":
        buy_parts(user)
        user_menu(user)
    elif action == "3":
        main_menu()
    elif action == "0" and user.role == "admin":
        admin_menu(user)
    else:
        print("Invalid action, try again")
        user_menu(user)


def csv_users_update(users):
    with open("csv_data/users_data.csv", "w", newline="") as f:
        fieldnames = users[0].__dict__.keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        for user in users:
            writer.writerow(user.__dict__)


def update_users(user):
    users = get_users()
    for u in users:
        if u.first_name == user.first_name:
            print(">", end="")
        u.print_info()
    selected_user_first_name = input("Select user by first name: ")
    update_users = False
    for u in users:
        if u.first_name == selected_user_first_name:
            u.role = input("Enter new role: ")
            u.first_name = input("Enter new first name: ")
            u.last_name = input("Enter new last name: ")
            u.email = input("Enter new email: ")
            u.phone_number = input("Enter new phone number: ")
            u.password = input("Enter new password: ")
            update_users = True
            break
    else:
        print("First name not found: ")
    if update_users:
        csv_users_update(users)
        print("User was successfully updated: ")


def find_user(first_name, password):
    users = get_users()
    for user in users:
        if user.first_name == first_name and user.password == password:
            return user
    return None


def main_menu():
    while True:
        print(35 * "-")
        print()
        print("Welcome to AUTOPARTS-BG.COM")
        print()
        print(35 * "-")
        user_action = input("""
      MAIN MENU
Please choose an option
1.Registration
2.Log in\n-->
""")
        if user_action == "1":
            registration_form()
            break
        elif user_action == "2":
            log_in()
            break
        else:
            print("Please enter valid option! ")


def log_in():
    while True:
        first_name = input("Please enter your first name\n-->").lower()
        password = input("Please enter your password\n-->")
        user = find_user(first_name, password)
        if user:
            user_menu(user)
            break
        else:
            print("Wrong first name or password, please try again")


def show_reg_users():
    users = get_users()
    print("Role: First name, Last name, Email, Date Created")
    all_users = []
    for user in users:
        all_users.append(user)
    for u in all_users:
        print(25 * "=")
        u.print_info()
    print(25 * "-")


def admin_menu(user):
    print("Please select action:\n1.Update user info\n2.Show registered users\n-->")
    action = input()
    if action == "1":
        update_users(user)
    elif action == "2":
        show_reg_users()
    user_menu(user)


def registration_form():
    while True:
        today = datetime.now()
        user = dict()
        user["role"] = input("Please enter your role\n-->")
        user["first_name"] = input("Please enter your first name\n-->")
        user["last_name"] = input("Please enter your last name\n-->")
        user["email"] = input("Please enter your email\n-->")
        user["phone_number"] = input("Please enter your phone number\n-->")
        user["password"] = input("Please enter your password\n-->")
        user["created"] = today.strftime("%d.%m.%Y-%H:%M:%S")
        existing_file = path.isfile("csv_data/users_data.csv")
        with open("csv_data/users_data.csv", "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=user.keys())
            if not existing_file:
                writer.writeheader()
            writer.writerow(user)
        main_menu()


main_menu()
