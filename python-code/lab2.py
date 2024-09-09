def calculation(num1,op,num2):
    if op=="+":
        return num1+num2
    elif op=="-":
        return num1-num2
    elif op=="*":
        return num2*num1
    elif op=="/":
        return num1/num2
    elif op=="%":
        return num1%num2
    else:
        print("Please Enter Valid Operator(+,-,/,*,%)")
        
        
n=int(input("Please Enter n: "))
elements=input(f"Please Enter {n*2} Elements space by space and at last please enter a operator(+,-,*,/,%): ").split(" ")
op=elements[-1]
elements=list(map(int,elements[:-1]))

print("Output = ",end="")
for i in range(0,2*n,2):
    cal=calculation(elements[i],op,elements[i+1])
    print(cal,end=" ")
print()