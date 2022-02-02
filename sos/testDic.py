import random

def int_main(void):
    print("Welcome to the vocabulary quiz program.\n")
    file_name = ("words.txt")
    #validating input
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print("The file name %s does not exist \n\nBye!" %file_name)
        return

    #number of words to be quizzed on
    while True:
        try:
            num_words = int(input("How many words would you like to be quizzed on? "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if num_words > 10 or num_words < 1:
            print("Please enter a valid number between 1 and 10.")
            continue
        else:
            break

    #File -> Dictionary
    dic = get_dic(file_name)
    print(dic)

    #Generating Question Bank
    bank = []
    for i in range(num_words):
        question = eng, *span = random.choice(list(dic.items()))
        bank.append(question)
        i += 1
    dbank = {}
    dbank = dict(bank)
    print(dbank)
    

    #Administering Quiz
    for eng, *span in dbank.items():
        print("English Word: ", eng)
        span_list = dbank[eng]
        print("span_list = dbank[eng] ->", type(span_list),"\n", span_list)
        num_trans = len(span_list)
        print("Spanish Word: ", span_list)
        print("Enter", num_trans, "equivalent Spanish word(s).")
        ans1 = input("Word [1]: ")
        count = num_words
        if num_trans == 1:
            if ans1.lower not in span_list:
                print("Incorrect.")
                count -= 1
            else:
                print("Correct!")
                
        else:
            ans2 = input("Word [2]: ")
            if ans1.lower or ans2.lower not in span_list:
                print("Incorrect.")
                count -= 1
            else:
                print("Correct!")
        print("\n---\n")   
        

    return 

def get_dic(file_name):
    engSpanDic = {}
    with open(file_name, "r") as file:
        for i in file:
            i = i.replace(",",":")
            key, *value = i.rstrip("\n").split(':')
            engSpanDic[key] = value
    return engSpanDic
    
void = None
int_main(void);

