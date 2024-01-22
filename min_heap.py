


def swap(var1,var2):
    temp = var1
    var1 = var2
    var2 = temp

def bubbleup(i,var,array1):
    num = (i-1)//2
    if var < array1[num]:
        swap(array1[i], array1[num])
    return num

def heapify(inputarray): 
    array1 = []
    
    for i,var in enumerate(inputarray):
        array1.append(var)
        newvalue = i

        while newvalue >=0 :
            print(newvalue)
            newvalue = bubbleup(i,var,array1)
    return array1

a = [3,8,10,5,15,7]

print(heapify(a))

        # num = (i-1)/2
# def callingthefunc():
#     hashdict = generate_frequency_map("135-0.txt")
#     newarray = list(hashdict.items())
#     heapify(newarray)
#     return newarray

# print(callingthefunc())
        
        
        
        
