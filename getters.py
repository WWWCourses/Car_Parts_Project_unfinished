import csv
from os import path
from classes import Users, Car_parts, Orders


def get_users():
    users_list = []
    if path.isfile("csv_data/users_data.csv"):
        with open("csv_data/users_data.csv", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                users_list.append(Users(**row))
    return users_list


def get_parts():
    parts_list = []
    if path.isfile("csv_data/Car_parts.csv"):
        with open("csv_data/Car_parts.csv", newline="") as f:
            reader = csv.DictReader(f, delimiter=",")
            for row in reader:
                parts_list.append(Car_parts(**row))
    return parts_list


def get_orders():
    orders_list = []
    if path.isfile("csv_data/orders.csv"):
        with open("csv_data/orders.csv", newline="") as f:
            reader = csv.DictReader(f, delimiter=",")
            for row in reader:
                orders_list.append(Orders(**row))
    return orders_list
