from resource import MENU, resources

MONEY = 0

def check_resources(coffee):
    ingredients = MENU[coffee]['ingredients']
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True

def process_coins():
    print("Please insert coins. ")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    money_received = 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies
    return money_received

def check_transaction(money_received, cost):
    if money_received >= cost:
        change = round((money_received - cost), 2)
        print(f"Here is ${change} dollars in change.")
        global MONEY
        MONEY += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(coffee):
    for item in resources:
        resources[item] = resources[item] - MENU[coffee]['ingredients'][item]
        return resources[item]


machine_on = True

while machine_on:
    coffee = input("What would you like? (espresso/latte/cappuccino): ")

    if coffee == "off":
        machine_on = False
    elif coffee == "report":
        print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${MONEY}")
    else:
        if check_resources(coffee):
            payment = process_coins()
            if check_transaction(payment, MENU[coffee]["cost"]):
                make_coffee(coffee)
                print(f"Here is your {coffee}☕. Enjoy!")





