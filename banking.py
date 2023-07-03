# Write your code here
import random
import sqlite3

MENU_PROGRAM = """
1. Create an account
2. Log into account
0. Exit"""

MENU_CARD = """
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit"""


def create_card_number():
    """Luhn algorithm"""

    card_number = [4, 0, 0, 0, 0, 0]
    for _ in range(9):
        card_number.append(random.randrange(10))
    number = [n for n in card_number]
    for n in range(0, 15, 2):
        number[n] *= 2
    for n in range(15):
        if number[n] > 9:
            number[n] -= 9
    card_number.append(0 if sum(number) % 10 == 0 else 10 - sum(number) % 10)
    return "".join([str(n) for n in card_number])


def is_check_card_number(card):
    if len(card) != 16:
        return False
    number = card[:-1]
    number = [int(n) for n in number]
    for n in range(0, 15, 2):
        number[n] *= 2
    for n in range(15):
        if number[n] > 9:
            number[n] -= 9
    number.append(int(card[-1]))
    if sum(number) % 10 == 0:
        return True
    else:
        return False


def generation_number(digit):
    number = ""
    for _ in range(digit):
        number += str(random.randrange(10))
    return number


def create_account(file_name):
    conn = sqlite3.connect(file_name)
    cur = conn.cursor()
    id_a = generation_number(6)
    card = create_card_number()
    pin = generation_number(4)
    account = [id_a, card, pin, 0]
    cur.execute("INSERT INTO card VALUES (?, ?, ?, ?)", account)
    print("\nYour card has been created"
          "\nYour card number:\n{}"
          "\nYour card PIN:\n{}".format(card, pin))
    conn.commit()
    conn.close()


def create_database(file_name):
    conn = sqlite3.connect(file_name)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS card (
                id INTEGER,
                number TEXT,
                pin TEXT,
                balance INTEGER DEFAULT 0)""")
    conn.commit()
    conn.close()


def select_database(file_name):
    conn = sqlite3.connect(file_name)
    cur = conn.cursor()
    cur.execute('SELECT id, number, pin, balance FROM card')
    account = cur.fetchall()
    conn.commit()
    conn.close()
    return account


def select_database_account(file_name, number, pin):
    conn = sqlite3.connect(file_name)
    cur = conn.cursor()
    data = [number, pin]
    cur.execute("SELECT id, number, pin, balance FROM card "
                "WHERE number = ? AND pin == ?", data)
    account = cur.fetchone()
    conn.commit()
    conn.close()
    return account


def select_database_card_number(file_name, number):
    conn = sqlite3.connect(file_name)
    cur = conn.cursor()
    data = [number]
    cur.execute("SELECT id, number, pin, balance FROM card "
                "WHERE number = ?", data)
    account = cur.fetchone()
    conn.commit()
    conn.close()
    return account


def add_database_balance(file_name, number, money):
    conn = sqlite3.connect(file_name)
    cur = conn.cursor()
    data = [money, number]
    cur.execute("UPDATE card SET balance = balance + ? "
                "WHERE number = ?", data)
    conn.commit()
    conn.close()


def update_database_transfer(file_name, number, num_transfer, money):
    conn = sqlite3.connect(file_name)
    cur = conn.cursor()
    data = [money, number]
    cur.execute("UPDATE card SET balance = balance - ? "
                "WHERE number = ?", data)
    conn.commit()
    conn.close()
    print("Success!\n")
    add_database_balance(file_name, num_transfer, money)


def log_into_account(file_name):
    number = input("\nEnter your card number:\n> ")
    pin = input("Enter your PIN:\n> ")
    card = select_database_account(file_name, number, pin)
    if not card:
        print("\nWrong card number or PIN!")
        menu_account(file_name)
    else:
        print("\nYou have successfully logged in!")
        menu_card(file_name, card)


def add_income(file_name, card):
    income = int(input("\nEnter income:\n> "))
    add_database_balance(file_name, card[1], income)
    print("Income was added!")


def check_number_card(file_name, num_transfer):
    if not is_check_card_number(num_transfer):
        print("Probably you made mistake in the card number.\n"
              "Please try again!")
        return False
    account = select_database_card_number(file_name, num_transfer)
    if not account:
        print("Such a card does not exist.\n")
        return False
    return True


def do_transfer(file_name, card, num_transfer):
    money = int(input("Enter how much money you want to transfer:\n> "))
    card = select_database_card_number(file_name, card[1])
    if money > card[3]:
        print("Not enough money!\n")
    else:
        update_database_transfer(file_name, card[1], num_transfer, money)
        # add_database_balance(file_name, num_transfer, money)


def close_account(file_name, card):
    conn = sqlite3.connect(file_name)
    cur = conn.cursor()
    account = [card[1]]
    cur.execute("DELETE FROM card WHERE number = ?", account)
    conn.commit()
    print("\nThe account has been closed!")
    conn.close()


def menu_card(file_name, card):
    print(MENU_CARD)
    n = input("Your choice: > ")
    if n == "1":
        card = select_database_card_number(file_name, card[1])
        print("\nBalance: {}".format(card[3]))
        menu_card(file_name, card)
    if n == "2":
        add_income(file_name, card)
        menu_card(file_name, card)
    if n == "3":
        num_transfer = input("\nTransfer\nEnter card number:\n> ")
        if check_number_card(file_name, num_transfer):
            do_transfer(file_name, card, num_transfer)
        menu_card(file_name, card)
    if n == "4":
        close_account(file_name, card)
        menu_account(file_name)
    if n == "5":
        print("\nYou have successfully logged out!")
        menu_account(file_name)
    if n == "0":
        print("\nBye!")


def menu_account(file_name):
    print(MENU_PROGRAM)
    choice = input('Your choice: > ')
    if choice == "0":
        print("\nBye!")
    if choice == "1":
        create_account(file_name)
        menu_account(file_name)
    if choice == "2":
        log_into_account(file_name)


def print_database(file_name):
    accounts = select_database(file_name)
    for account in accounts:
        print(account)


def main(file_name):
    create_database(file_name)
    # print_database(file_name)
    menu_account(file_name)


database_card = 'card.s3db'
main(database_card)

# main(database_card)
# print_database(database_card)
# print(is_check_card_number(input()))
# print_database(file_name)  # delete
# drop_database()
# def drop_database():
#     conn = sqlite3.connect('card.s3db')
#     cur = conn.cursor()
#     cur.execute("DROP TABLE card")
#     conn.commit()
