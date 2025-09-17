burgerMenu = {
    "Smoky Volcano Burger": [10.99, "A fiery blend of smoked beef, chipotle aioli, pepper jack cheese, and jalapeños."],
    "Jalapeño Jackpot": [9.99,"Loaded with fresh jalapeños, spicy mayo, and a kick of habanero cheese."],
    "Ghost Pepper Slammer": [11.75, "Spicy ghost pepper sauce, pepper jack cheese, and crispy fried jalapeños."]
    }
sideMenu = {
    "Coleslaw": 4.99,
    "Fries": 5.25,
    "Mashed Potato": 3.99,
}
while True:
    total = 0
    print("🍔✨ Welcome to Burger Bliss! ✨🍔")
    print("---------------------------------")
    print("1️⃣  Buy a Hamburger 🍔")
    print("2️⃣  Show a New Hamburger 🆕")
    print("3️⃣  Buy a Side Dish 🍟")
    print("4️⃣  Total and Payment 💳")
    print("5️⃣  Exit ❌")
    selection = input("What would you like to do? ")
    if selection == "1":
        print("1. Smoky Volcano Burger - $10.99 ")
        print("2. Jalapeño Jackpot - $9.99 ")
        print("3. Ghost Pepper Slammer - $11.75 ")
        burgerChoice = input("What would you like to do? ")
        if burgerChoice == "1":
            quanity = int(input("How many burgers would you like? "))
            price = burgerMenu["Smoky Volcano Burger"] [0] * quanity
            total += price
            print(total)
        elif burgerChoice == "2":
            quanity = int(input("How many burgers would you like? "))
            price = burgerMenu["Jalapeño Jackpot"] [0] * quanity
            total += price
            print(total)
        elif burgerChoice == "3":
            quanity = int(input("How many burgers would you like? "))
            price = burgerMenu["Ghost Pepper Slammer"] [0] * quanity
            total += price
            print(total)
        else:
            print("This burger doesn't exist.")
    elif selection == "2":
        print("🔥 Limited-Time Burger Promo! 🔥")
        print(" The Lava Crunch Burger – Only $8.99!")
        print("Description:")
        print("Turn up the heat with our brand-new Lava Crunch Burger – a sizzling combo of spicy beef, crunchy jalapeño chips, melted pepper jack cheese, and a splash of our signature volcano sauce, all stacked on a toasted brioche bun. 🌶️🔥")
        print("Regular Price: $11.25 – Now Only $8.99 for a limited time! 💥")
        print("🎁 Comes with a free soft drink if you order before 5 PM! 🥤")
    elif selection == "3":
        print("1. Fries - $5 ")
        print("2. Mashed Potato - $10 ")
        print("3. Coleslaw - $15 ")
        sideChoice = input("What would you like to do? ")
        if sideChoice == "1":
            quanity = int(input("How many burgers would you like? "))
            price = sideMenu["Fries"] * quanity
            total += price
            print(total)
        elif sideChoice == "2":
            quanity = int(input("How many burgers would you like? "))
            price = sideMenu["Mashed Potato"]* quanity
            total += price
            print(total)
        elif sideChoice == "3":
            quanity = int(input("How many burgers would you like? "))
            price = sideMenu["Coleslaw"] * quanity
            total += price
            print(total)
        else:
            print("This burger doesn't exist.")
    elif selection == "4":
        print(f"${total} is your total")
        print("Thank you for shopping with Burger Bliss.")
    elif selection == "5":
        break
    print("---------------------------------")