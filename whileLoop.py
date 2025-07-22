# exercicio 1:


#name =  input("Enter your name: ")

#while name == "":
    #print("user, you did not enter your name. try again.")
    #name =  input("Enter your name: ")
#print(f"Welcome {name}") 
    
    
    
#exercicio 2:

#user = input("Enter your user:")
#age = int(input("Enter your age: "))

#while age < 18 :
#    print("You must be at least 18")
#    age = int(input("Hello, {user}. Enter your age: "))
#print(f"Hello, {user}. Your age is {age}")


#Exercicio 3:

#food = input("Enter a food you like: (enter q to quit)")

#while not food == "q" :
#    food = input("Enter a food you like: (enter q to quit)")
#print("bye")


#Exercicio 4:

num = int(input("enter a number between 1-10 : "))

while num < 1 or num > 10:
    print("Your number is not valid. try again")
    num = int(input("enter a number between 1-10 : "))

print(f"your number is {num}")