questions = ("What is full of holes but still holds water?: ",
             "How many continents are there on Earth?:",
             "Who wrote ""Romeo and Juliet""?: ",
             "What is the chemical symbol for water?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A) London", "B) Berlin", "C) Rome", "D) Paris"),
           ("A) 5", "B) 6", "C) 7", "D) 8"),
           ("A) William Shakespeare", "B) Charles Dickens", "C) Jane Austen", "D) Arthur Conan Doyle"),
           ("A)O2", "B) H2O", "C) CO2", "D) N2"),
           ("A) Mercury", "B) Venus", "C) Earth", "D) Mars"))

answers = ("D", "C", "A", "B", "B")
guesses = []
check = ["A", "B", "C", "D"]
score = 0
question_num = 0

for question in questions:
    print("---------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    while True:  # Add a while loop for input validation
        guess = input("Enter the correct option:").strip().upper()
        if guess in check:
            break
        else:
            print("Invalid Input. Please enter A, B, C, or D.")

    guesses.append(guess)

    if guesses[question_num] == answers[question_num]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("---------------------------------------------")
print("Quiz Complete")
print("---------------------------------------------")
print("Answers:", end=" ")
for answer in answers:
    print(answer, end=" ")
print()
print("Guesses:", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()
print("Score Percentage:", round(score / len(questions) * 100, 2), "%")
print("---------------------------------------------")
