
listt=[]

print("\n")
print("1.ROAST                   price 70/=")
print("2.POLAO                   price 50/=")
print("3.EGG                     price 15/=")
print("4.BEAF BIRIYANI           price 350/=")
print("5.CHICKEN BIRIYANI        price 250/=")

print("\n")



while True:
    ran = int(input("How Many item do you want :"))
    print("\n")
    for i in range(ran):
        inn = int(input("Which one do you want ? :"))
        print("\n")
        if inn == 1:
            inpu1 = int(input("How Many Roast you want ? :"))
            Roast = inpu1 * 70
            listt.append(Roast)

        elif inn == 2:
            inpu2 = int(input("How Many plate polao you want ? :"))
            polao = inpu2 * 50
            listt.append(polao)

        elif inn == 3:
            inpu3 = int(input("How Many Egg  you want ? :"))
            Egg = inpu3 * 15
            listt.append(Egg)


        elif inn == 4:
            inpu4 = int(input("How Many plate Beaf_Biriyani  you want ? :"))
            Beaf_Biriyani = inpu4 * 350
            listt.append(Beaf_Biriyani)


        elif inn == 5:
            inpu5 = int(input("How Many plate Chicken_Biriyani you want ? :"))
            Chicken_Biriyani = inpu5 * 250
            listt.append(Chicken_Biriyani)
    print("\n")

    print("Total list :",listt)
    print("\n")

    print("Your TotaL bill :", sum(listt))
    break
