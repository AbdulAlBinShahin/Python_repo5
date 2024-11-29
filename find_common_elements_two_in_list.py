num1=list(map(int,input("enter num: ").split()))
num2=list(map(int,input("enter num: ").split()))
 
intersection=list(set(num1)& set(num2))
print(f"{intersection}")
