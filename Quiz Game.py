questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "A", "A", "A", "B")
guesses = []
check = ["A", "B", "C", "D"]
score = 0
question_num = 0

for question in questions:
    print("---------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter the correct option:")
    guesses.append(guess.upper())

    if guesses[question_num] == answers[question_num]:
        score += 1
        print("Correct")
    elif guesses[question_num] in check:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")
    else:
        print("Invalid Input")
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
