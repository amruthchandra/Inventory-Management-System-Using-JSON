import json

with open("data.json") as f:
    data = json.load(f)
# print(data)

# purchase
while(1):
    print()
    print('///////////////////')
    print("menu")
    print("select option")
    print("1.Purchase an Item from Inventory Management System")
    print("2.Add Product to the Inventory Management System")
    print("3.Check Quantity/Stock")
    print("4.Updating quantity and price")
    print("5.Reading the data from Inventory Management System")
    print("6.Exit")
    n = int(input())
    l = data['category']

    if(n == 1):
        c = 0
        for y in l.keys():
            c += 1
            print(str(c)+'.'+y)

        print("Select Category")
        cat = int(input())
        cat_st = list(l.keys())[cat-1]
        print("select the product")
        c = 0

        for y in l[cat_st]:
            c += 1
            print(str(c)+'.'+y)

        pro = int(input())
        pro_st = list(l[cat_st].keys())[pro-1]
        print("enter the quantity required")
        u_req = int(input())
        l_qut = l[cat_st][pro_st]["quantity"]
        l_pri = l[cat_st][pro_st]["price"]
        if u_req > l_qut:
            print("Item Required Out of Range")
        else:
            d = print()
            l[cat_st][pro_st]["quantity"] = (l_qut-u_req)
            print("billing amount is ", u_req*l_pri)
    elif(n == 2):

        print("Select Category in which you want to add")

        c = 0
        for y in l.keys():
            c += 1
            print(str(c)+'.'+y)

        cat = int(input())
        cat_st = list(l.keys())[cat-1]

        print("Enter the name of the product")
        c = 0
        name = input()
        print("Enter the price of the product")
        price = int(input())
        print("Enter the quantity")
        quant = input()
        print("Enter the arrived date")
        date = input()
        try:
            l[cat_st][name] = {"quantity": quant,
                               "price": price, "arrived_date": date}
            print("Successfully Added")
        except:
            print("OOps there was a error")

    elif(n == 3):

        c = 0
        for y in l.keys():
            c += 1
            print(str(c)+'.'+y)

        print("Select Category in which you want to check")
        cat = int(input())
        cat_st = list(l.keys())[cat-1]
        print("select the product")
        c = 0

        for y in l[cat_st]:
            c += 1
            print(str(c)+'.'+y)

        pro = int(input())
        pro_st = list(l[cat_st].keys())[pro-1]

        l_qut = l[cat_st][pro_st]["quantity"]
        l_pri = l[cat_st][pro_st]["price"]
        print("Quantity of the product available is ", l_qut)
        print("Price of the product is ", l_pri)
    elif(n == 4):
        c = 0
        for y in l.keys():
            c += 1
            print(str(c)+'.'+y)

        print("Select Category")
        cat = int(input())
        cat_st = list(l.keys())[cat-1]
        print("select the product")
        c = 0

        for y in l[cat_st]:
            c += 1
            print(str(c)+'.'+y)

        pro = int(input())
        pro_st = list(l[cat_st].keys())[pro-1]
        print("enter the quantity need to Modified (Previous is)",
              l[cat_st][pro_st]["quantity"],)
        new_qut = int(input())
        print("enter the price need to Modified (Previous is)",
              l[cat_st][pro_st]["price"])
        new_price = int(input())
        try:
            l[cat_st][pro_st]["quantity"] = new_qut
            l[cat_st][pro_st]["price"] = new_price
        except:
            print("OOPS something Went wrong try AGain")
    elif(n == 5):
        print("Categories Present in Inventory Management System")
        for y in l.keys():
            print(y)
            print("     Products in Category", y)
            for z in l[y].keys():
                print("         "+z)
    elif(n == 6):
        print("Thanking for Using Inventory Management System")
        print("Your Data is Saved By JSON... Have A Nice Day :)")
        break
    with open("data.json", 'w') as f:
        json.dump(data, f, indent=2)
