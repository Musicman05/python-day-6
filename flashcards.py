import random


# get_random _question
# Quit_app
# show_question
# show_answer


flashcards = [
{"question" : "Was It Sunny Today", "answer" : "No"}
{"question" : "Was It 70 out", "answer" : "Yes"}
{"question" : "Is Ice Cream or Cookies better", "answer" : "Ice Cream Always"}
]

'''
task; tell user goodbye.
input; none
side effect; prints a goodbye message to terminal
return;

'''
def quit_app():
    print("see you later bro")

'''
task; selects retrieves a random element in flashcard list
input; list
side effect;
return; flashcards (dictionary)

'''
def get_random_question(cards):
    random_card = random.choice(cards)
    return random_card
'''
task; display the question.
input; question card
side effect;
return;
'''

def show_question(card):
    question = card["question"]
    print("Question:", question)

'''
task; display answer
input; question card
side effect; print answer
return; none
'''

def show_answer(card):
    answer = card["answer"]
    print("answer:", answer)





def main():
    

    main():