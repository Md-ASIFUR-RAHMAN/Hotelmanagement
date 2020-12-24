def ASIFUR_insertion(ar):
    for i in range( 1 , len(ASIFUR_C)):
        temp = ASIFUR_C[i]
        j = i-1
        while(temp > ASIFUR_C[j] and j>=0):
            ASIFUR_C[j+1] = ASIFUR_C[j]
            j=j-1
        ASIFUR_C[j+1] = temp
    return ar

def ASIFUR_binary_search(ar,data):
    l=0
    r=len(ASIFUR_C)-1
    while(l<=r):
        mid = (l+r)//2
        if ASIFUR_C[mid]==data:
            print("Data Found ")
            break
        elif ASIFUR_C[mid]>data:
            r=mid-1
        elif ASIFUR_C[mid]<data:

            l=mid+1

    return ar

ASIFUR_a = [5,4,3,1,10]
ASIFUR_B = [15,5,3,5,20]
ASIFUR_C= ASIFUR_a + ASIFUR_B

print(ASIFUR_C)
print(ASIFUR_insertion(ASIFUR_C))

data = int(input("Enter Number :"))
print(ASIFUR_insertion(ASIFUR_C))
ASIFUR_binary_search(ASIFUR_C,data)
print( "Data found " + str(ASIFUR_C.count(data))+" times " )
