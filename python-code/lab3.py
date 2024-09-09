string = input("Please Enter a Number or string: ")
revString=string[::-1]
if string==revString:
    print("The Number or String is Palindrome")
else:
    print("The  Number or String is not Palindrome")