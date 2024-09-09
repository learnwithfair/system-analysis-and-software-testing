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
        
        

print("Enter Sample Input: ",end="")
while True:
    num1,op,num2,equal=input().split(" ")
    num1,num2=int(num1),int(num2)
    if equal=='=':
        print(f"Result : {num1} {op} {num2} = {calculation(num1,op,num2)}")

    else:
        print("Please Enter in this format link (1 + 2 =)")