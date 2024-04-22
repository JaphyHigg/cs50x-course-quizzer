import sys, os, random, questions

seen = [[],[],[]]

def main(weeks = None):
    weeks = get_questions()
    menu(weeks)


def get_questions():
    weeks = {"w0" : questions.week0, "w1" : questions.week1, "w2" : questions.week2}
    return weeks


def menu(weeks):
    os.system("clear")
    print("CS50x Self Quizzer\n")
    print("1. Random question")
    print("2. Particular week's random question")
    print("3. Exit\n")
    while True:
        choice = input("Your selection: ").strip().lower()
        if choice == "1" or choice[0] == "r":
            get_random(weeks)
        elif choice == "2" or choice[0] == "p":
            while True:
                w_num = input("Which week? (0, 1, or 2): ").strip()
                #if w_num not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
                if w_num not in ("0", "1", "2"):
                    continue
                else:
                    get_random(weeks, w_num)
        elif choice == "3" or choice[0] == "e":
            sys.exit()
        else:
            print("Invalid choice, please choose option 1, 2, or 3.")
            continue


def get_random(weeks, w_num = None):
    global seen
    specific_week = True
    if w_num == None:
        specific_week = False
        w_num = str(random.randint(0,2))
    week_picked = "w" + w_num
    week = weeks[week_picked]
    w_len = len(week)
    q_index = random.randint(0,(w_len-1))
    os.system("clear")
    w_num_int = int(w_num)
    if len(seen[w_num_int]) == w_len:
        seen[w_num_int] = []
    if week[q_index][0]['question'] not in seen[w_num_int]:
        print(f"From Week {w_num}:\n")
        print(week[q_index][0]['question'] + "\n")
        advance = input("Press enter to reveal answer ")
        os.system("clear")
        print(f"From Week {w_num}:\n")
        print(week[q_index][0]['question'] + "\n")
        print(week[q_index][0]['answer'] + "\n")
        seen[w_num_int].extend({week[q_index][0]['question']})
        if specific_week:
            return sub_menu(weeks, w_num)
        return sub_menu(weeks)
    else:
        if specific_week:
            return get_random(weeks, w_num)
        return get_random(weeks)


def sub_menu(weeks, w_num = None):
    choice = input("Press enter for next question, or type exit or menu: ").strip().lower()
    if choice == "":
        get_random(weeks, w_num)
    elif choice[0] == "e":
        sys.exit()
    elif choice[0] == "m":
        menu(weeks)
    else:
        get_random(weeks)


if __name__ == "__main__":
    main()