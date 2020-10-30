from MultiChoice import Question
from MultiChoice import TrueFalse
from MultiChoice import MultiChoice

get_name = Question("What is your name?")  # setup
user = get_name()                          # get input
print(user)                                # print


question = TrueFalse("True or False: Python3 is the best!")
answer = question()
print(answer)

question = MultiChoice(
    "What is your favorite color?\n"
    "You must choose one of the following:",
    options=("Red", "Orange", "Yellow", "Green", "Blue", "Purple"),
)
answer = question()
print(answer)