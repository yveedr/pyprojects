username = input("Enter a username: ")

if len(username) > 12: 
  print("Your username cannot be more than 12 characters")
elif not username.find(" ") == -1:
  print("your username cannot contain spaces")
elif not username.isalpha():
  print("your username cannot have digits")
else:
  print(f"Welcome {username}")