class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your balance is 25000")

    def withdrawl(self,amount):
        new_amount = 50000 - amount
        print("You have Withdrawn Amount "+str(amount) +". Your Remaining Balance is "+ str(new_amount))


def main():
    Card_number = input("Insert your Card Number:- ")
    pin_number  = input("Enter your Pin Number:- ")

    new_user =  Atm(Card_number ,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.Withdrawl")
    activity = int(input("Enter Activity Number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("Enter the Amount:- "))
        new_user.withdrawl(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()