balance = 50000
trial = 0
correct_pin = '2210'

print('=' * 30)
print('ZENFURA BANKING'.center(30))
print('WELCOME'.center(30))
print('=' * 30)

while trial < 3:
    pin = input('Enter your 4 digit pin: ')
    print()

    if pin == correct_pin:
        print('Welcome Mr Terry')
        print()

        while True:
            print('1. Check Balance')
            print('2. Deposit')
            print('3. Withdraw')
            print('4. Exit')
            print()

            option = int(input('What would you like to do: '))

            if option == 1:
                print('Your account balance is: ' + str(balance))
                print()

            elif option == 2:
                deposit = int(input('How much would you like to deposit: '))
                if deposit <= 0:
                    print('Deposit must be greater than zero.')
                    continue
                balance = balance + deposit
                print('Your new balance is: ' + str(balance))
                print()

            elif option == 3:
                withdrawal = int(input('How much would you like to withdraw: '))
                if withdrawal <= 0:
                    print('Withdrawal must be greater than zero.')
                    continue
                elif withdrawal > balance:
                    print('Insufficient funds.')
                    print('Your balance is: ' + str(balance))
                    continue
                balance = balance - withdrawal
                print('Your new balance is: ' + str(balance))
                print()

            elif option == 4:
                print('Goodbye. Thank you for banking with Zenfura.')
                break

            else:
                print('Please enter a value between 1 and 4.')

        break

    else:
        trial += 1
        print(f'Incorrect PIN. Attempts left: {3 - trial}')

if trial == 3:
    print('Your account is restricted. Too many incorrect PIN attempts.')

