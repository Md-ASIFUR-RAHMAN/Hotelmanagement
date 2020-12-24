def ASIFUR_insertion(ar):
    for i in range( 1 , len(ASIFUR_name)):
        temp = ASIFUR_name[i]
        j = i-1
        while(temp < ASIFUR_name[j] and j>=0):
            ASIFUR_name[j+1] = ASIFUR_name[j]
            j=j-1
        ASIFUR_name[j+1] = temp
    return ar

def duplicate(data,a):
    if a>0:
        ASIFUR_name.remove(data)


ASIFUR_name = ["rakibul","rehan","punnota","halima","ayon","omee","ayon"]
print(ASIFUR_insertion(ASIFUR_name))

data = input("Enter name :")
a = ASIFUR_name.count(data)

duplicate(data,a)
print(ASIFUR_name.count(data))
print(ASIFUR_insertion(ASIFUR_name))
