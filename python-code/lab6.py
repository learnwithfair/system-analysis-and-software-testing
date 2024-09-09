def sum(array):    
    summation=0
    i = 0
    while(i<len(array)):
        summation+=array[i]
        i+=1 
    return summation


def average(array):   
    summation=sum(array)
    return summation/len(array)

array = input("Enter Array Elements: ").split(" ")
array=list(map(int,array))
print("Summation:",sum(array))
print(f"Average: {average(array):.2f}")