import random

question = {"Who created Python?":"A",
            "What year was Python created?":"B",
            "Python is tributed to which comedy group?":"C",
            "Is Earth round?":"A"}

options = [["A. Guido van Rossum","B. Elon Musk","C. Bill GATES","D. Mark Zuckerburg"],["A. 1989","B. 1991","C. 2000","D. 2016"],["A. Lonely Island","B. Smosh","C. Monty Python","D. SNL"],["A. True","B. False","C. sometimes","D. what's Earth??"]]

def new_games():

    correct_guesses = 0
    question_num = 0
    while True:
        for key in question:
            print("****************************************")
            print(key)
            for i in options[question_num]:
                print(i)
            answer = input("Enter (A,B,C or D):").upper()
            correct_guesses += check_answer (question[key],answer) 
            question_num+=1

        again = input("play again?? (Y/N)").upper()
        if again == "Y":
            question_num = 0
            continue
        else:
            print(f"your score is {correct_guesses}")
            break

def check_answer(value,answer):
    if answer == value:
        print("Correct!!")
        return 1
    else:
        print("Incorrect :(")
        return 0
    
new_games()
