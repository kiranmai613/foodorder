import json


def main():
    print("Welcome to the restaurant!")
    print("Are you a new or existing user?")
    print("1. Existing user (login)")
    print("2. New user (register)")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        login()
    elif choice == 2:
        register()
    else:
        print("Invalid choice, please try again.")
        main()

def login():
    print("Please select your login type:")
    print("1. Admin login")
    print("2. User login")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        with open("C:\\Users\\KIRANMAYI\\Desktop\\assi6\\hmm.py\\z.py\\data.json", 'r') as f:
            data = json.load(f)
        if username in data and data[username]["password"] == password:
            print("Login successful.")
            access_foodfunctions()
        else:
            print("Invalid credentials, please try again.")
            login()

    elif choice == 2:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        with open("C:\\Users\\KIRANMAYI\\Desktop\\assi6\\hmm.py\\z.py\\data.json", 'r') as f:
            data = json.load(f)
        if username in data and data[username]["password"] == password:
            print("Login successful.")
            access_order()
        else:
            print("Invalid credentials, please try again.")
            login()

    

def register():
    print("Please select your registration type:")
    print("1. Admin registration")
    print("2. User registration")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        username = input("Enter your username: ")
        phone = input("Enter your phone number: ")
        email = input("Enter your email address: ")
        address = input("Enter your address: ")
        password = input("Enter your password: ")

        with open("C:\\Users\\KIRANMAYI\\Desktop\\assi6\\hmm.py\\z.py\\data.json", 'r') as f:
            data = json.load(f)
        data[username] = {
            "phone": phone,
            "email": email,
            "address": address,
            "password": password
        }
        with open("C:\\Users\\KIRANMAYI\\Desktop\\assi6\\hmm.py\\z.py\\data.json", 'w') as f:
            json.dump(data, f)
        print("Registration successful.")

    elif choice == 2:
        username = input("Enter your username: ")
        phone = input("Enter your phone number: ")
        email = input("Enter your email address: ")
        address = input("Enter your address: ")
        password = input("Enter your password: ")

        with open("C:\\Users\\KIRANMAYI\\Desktop\\assi6\\hmm.py\\z.py\\data.json", 'r') as f:
            data = json.load(f)
        data[username] = {
            "phone": phone,
            "email": email,
            "address": address,
            "password": password
        }
        with open("C:\\Users\\KIRANMAYI\\Desktop\\assi6\\hmm.py\\z.py\\data.json", 'w') as f:
            json.dump(data, f)
        print("Registration successful.")

    else:
        print("Invalid choice, please try again.")
        register()



def access_foodfunctions():
    print("Welcome to food functions!")
    print("1. Add food items")
    print("2. Edit food items")
    print("3. View food items")
    print("4. Remove food items")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_fooditems()
    elif choice == 2:
        edit_fooditems()
    elif choice == 3:
        view_fooditems()
    elif choice == 4:
        remove_fooditems()
    else:
        print("Invalid choice, please try again.")
        





def add_fooditems():
    print("Add new food item:")
    name = input("Enter food name: ")
    quantity = input("Enter quantity (e.g. 100ml, 250gm, 4 pieces): ")
    price = input("Enter price: ")
    discount = input("Enter discount: ")
    stock = input("Enter stock: ")

    with open("C:\\Users\\KIRANMAYI\\Desktop\\assi6\\hmm.py\\z.py\\data.json", 'r') as f:
        data = json.load(f)

    # Generate FoodID automatically
    food_id = len(data) + 1

    data[food_id] = {
        "FoodID": food_id,
        "Name": name,
        "Quantity": quantity,
        "Price": price,
        "Discount": discount,
        "Stock": stock
     }

    with open("C:\\Users\\KIRANMAYI\\Desktop\\assi6\\hmm.py\\z.py\\data.json", 'w') as f:
        json.dump(data, f)

    


    




def edit_fooditems():
    print("Edit existing food item:")
    food_id = int(input("Enter food item ID: "))
    with open("C:\\Users\\KIRANMAYI\\Desktop\\assi6\\hmm.py\\z.py\\data.json", 'r') as f:
        data = json.load(f)
    for item in data:
        if item["FoodID"] == food_id:
            item["FoodName"] = input("Enter new food name: ")
            item["FoodPrice"] = float(input("Enter new food price: "))
            break

    with open("C:\\Users\\KIRANMAYI\\Desktop\\assi6\\hmm.py\\z.py\\data.json", 'w') as f:
        json.dump(data, f)

    




def view_fooditems():
    print("List of food items:")
    with open("C:\\Users\\KIRANMAYI\\Desktop\\assi6\\hmm.py\\z.py\\data.json", 'r') as f:
        data = json.load(f)
        for item in data:
            print(f"{item['FoodID']}. {item['Name']} ({item['Quantity']}) [INR {item['Price']}] - Discount: {item['Discount']}, Stock: {item['Stock']}")
    



def remove_fooditems():
    print("Remove food item:")
    food_id = int(input("Enter food item ID: "))

    with open("C:\\Users\\KIRANMAYI\\Desktop\\assi6\\hmm.py\\z.py\\data.json", 'r') as f:
        data = json.load(f)

    food_item = None
    for item in data:
        if item["FoodID"] == food_id:
            food_item = item
            break

    if food_item:
        data.remove(food_item)
        with open("C:\\Users\\KIRANMAYI\\Desktop\\assi6\\hmm.py\\z.py\\data.json", 'w') as f:
            json.dump(data, f)
        
        print("Food item removed successfully.")
        access_foodfunctions()
    else:
        print("Food item not found, please try again.")
        remove_fooditems()




def access_order():
    
    print("Select an option:")
    print("1. Place new order")
    print("2. Order history")
    print("3. Update profile")
    option = input("Enter option number: ")
                
    if option == '1':
        # Display list of food items
        print("Menu:")
        print("1. Tandoori Chicken (4 pieces) [INR 240]")
        print("2. Vegan Burger (1 Piece) [INR 320]")
        print("3. Truffle Cake (500gm) [INR 900]")
                    
        # Prompt user to select items
        item_numbers = input("Enter array of item numbers: ")
        item_numbers = [int(n) for n in item_numbers]
        items = []
        for n in item_numbers:
            if n == 1:
                items.append("Tandoori Chicken (4 pieces)")
            elif n == 2:
                items.append("Vegan Burger (1 Piece)")
            elif n == 3:
                items.append("Truffle Cake (500gm)")
                    
        # Display selected items to the user
        print("Selected items:")
        for item in items:
            print("- " + item)
                    
        # Prompt user to place order
        place_order = input("Place order? (y/n) ")
        if place_order == 'y':
            print("Order placed successfully")
                    
    elif option == '2':
        # Display order history
        with open("C:\\Users\\KIRANMAYI\\Desktop\\assi6\\hmm.py\\z.py\\data.json", 'r') as f:
            data = json.load(f)
        if 'order_history' in data[0]:
            print("Order history:")
            for order in data[0]['order_history']:
                print("- " + order)
        else:
            print("No order history")
                    
    elif option == '3':
        # Update user profile
        with open("C:\\Users\\KIRANMAYI\\Desktop\\assi6\\hmm.py\\z.py\\data.json", 'r') as f:
            data = json.load(f)
        print("Current profile:")
        print("- User name: " + data[0]['user_name'])
        print("- Password: " + data[0]['password'])
        print("- Email: " + data[0]['email'])
        new_user_name = input("Enter new user name (leave blank to keep current value): ")
        if new_user_name:
            data[0]['user_name'] = new_user_name
        new_password = input("Enter new password (leave blank to keep current value): ")
        if new_password:
            data[0]['password'] = new_password
        new_email = input("Enter new email (leave blank to keep current value): ")
        if new_email:
            data[0]['email'] = new_email
        # Save updated user data to JSON file
        with open("C:\\Users\\KIRANMAYI\\Desktop\\assi6\\hmm.py\\z.py\\data.json", 'w') as f:
            json.dump(data, f)
        print("Profile updated successfully")
                
    else:
        print("Invalid option, please try again")


    
main()

register()
login()


add_fooditems()
edit_fooditems()
remove_fooditems()



