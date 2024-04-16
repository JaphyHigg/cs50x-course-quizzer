import sys, os, random, questions


def main():
    menu()


def menu():
    os.system("clear")
    print("CS50x Self Quizzer")
    print()
    print("1. Random question")
    print("2. Particular week's random question")
    print("3. Exit")
    print()
    choice = input("Your selection: ").strip().lower()
    if choice[0] == "1" or choice[0] == "r":
        get_random()
    elif choice[0] == "2" or choice[0] == "p":
        week = input("Which week?: ").strip()
        if week not in ("012345678910"):
            menu()
        get_random(week)
    else:
        sys.exit()


def get_random(w_num = None):
    if w_num == None:
        w_num = str(random.randint(1,1))
    week_picked = "week" + w_num
    week = getattr(questions, week_picked)
    w_len = len(week)
    q_index = random.randint(0,(w_len-1))
    os.system("clear")
    print(f"From Week {w_num}:")
    print()
    print(week[q_index][0]['question'])
    print()
    advance = input("Press enter to reveal answer ")
    os.system("clear")
    print(f"From Week {w_num}:")
    print()
    print(week[q_index][0]['question'])
    print()
    print(week[q_index][0]['answer'])
    print()
    sub_menu()


def sub_menu():
    choice = input("Press enter for next question, or type exit or main: ").strip().lower()
    if choice == "":
        get_random()
    elif choice[0] == "e":
        sys.exit()
    elif choice[0] == "m":
        main()
    else:
        get_random()


if __name__ == "__main__":
    main()