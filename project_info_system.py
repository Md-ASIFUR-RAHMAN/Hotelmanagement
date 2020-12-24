list = []
listt=[]
print("\n")
while True:

    print("1.Add Info")
    print("2.Remove Info")
    print("3.see the list")
    print("4.Exit")

    print("\n")

    INN = int(input("Which platform you want to go :"))

    if INN == 1:
        IN = int(input("How mane name you want to add :"))
        print("\n")

        for i in range(IN):
            Name = input("Enter your name :")
            print("\n")
            ID = int(input("Enter your ID :"))
            print("\n")
            list.append(Name)
            list.append(ID)
            print("Added sucessful ")



    elif INN == 2:
        IN = int(input("How many info you want to remove :"))
        print("\n")

        for i in range(IN):
            Name = input("Enter your name :")
            print("\n")
            ID = int(input("Enter your ID :"))
            print("\n")
            list.remove(Name)
            list.remove(ID)
            print("Remove sucessful ")

    elif INN ==3:
        print(list)

    elif INN==4:
        break
    elif INN == 5:

        IN = int(input("How mane name you want to add :"))
        print("\n")

        for i in range(IN):
            Name = input("Enter  name :")
            print("\n")
            ID = int(input("Enter ID :"))
            print("\n")
            Birth_date = int(input("Enter  Birth_date  :"))
            print("\n")
            #Blood_Group = input("Enter Blood_Group :")
            #print("\n")
            listt.append(Name)
            listt.append(ID)
            listt.append(Birth_date)
            #listt.append(Blood_Group)

            print("Added sucessful ")

    elif INN==6:
        INNN= int(input("birth date :"))
        a=INNN
        b = listt.index(a)
        listt.reverse()

        print(listt)

    #elif INN==7:
        #list1=["ayon","omee","rk","dj"]
        #list1.index("omee")
        #print(list1.index("omee"))



