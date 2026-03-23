# daily_expense_tracker.py
# ZenfuraVision Daily Expense Tracker
# Tracks daily income and expenses, validates amounts,
# and prints a full financial report with spending summary.
# Concepts: functions, return values, try/except,
#           while loops, string building, type conversion
# Author: Terry Juwah

import sys

def get_info():
    name = input('Enter Your Name: ')
    try:
        balance = int(input('How much was the budget for today: '))
    except ValueError:
        print('Enter a number only. Try again.')
        return get_info()
    return name, balance

def get_expense():
    item = input('What are you spending on: ')
    try:
        price = int(input('How much: '))
    except ValueError:
        print('Enter a number only. Try again.')
        return get_expense()
    return item, price

def validate(price, balance):
    if price <= 0:
        return False
    if price > balance:
        return False
    return True

def print_report(name, income, spent, balance, expense_log):
    print('=' * 30)
    print('DAILY EXPENSE REPORT'.center(30))
    print('=' * 30)
    print(' ')
    print('Name:    ' + name)
    print('Budget:  ₦' + str(income))
    print(' ')
    print('-' * 30)
    print('Expenses:')
    print(' ')
    print(expense_log)
    print('-' * 30)
    print(' ')
    print('Total Spent:  ₦' + str(spent))
    print('Remaining:    ₦' + str(balance))
    print('=' * 30)

name, balance = get_info()
income = balance
spent = 0
expense_log = ''

while True:
    item = input("What did you buy? (type 'done' to finish): ")
    if item.lower() == 'done':
        break
    try:
        price = int(input('How much: '))
    except ValueError:
        print('Numbers only.')
        continue
    if validate(price, balance) == False:
        print('Invalid amount.')
        continue
    balance = balance - price
    spent = spent + price
    expense_log = expense_log + item + ': ₦' + str(price) + '\n'
    print('Remaining: ₦' + str(balance))

print_report(name, income, spent, balance, expense_log)
