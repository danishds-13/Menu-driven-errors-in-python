def div(a,b):
    c=a/0
    print("zero  division error ")
  
def add(a,b):
    c=a+b
    print(d)
    print("name error example")
  
def sub(a,b):
    printf("sub is :",a-b)
    print("IO error example")
  
while True:  
    print("\nMAIN MENU")  
    print("1. zero division error example:")
    print("2. Name error example:")
    print("3. IO error example")
    print("4. indentation error example:")
    print("5. syntax error example:")
    print("6. file not found error example:")
    print("7. import error example:")
    print("8. unicode error example:")
    print("9. keyerror example:")
    print("10. exit")
    choice2= int(input("Enter the Choice:"))  
  
    
    if choice2 == 1:  
        div(8,9)
              
    elif choice2 == 2:  
        add(5,5)
              
    elif choice2 == 3:  
        sub(8,6)
  
    elif choice2 == 4: 
        num=5
        if num>0:
            print("Number is greater  than zero:")
        print("indentation error example:")
        
        
    elif choice2 == 5:
        n=int(input("Enter number:"))
        fact=1
        while(n>0):
            fact=fact*n
            n=n-1
        print("Factorial of the number is: ")
        print(fact)
        
    elif choice2 == 6:
        open("imaginary.txt")
        print("File not found error :")
        
    elif choice2 == 7:
        import request
        print("Import error example:")
        
    elif choice2 == 8:
        str(u'éducba')
        print(str)
        print("Unicode error example:")
        print("we have not specified any encoding at the starting of this program, and therefore it throws an error, and the default encoding that is used is 7-bit encoding, and it cannot recognize the characters that are outside the 0 to 128 range.")
    
    elif choice2 == 9:
        ages={'A':45,'B':51,'C':67}  
        print(ages['A'])  
        print(ages['B'])  
        print(ages['C'])  
        print(ages['D'])  
        print("Key error example :")
        
    else:  
        print("Oops! Incorrect Choice.")  
