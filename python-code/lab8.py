def calculation(num1,op,num2):
    if op=="+":
        return num1+num2
    elif op=="-":
        return num1-num2
    elif op=="*":
        return num2*num1
    elif op=="/":
        return num1/num2
    else:
        print("Please Enter Valid Operator(+,-,/,*)")
        

with open('input.txt', 'r') as file:
    input_data = file.read()


elements=list(map(int, input_data.replace(',', ' ').split()))
n=len(elements)


for i in range(0,n,2):
    add=calculation(elements[i],"+",elements[i+1])
    sub=calculation(elements[i],"-",elements[i+1])
    mul=calculation(elements[i],"*",elements[i+1])
    div=calculation(elements[i],"/",elements[i+1])
    result=[add,sub,mul,div]
    with open('output.txt', 'a') as file:
        file.write(f"Case-{i//2+1}: "+' '.join(map(str, result))+"\n")
print("Successfully Created File with Required Calculations")
