questions = ("What is 15 + 27?",
             "What is 8 x 7?", 
             "What is 45 / 5?", 
             "What is 12 - 8?", 
             "What is 6 x 3 + 2?",)

options = (("A. 32", "B. 42", "C. 40", "D. 45", "E. 52"), 
           ("A. 48", "B. 54", "C. 56", "D. 63", "E. 64"), 
           ("A. 7", "B. 8", "C. 9", "D. 10", "E. 11"), 
           ("A. 2", "B. 3", "C. 4", "D. 5", "E. 6"), 
           ("A. 18", "B. 20", "C. 22", "D. 24", "E. 26"))

answers = ("C", "C", "C", "C", "B")
guesses = []
score = 0
question_num = 0


for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, C or E): ").upper()
    guesses.append(guess)
    
    if guess == answers[question_num]:
       print("CORRECT!")
       score +- 1
    else:
        print("INCORRECT!")
        print(f"the correct answer is: {answers[question_num]} ")
    
    question_num += 1
    
print("---------------------")
print("       RESULTS       ")
print("---------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score / len(question) * 100)
print(f"your score is: {score}%")