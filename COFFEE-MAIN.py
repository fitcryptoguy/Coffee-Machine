from Menu import resources
from Menu import MENU

profit = 0
total = 0
order = None


def process_coins():
    print(MENU[cofee_choice]["cost"])
    print("Please insert coins.")
    quarter = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.1
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    global total
    total = (quarter + dimes + nickles + pennies)
    return total


def order_successful():

    if total >= MENU[cofee_choice]["cost"]:
        refund = total - MENU[cofee_choice]["cost"]
        print("Coins accepted")
        print(f"Here is your refund {refund}")
        print(f"Here is your {cofee_choice}")
        global order
        order = True
        return order
    else:
        print("Not enough coins")
        return False

    global profit
    price = profit + coffe_cost



# *********************************************************************************************************************************************************


while True:

    cofee_choice = input("wat do you like sir? espresso/latte/cappuccino:  ")

    if cofee_choice == "report":
        for item, value in resources.items():
            print(f"{item}, {value}")

    elif cofee_choice == "off":
        break

    else:
        process_coins()
        order_successful()

