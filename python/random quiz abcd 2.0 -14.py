import random

quiz_questions = {
    "What is the capital of France?": {
        "a": "Paris",
        "b": "London",
        "c": "Berlin",
        "correct": "a",
    },
    "Which planet is known as the 'Red Planet'?": {
        "a": "Mars",
        "b": "Venus",
        "c": "Jupiter",
        "correct": "a",
    },
    "What is the chemical symbol for water?": {
        "a": "H2O",
        "b": "CO2",
        "c": "O2",
        "correct": "a",
    }
}

score = 0

def new_game():
    question = list(quiz_questions)
    random.shuffle(question)
    score = 0
    print("Welcome to the quiz XD")
    run_quiz(question,score)

def run_quiz(question,score):
    for q in question:
        print(q)
        options = quiz_questions[q]
        for option,answer in options.items():
            if option != "correct":
                print(f"{option.upper()}",{answer})
        user_answer = input("Enter your answer (a/b/c):").lower()
        if(user_answer == options["correct"]):
            print("Correct!! :)")
            score +=1
        else:
            print("Incorrect :( \n")
    print(f"You final score is {score}/{len(quiz_questions)}")
       
new_game()