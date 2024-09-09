n=int(input("Please Enter a number: "))
fact=1
for i in range(1,n+1):
   prev=fact
   fact = i*fact
   # To verify the factorial  
   print(f"In {i} iteration factorial is {prev} X {i} = {fact}")

# while loop 
# i = 1
# while i<=n:
#    prev=fact
#    fact = i*fact
#    # To verify the factorial  
#    print(f"In {i} iteration factorial is {i} X {i-1}! = {fact}")
#    i+=1
   
print(f"{n}! = {fact}")