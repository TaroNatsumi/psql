from datetime import datetime
from medical_product import add_new_med_product, edit_med_product, show_med_product, delete_product
from customer_system import show_med_product, buy

while True:

    
    print("Exit/Admin/Customer(0/1/2)")
    options = input("Options: ")

    if options == "0":
        break
    elif options == "1":
        while True:
            print("Exit/Show/Add New/Edit(0/1/2/3)")
            options = input("Options: ")
            if options == "0":
                break
            elif options == "1":
                show_med_product()
            elif options == "2":
                show_med_product()
                name = input("Product name: ").capitalize()
                count = int(input("Count: "))
                price = float(input("Price: "))
                time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                add_new_med_product(name, count, price, time)
            elif options == "3":
                show_med_product()
                print("Exit/Up Data/ Delete(0/1/2)")
                options = input("Options: ")
                if options == "0":
                    break
                elif options == "1":
                    name = input("Name: ").capitalize()
                    count = int(input("Count: "))
                    price = float(input("Price: "))
                    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    edit_med_product(name, count, price, time)
                elif options == "2":
                    name = input("Name: ")
                    delete_product(name)
    elif options == "2":
        while True:
            first_name = input("First name: ").capitalize()
            second_name = input("Second name: ").capitalize()
            while True:
                print("Exit/Show/Buy(0/1/2)")
                options = input("Options: ")
                if options == "0":
                    break
                elif options == "1":
                    show_med_product()
                elif options == "2":
                    show_med_product()
                    product_name = input("Product name: ").capitalize()
                    count = int(input("Count: "))
                    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    buy(first_name, second_name, product_name, count, time)
                else:
                    print("Wrong choose")
            break
