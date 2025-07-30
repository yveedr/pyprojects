num_pad = ((1, 2 , 3),
           (4, 5, 6), 
           (7, 8, 9), 
           ("*", 0, "#"))

for all in num_pad:
    for numbers in all:
       print(numbers, end=" ")
    print()