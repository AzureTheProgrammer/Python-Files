# UPDATE 1.8 # 

"""
TO DO LIST:
Fixing Advertisements (accepting advertisements)
"""

import random, time, math, os
from termcolor import cprint
from colorama import *

init()
os.system('clear')

# Unrelated
TimeToWork = 0

Staff_payment = 10 # every staff upgrade level = 10 employees

# levels
money = 5000
gear_upgrade = 1      
security_upgrade = 1  
staff_upgrade = 1     
customers = 10        
employees = 10

# Upgrade Prices
gear_upgrade_price = 250
security_upgrade_price = 500
staff_upgrade_price = 250
advertise_price = 300
paperwork_price = 5

# Move location prices
current_location = ""

Dubai_price = 500
Moscow_price = 700
Chicago_price = 900
London_price = 1100
LA_price = 1300
NY_price = 1500
Tokyo_price = 1700

# List of locations if they choose above 4
start_locations = ["Washington D.C", "Seattle", "San Francisco"]

print(Fore.GREEN + """ 
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$            
     ____              _    _                 _____ _           
    |  _ \            | |  (_)               / ____(_)          
    | |_) | __ _ _ __ | | ___ _ __   __ _   | (___  _ _ __ ___  
    |  _ < / _` | '_ \| |/ / | '_ \ / _` |   \___ \| | '_ ` _ \ 
    | |_) | (_| | | | |   <| | | | | (_| |   ____) | | | | | | |
    |____/ \__,_|_| |_|_|\_\_|_| |_|\__, |  |_____/|_|_| |_| |_| 
                                     __/ |                     
                                    |___/   
                                
   A virtual bank that you can go to work, go home, and go bankrupt.
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

Loading...
""" + Fore.RESET)

time.sleep(3)
print("To start your bank, you persuaded your family and friends to be your customers")
cprint("+10 Customers!", "red")

time.sleep(3)

# START LOCATION
print("Now that you got customers ready, you need to find a location for your bank!")
print("1. Washington D.C")
print("2. Seattle")
print("3. San Francisco")
choice = input(">> ")

if choice == "1":
    print("You set your location as Washington D.C")
    current_location = "Washington D.C"

if choice == "2":
    print("You set your location as Seattle")
    current_location = "Seattle"

if choice == "3":
    print("You set your location as San Francisco")
    current_location = "San Francisco"

if choice >= "4":
    random_location = random.choice(start_locations)
    current_location = random_location
    print("You set your location as: " + random_location)

time.sleep(2)

TypesOfPeople = ["a single mom", "a homeless man", "a war veteran", "a small business owner"]
TypesOfAdvertisement = ["a Radio", "a TV Series", "a Movie Series", "a Social Media Site"]

# THE ACTUAL PROGRAM WHERE STUFF HAPPENS

def GetToWork():
    os.system('clear')
    global money, customers, gear_upgrade, staff_upgrade, security_upgrade, paperwork_price, current_location, gear_upgrade_price, security_upgrade_price, staff_upgrade_price, employees, TimeToWork, Staff_payment

    TimeToWork = TimeToWork + 1

    if money <= 0:
        cprint("GAME OVER!", "red", attrs=["bold", "underline"])     
        print("""
___________________________________
|#######====================#######|
|#(1)*UNITED STATES OF AMERICA*(1)#|
|#**          /===\   ********  **#|
|*# {G}      | (") |             #*|
|#*  ******  | /v\ |    O N E    *#|
|#(1)         \===/            (1)#|
|##=========ONE DOLLAR===========##|
------------------------------------""")
        print("Better luck next time") 
        return
    
    if customers <= 0:
        print(Fore.RED + "GAME OVER!" + Fore.RESET)
        print("Your bank ran out of customers :(")
    
    if money >= 100000:
        cprint("YOU WON! You got your bank to $100,000!", "green", attrs=["bold"])
        print("But however, there is a recession... so bye")
        time.sleep(3)
        for i in range(1, money):
            time.sleep(0.01)
            money = money - 10000
            print("Your Money: " + Fore.GREEN + "$" + str(money) + Fore.RESET)
            os.system('clear')

            if money <= 0:
                cprint("GAME OVER", "red")
                print(Fore.GREEN + """
___________________________________
|#######====================#######|
|#(1)*UNITED STATES OF AMERICA*(1)#|
|#**          /===\   ********  **#|
|*# {G}      | (") |             #*|
|#*  ******  | /v\ |    O N E    *#|
|#(1)         \===/            (1)#|
|##=========ONE DOLLAR===========##|
------------------------------------""" + Fore.RESET)
                print("You won, but also lost")
                return
        
    # printing current stats
    print("Current Stats:")
    print("Your Balance: " + Fore.GREEN + "$" + str(money) + Fore.RESET)
    print("Equipment Level: " + str(gear_upgrade))
    print("Security Level: " + str(security_upgrade))
    print("Staff Level: " + str(staff_upgrade))
    print("Customers: " + str(customers))
    print("Current Location: " + current_location)
    print("")
    print("You arrived at work! What do you do?")
    print("1. Give out loans")
    print("2. Accept advertisements")
    print("3. Do paperwork")
    print("4. Invest")
    print("5. Check Donation Bin")
    print("6. Sabotage Competition")
    print("7. Go Bankrupt (OOF yourself)")
    print("8. Leave work")
    choice = input(">> ")

    # Give out Loans
    if choice == "1":
        os.system('clear')
        wantedLoan = random.randint(100, 1000)

        if money < wantedLoan:
            print("You don't have enough money for this!")
            time.sleep(2)
            GetToWork()

        print("Someone walks in to your bank and asks for a loan of " + Fore.GREEN + "$" + str(wantedLoan) + Fore.RESET)
        print("Do you accept their offer?")
        yn = input("y/n: ")
        if yn == "y":
            chanceOfReturn = random.randint(1, 2)
            money = money - wantedLoan
            print("You have given the loan of " + Fore.RED + "$" + str(wantedLoan) + Fore.RESET)
            print("Only time will tell if you get the money back")
            time.sleep(5)

            # Get your money back (Successful Loan)
            if chanceOfReturn == 1:
                print("You were able to get your money back! And got paid for work!")
                PaidForWork = random.randint(25, 50)
                total = wantedLoan + PaidForWork
                print("You just got a total of: " + Fore.GREEN + "$" + str(total) + Fore.RESET)
                oney = money + total
                print("Your total balance is: " + Fore.GREEN + "$" + str(money) + Fore.RESET)
                time.sleep(4)
                GetToWork()
            
            # No money back
            if chanceOfReturn == 2:
                print("You were unable to make any money back.")
                print("You lost: " + Fore.RED + "$" + str(wantedLoan) + Fore.RESET)
                time.sleep(3)
                GetToWork()
        
        if yn == "n":
            print("Alright then, no loans at this time!")
            time.sleep(1)
            GetToWork()

    # Accept Advertisements 
    if choice == "2":
        TypesOfAdvertisement_chosen = random.choice(TypesOfAdvertisement)
        Chosen_price = random.randint(50, 100)
        print("A company has decided to use you as an advertiser!")
        print("The company that wants you to advertise is: " + TypesOfAdvertisement_chosen)
        print("They want to pay you: " + Fore.GREEN + "$" + str(Chosen_price) + Fore.RESET)
        print("Do you accept this offer?")

        yn = input("y/n: ")
        if yn == "y":
            print("You just accepted the offer and got $" + Fore.GREEN + "$" + str(Chosen_price) + Fore.RESET)
            money = money + Chosen_price
            print("Your balance is now: " + Fore.GREEN + "$" + str(money) + Fore.RESET)
            time.sleep(2)
            os.system('clear')
            GetToWork()
        
        if yn == "n":
            print("You refused the offer, and didn't make any money.")
            time.sleep(2)
            GetToWork()

    # Do paperwork
    if choice == "3":
        level = gear_upgrade
        print("Doing paperwork...")
        time.sleep(3)
        paperwork_price = paperwork_price + level
        money = money + paperwork_price
        print("You have earned " + Fore.GREEN + "$" + str(paperwork_price) + Fore.RESET)
        print("Your Balance is now: " + Fore.GREEN + "$" + str(money) + Fore.RESET)
        time.sleep(3)
        GetToWork()

    # invest
    if choice == "4":
        bankInvestment = random.randint(50, 500)
        chanceOfSuccess = random.randint(1, 2)

        # 1 = Successful Investment
        # 2 = Failed Investment

        print("A company has requested that you invest in their company.")
        print("You will give them: " + Fore.GREEN + "$" + str(bankInvestment) + Fore.RESET)
        print("Do you accept?")
        yn = input("y/n: ")

        if yn == "y":
            os.system('clear')
            print("You have given out the loan of " + Fore.GREEN + "$" + str(bankInvestment) + Fore.RESET + " Only time will tell if this was good or not!")
            time.sleep(3)

            # Successful Investment
            if chanceOfSuccess == 1:
                print("You made a successful investment! And you earned x2 your money!")
                investment = bankInvestment * 2
                money = money + investment
                cprint("You earned: " + Fore.GREEN + "$" + str(investment) + Fore.RESET)
                print("Your balance is now: " + Fore.GREEN + "$" + str(money) + Fore.RESET)
                time.sleep(4)
                GetToWork()
            
            # Failed Investment
            if chanceOfSuccess == 2:
                money = money - bankInvestment
                print("The business you invested in failed!")
                print("You did not make any money back!")
                print("You wasted: " + Fore.RED + "$" + str(bankInvestment) + Fore.RESET)
                print("Your balance is now: " + Fore.GREEN + "$" + str(money) + Fore.RESET)
                time.sleep(4)
                GetToWork()

        if yn == "n":
            os.system('clear')
            print("You refused to invest in the business!")
            print("Maybe you would've made more money.")
            time.sleep(3)
            GetToWork()
            
    # Check donation bin
    if choice == "5":
        amount = random.randint(10, 15)
        donation = amount * staff_upgrade + TimeToWork
        print("You look into the recycle bin")
        print("There is a total of: " + Fore.GREEN + "$" + str(donation) + Fore.RESET)
        money = money + donation
        print("Your Balance is now: " + Fore.GREEN + "$" + str(money) + Fore.RESET)
        time.sleep(2)
        Menu()

    # Sabotage Competition
    if choice == "6":
        print("You leave the bank to try and sabotage other bank's advertisements!")
        time.sleep(2)
        print("You were able to take down some of their posters!")
        print("Some customers may not like this though!")
        time.sleep(2)
        customersLost = random.randint(1, 50)
        customersGained = random.randint(1, 50)
        os.system('clear')
        print(Fore.RED + "You lost: " + str(customersLost) + " customers" + Fore.RESET)
        print(Fore.GREEN + "But you also gained: " + str(customersGained) + " customers" + Fore.RESET)
        customers = customers - customersLost
        customers = customers + customersGained

        if customersGained > customersLost:
            difference = customersGained - customersLost
            print(Fore.GREEN + "You now have made " + str(difference) + " new customers!")
            time.sleep(2)

        if customersLost > customersGained:
            difference = customersLost - customersGained
            print("You were unable to make any new customers!")
            print(Fore.RED + "You were able to get: " + str(difference) + " customers!" +  Fore.RESET)
            time.sleep(2)

        print("Current Customers: " + str(customers))
        time.sleep(5)
        GetToWork()

    # Give up
    if choice == "7":
        print("Are you sure you'd like to go bankrupt?")
        yn = input("y/n: ")

        if yn == "y":
            os.system('clear')
            print(Fore.RED + "GAME OVER!" + Fore.RESET)
            print("You've just gone bankrupt... i can't tell if this was dumb or smart.")
            print(Fore.RED + "Your Balance: $" + "-100000" + Fore.RESET)
            return


    # Leave work
    if choice == "8":
        os.system('clear')
        print("Exiting work and going home...")
        time.sleep(3)
        Menu()

################################### MAIN MENU ##################################

def Menu():
    os.system('clear')
    global money, customers, gear_upgrade, staff_upgrade, security_upgrade, paperwork_price, current_location, gear_upgrade_price, security_upgrade_price, staff_upgrade_price, employees, Staff_payment

    if money <= 0:
        cprint("GAME OVER!", "red", attrs=["bold", "underline"])
        print(Fore.GREEN + """
___________________________________
|#######====================#######|
|#(1)*UNITED STATES OF AMERICA*(1)#|
|#**          /===\   ********  **#|
|*# {G}      | (") |             #*|
|#*  ******  | /v\ |    O N E    *#|
|#(1)         \===/            (1)#|
|##=========ONE DOLLAR===========##|
------------------------------------

You won, but also lost. Better luck next time.""" + Fore.RESET)
        return

    if customers <= 0:
        print(Fore.RED + "GAME OVER!" + Fore.RESET)
        print("Your bank ran out of customers :(")
    
    if money >= 100000:
        cprint("YOU WON! You got your bank to $100,000", "green", attrs=["bold"])
        print("But however, there is a recession... so bye")
        time.sleep(4)
        for i in range(1, money):
            time.sleep(0.01)
            money = money - 1000
            cprint("Money: " + Fore.GREEN + "$" + str(money) + Fore.RESET)
            os.system('clear')
       
            if money <= 0:
                cprint("GAME OVER", "red")
                print(Fore.GREEN + """
___________________________________
|#######====================#######|
|#(1)*UNITED STATES OF AMERICA*(1)#|
|#**          /===\   ********  **#|
|*# {G}      | (") |             #*|
|#*  ******  | /v\ |    O N E    *#|
|#(1)         \===/            (1)#|
|##=========ONE DOLLAR===========##|
------------------------------------""" + Fore.RESET)
                return

    print("Current Balance: " + Fore.GREEN + "$" + str(money) + Fore.RESET)
    print("Current Customers: " + str(customers))
    print("Current Location: " + current_location)
    print("Current Employees: " + str(employees))
    print("")
    print("Here is the main menu! What do you want to do?")
    print("1. Upgrade Your Equipment (" + Fore.GREEN + "$" + str(gear_upgrade_price) + Fore.RESET + ") " + str(gear_upgrade) + "/5")
    print("2. Upgrade Your Security (" + Fore.GREEN + "$" + str(security_upgrade_price) + Fore.RESET + ") " + str(security_upgrade) + "/5")
    print("3. Upgrade Your Staff (" + Fore.GREEN + "$" + str(staff_upgrade_price) + Fore.RESET + ") " + str(staff_upgrade) + "/5")
    print("4. Advertise (" + Fore.GREEN + "$" + str(advertise_price) + Fore.RESET + ")")
    print("5. Move location")
    print("6. Go To Work")

    choice = input(">> ")

    # Equipment Upgrade
    if choice == "1":
        if money < gear_upgrade_price:
            print("You do not have enough for this upgrade!")
            time.sleep(3)
            os.system('clear')
            Menu()
        
        if gear_upgrade == 5:
            print("You can no longer upgrade this!")
            time.sleep(2)
            Menu()
    
        print("Are you sure you would like to upgrade your Equipment for: " + Fore.GREEN + "$" + str(gear_upgrade_price) + Fore.RESET)

        yn = input("y/n: ")
        if yn == "y":
            money = money - gear_upgrade_price
            gear_upgrade = gear_upgrade + 1
            print("Taken away: " + Fore.RED + "$" + str(gear_upgrade_price) + Fore.RESET)
            print("Your balance is now: " + Fore.GREEN + "$" +str(money) + Fore.RESET)
            print("Your Equipment Level is now: " + str(gear_upgrade))
            gear_upgrade_price = gear_upgrade_price + 500
            time.sleep(3)
            os.system('clear')
            Menu()
        if yn == "n":
            os.system('clear')
            Menu()

    # Security Upgrade
    if choice == "2":
        if money < security_upgrade_price:
            print("You do not have enough money for this upgrade!")
            time.sleep(3)
            os.system('clear')
            Menu() 
        
        if security_upgrade == 5:
            print("You can no longer upgrade this!")
            time.sleep(2)
            Menu()
        
        print("Are you sure you would like to upgrade your Security for: " + Fore.GREEN + "$" + str(security_upgrade_price) + Fore.RESET)

        yn = input("y/n: ")
        if yn == "y":
            money = money - security_upgrade_price
            security_upgrade = security_upgrade + 1
            print("Taken away: " + Fore.RED + "$" + str(security_upgrade_price) + Fore.RESET)
            print("Your balance is now: " + Fore.GREEN + "$" + str(money) + Fore.RESET)
            print("Your Security Level is now: " + str(security_upgrade))
            security_upgrade_price = security_upgrade_price + 500
            time.sleep(3)
            os.system('clear')
            Menu()
        
        if yn == "n":
            os.system('clear')
            Menu()

    # Staff Upgrade
    if choice == "3":
        if money < staff_upgrade_price:
            print("You do not have enough money for this upgrade!")
            time.sleep(3)
            os.system('clear')
            Menu()

        if staff_upgrade == 5:
            print("You can no longer upgrade this!")
            time.sleep(2)
            Menu()
        
        print("Are you sure you would like to upgrade your Staff for: " + Fore.GREEN + "$" + str(staff_upgrade_price) + Fore.RESET)
        yn = input("y/n: ")

        if yn == "y":
            money = money - staff_upgrade_price
            employees = employees + 10
            staff_upgrade = staff_upgrade + 1
            print("Taken away: " + Fore.RED + "$" + str(staff_upgrade_price) + Fore.RESET)
            print("Your balance is now: " + Fore.GREEN + "$" + str(money) + Fore.RESET)
            print("Your Staff level is now: " + str(staff_upgrade))
            print("You now have " + str(employees) + " employees")
            staff_upgrade_price = staff_upgrade_price + 250
            time.sleep(3)
            os.system('clear')
            Menu()
        
        if yn == "n":
            Menu()
    
    # Advertise!
    if choice == "4":

        if money < advertise_price:
            print("You do not have enough money for this!")
            time.sleep(2)
            Menu()
        
        # Robberies
        chanceOfRobbery = random.randint(1, 100)
        if security_upgrade == 1:
            if chanceOfRobbery < 50:
                os.system('clear')
                print(Fore.RED + "BEWARE!" + Fore.RESET)
                print("Robbery incoming!")
                print("3...")
                time.sleep(1)
                print("2...")
                time.sleep(1)
                print("1...")
                time.sleep(2)
                robbedMoney =  math.floor(.35 * money)
                print("Robbers got away with: " + Fore.RED + "$" + str(robbedMoney) + Fore.RESET)
                money = money - robbedMoney
                time.sleep(2)
                Menu()

        if security_upgrade == 2:
            if chanceOfRobbery < 40:
                os.system('clear')
                print(Fore.RED + "BEWARE!" + Fore.RESET)
                print("Robbery incoming!")
                print("3...")
                time.sleep(1)
                print("2...")
                time.sleep(1)
                print("1...")
                time.sleep(2)
                robbedMoney =  math.floor(.35 * money)
                print("Robbers got away with: " + Fore.RED + "$" + str(robbedMoney) + Fore.RESET)
                money = money - robbedMoney

                if money <= 0:
                    print(Fore.RED + "GAME OVER!" + Fore.RESET)
                    return

                time.sleep(2)
                Menu()
        
        if security_upgrade == 3:
            if chanceOfRobbery < 30:
                os.system('clear')
                print(Fore.RED + "BEWARE!" + Fore.RESET)
                print("Robbery incoming!")
                print("3...")
                time.sleep(1)
                print("2...")
                time.sleep(1)
                print("1...")
                time.sleep(2)
                robbedMoney =  math.floor(.35 * money)
                print("Robbers got away with: " + Fore.RED + "$" + str(robbedMoney) + Fore.RESET)
                money = money - robbedMoney

                if money <= 0:
                    print(Fore.RED + "GAME OVER!" + Fore.RESET)
                    return

                time.sleep(2)
                Menu()
        
        if security_upgrade == 4:
            if chanceOfRobbery < 20:
                os.system('clear')
                print(Fore.RED + "BEWARE!" + Fore.RESET)
                print("Robbery incoming!")
                print("3...")
                time.sleep(1)
                print("2...")
                time.sleep(1)
                print("1...")
                time.sleep(2)
                robbedMoney =  math.floor(.35 * money)
                print("Robbers got away with: " + Fore.RED + "$" + str(robbedMoney) + Fore.RESET)
                money = money - robbedMoney

                if money <= 0:
                    print(Fore.RED + "GAME OVER!" + Fore.RESET)
                    return

                time.sleep(2)
                Menu()
        
        if security_upgrade == 5:
            if chanceOfRobbery < 10:
                os.system('clear')
                print(Fore.RED + "BEWARE!" + Fore.RESET)
                print("Robbery incoming!")
                print("3...")
                time.sleep(1)
                print("2...")
                time.sleep(1)
                print("1...")
                time.sleep(2)
                robbedMoney =  math.floor(.35 * money)
                print("Robbers got away with: " + Fore.RED + "$" + str(robbedMoney) + Fore.RESET)
                money = money - robbedMoney

                if money <= 0:
                    print(Fore.RED + "GAME OVER!" + Fore.RESET)
                    return

                time.sleep(2)
                Menu()


        money = money - advertise_price
        os.system('clear')
        print("You paid: " + Fore.RED + "$" + str(advertise_price) + Fore.RESET)
        print("Printing Posters...")
        time.sleep(2)
        print("Uploading Website Adverts...")
        time.sleep(1)
        print("Created Billboard")
        print("")
        new_customers = random.randint(10, 30)
        customers = customers + new_customers
        
        print("Well done! You have achieved", new_customers, "new customers!")
        NC_Money = new_customers * 5
        money = money + NC_Money
        print("You earned " + Fore.GREEN + "$" + str(NC_Money) + Fore.RESET + " from new customers signing up!")
        time.sleep(3)
        os.system('clear')
        Menu()

###################### MOVING BANK LOCATIONS ###################################
    if choice == "5":
        os.system('clear')
        print("You have decided to move your bank location to bigger cities for more money! But where do you choose? And what can you afford?")
        print("1. Dubai (" + Fore.GREEN + "$" + str(Dubai_price) + Fore.RESET + ")")
        print("2. Moscow (" + Fore.GREEN + "$" + str(Moscow_price) + Fore.RESET + ")")
        print("3. Chicago (" + Fore.GREEN + "$" + str(Chicago_price) + Fore.RESET + ")")
        print("4. London (" + Fore.GREEN + "$" + str(London_price) + Fore.RESET + ")")
        print("5. Los Angeles (" + Fore.GREEN + "$" + str(LA_price) + Fore.RESET + ")")
        print("6. New York (" + Fore.GREEN + "$" + str(NY_price) + Fore.RESET + ")")
        print("7. Tokyo (" + Fore.GREEN + "$" + str(Tokyo_price) + Fore.RESET + ")")
        print("8. Go back to the Main Menu")
        new_location = input(">> ")

        #Dubai
        if new_location == "1":
            if money < Dubai_price:
                print("You do not have enough money to move here")
                time.sleep(2)
                Menu()
            
            if current_location == "Dubai":
                print("You already are here!")
                time.sleep(1)
                Menu()

            print("Are you sure you would like to move to this location?")
            yn = input("y/n: ")
            
            if yn == "y":
                print("Alright then! You have moved to a new location!")
                current_location = "Dubai"
                money = money - Dubai_price
                print("Taken away: " + Fore.RED + "$" + str(Dubai_price) + Fore.RESET)
                print("Money: " + Fore.GREEN + "$" + str(money) + Fore.RESET)
                print("Customers Gained: +100")
                customers = customers + 100
                time.sleep(4)
                Menu()
            
            if yn == "n":
                print("Alright then! Back to the Main Menu!")
                time.sleep(2)
                Menu()

        #Moscow
        if new_location == "2":
            if money < Moscow_price:
                print("You do not have enough money to move here")
                time.sleep(2)
                Menu()

            if current_location == "Moscow":
                print("You already are here!")
                time.sleep(1)
                Menu()
            
            print("Are you sure you would like to move to this location?")
            yn = input("y/n: ")
            
            if yn == "y":
                print("Alright then! You have moved to a new location!")
                current_location = "Moscow"
                money = money - Moscow_price
                print("Taken away: " + Fore.RED + "$" + str(Moscow_price) + Fore.RESET)
                print("Money: " + Fore.GREEN + "$" + str(money) + Fore.RESET)
                print("Customers Gained: +150")
                customers = customers + 150
                time.sleep(4)
                Menu()
            
            if yn == "n":
                print("Alright then! Back to the Main Menu!")
                time.sleep(2)
                Menu()

        # Chicago
        if new_location == "3":
            if money < Chicago_price:
                print("You do not have enough money to move here")
                time.sleep(2)
                Menu()
            
            if current_location == "Chicago":
                print("You already are here!")
                time.sleep(1)
                Menu()

            print("Are you sure you would like to move to this location?")
            yn = input("y/n: ")
            
            if yn == "y":
                print("Alright then! You have moved to a new location!")
                current_location = "Chicago"
                money = money - Chicago_price
                print("Taken away: " + Fore.RED + "$" + str(Chicago_price) + Fore.RESET)
                print("Money: " + Fore.GREEN + "$" + str(money) + Fore.RESET)
                print("Customers Gained: +200")
                customers = customers + 200
                time.sleep(4)
                Menu()
            
            if yn == "n":
                print("Alright then! Back to the Main Menu!")
                time.sleep(2)
                Menu()
            
        # London
        if new_location == "4":
            if money < London_price:
                print("You do not have enough money to move here")
                time.sleep(2)
                Menu()

            if current_location == "London":
                print("You already are here!")
                time.sleep(1)
                Menu()
            
            print("Are you sure you would like to move to this location?")
            yn = input("y/n: ")
            
            if yn == "y":
                print("Alright then! You have moved to a new location!")
                current_location = "London"
                money = money - London_price
                print("Taken away: " + Fore.RED + "$" + str(London_price) + Fore.RESET)
                print("Money: " + Fore.GREEN + "$" + str(money) + Fore.RESET)
                print("Customers Gained: +250")
                customers = customers + 250
                time.sleep(4)
                Menu()
            
            if yn == "n":
                print("Alright then! Back to the Main Menu!")
                time.sleep(2)
                Menu()

        # Los Angeles
        if new_location == "5":
            if money < LA_price:
                print("You do not have enough money to move here")
                time.sleep(2)
                Menu()
            
            if current_location == "Los Angeles":
                print("You already are here!")
                time.sleep(1)
                Menu()

            print("Are you sure you would like to move to this location?")
            yn = input("y/n: ")
            
            if yn == "y":
                print("Alright then! You have moved to a new location!")
                current_location = "Los Angeles"
                money = money - LA_price
                print("Taken away: " + Fore.RED + "$" + str(LA_price) + Fore.RESET)
                print("Money: " + Fore.GREEN + "$" + str(money) + Fore.RESET)
                print("Customers Gained: +300")
                customers = customers + 300
                time.sleep(4)
                Menu()
            
            if yn == "n":
                print("Alright then! Back to the Main Menu!")
                time.sleep(2)
                Menu()

        # New York
        if new_location == "6":
            if money < NY_price:
                print("You do not have enough money to move here")
                time.sleep(2)
                Menu()
            
            if current_location == "New York":
                print("You already are here!")
                time.sleep(1)
                Menu()

            print("Are you sure you would like to move to this location?")
            yn = input("y/n: ")
            
            if yn == "y":
                print("Alright then! You have moved to a new location!")
                current_location = "New York"
                money = money - NY_price
                print("Taken away: " + Fore.RED + "$" + str(NY_price) + Fore.RESET)
                print("Money: " + Fore.GREEN + "$" + str(money) + Fore.RESET)
                print("Customers Gained: +350")
                customers = customers + 350
                time.sleep(4)
                Menu()
            
            if yn == "n":
                print("Alright then! Back to the Main Menu!")
                time.sleep(2)
                Menu()

        # Tokyo
        if new_location == "7":
            if money < Tokyo_price:
                print("You do not have enough money to move here")
                time.sleep(2)
                Menu()
            
            if current_location == "Tokyo":
                print("You already are here!")
                time.sleep(1)
                Menu()

            print("Are you sure you would like to move to this location?")
            yn = input("y/n: ")
            
            if yn == "y":
                print("Alright then! You have moved to a new location!")
                current_location = "Tokyo"
                money = money - Tokyo_price
                print("Taken away: " + Fore.RED + "$" + str(Tokyo_price) + Fore.RESET)
                print("Money: " + Fore.GREEN + "$" + str(money) + Fore.RESET)
                print("Customers Gained: +400")
                customers = customers + 400
                time.sleep(4)
                Menu()
            
            if yn == "n":
                print("Alright then! Back to the Main Menu!")
                time.sleep(2)
                Menu()

        if new_location == "8":
            print("Going back to the main menu")
            time.sleep(2)
            Menu()
    
    # Going to work
    if choice == "6":
        Staff_payment_amount = Staff_payment * employees

        if money < Staff_payment_amount:
            print("You were unable to pay your staff, so they left the business")
            employees = employees - 10
            staff_upgrade = staff_upgrade - 1

            if employees <= 0:
                print("You ran out of employees")
                print(Fore.RED + "GAME OVER" + Fore.RESET)
                return

        else:
            print("You have paid your employees " + Fore.GREEN + "$" + str(Staff_payment_amount) + Fore.RESET + " for the day")
            money = money - Staff_payment_amount
            print("Driving to work...")
            time.sleep(2)
            GetToWork()
        
Menu()
