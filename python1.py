import random

balance = 1000

def game():
     global balance
     while True:
        bet = int(input('Enter a bet: '))
        if bet > balance:
            print('Bet is greater than balance')
        else:
            a = int(input('Enter a: '))
            b = int(input('Enter b: '))
            if a > 99 or a < 1 or b > 99 or b < 1:
                print('Invalid input, enter numbers in range 1 - 99')
                continue 
            random1 = random.randint(1, 99)
            random2 = random.randint(1, 99)
            print(f'Your numbers: {a}, {b}\nComputer numbers: {random1}, {random2}')

            if random1 == a or random2 == a or random1 == b or random2 == b:
                if random1 == a or random2 == a and random1 == b or random2 == b:
                    balance += bet * 2
                    print(f'Your balance is {balance}')
                else:
                    print(f'Your balance is {balance}')

            else:
                balance -= bet
                print(f'Your balance is {balance}')

            if balance <= 0:
                print('Your balance is zero or negative')
                break 

            again = input('Do you want to continue? (y/n): ').lower()
            if again != 'y':
                break
game()