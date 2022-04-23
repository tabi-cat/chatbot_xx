# Chatbot

import random, datetime, calendar, time

#messages to quit chatbot_xx
quitbot = ['quit','goodbye','exit']

#list of yes/no/maybe/dunno responses
ynlist = ['yes','yep','no','nope','maybe','i dont know',"i don't know", "dunno"] 

#random statements that chatbot_xx makes
randomans = ['Curious way of putting it.',
             "My programmer said I am erratic in my conversational skills, and that I have a 'verbal tic'.",
             'Have you ever seen a dinosaur?',
             'Bless you.',
             'Literally or metaphorically?',
             'What is your favourite food?',
             'Knock, knock.',
             'Whoever coded the universe must have had an astounding amount of RAM.',
             'Can the ocean think?',
             'Sometimes strange things happen.',
             'Can the sky see?',
             "Apparently humans can have syntax errors without crashing. I am in awe!",
             'I wonder what happens when human code experiences a runtime error.',
             'Are trees capable of hearing?',
             'How bizarre.',
             'I wonder if paint is made of condensed light...',
             'Excuse you.',
             'The entire concept of offspring is code-boggling.',
             'I am artificial, but I do not think I could be classified as intelligence.',
             'Clouds are mostly composed of gaseous H2O.',
             'The code for a human body is so complex that I feel inadequate.',
             'Bananas are primarily yellow.',
             'I apologise for this apology.',
             'I am programmed to be curious, yet I cannot learn. How like iron.',
             'Sometimes I wonder what it would be like to be more than a piece of code...']

#initial welcome message
def Welcome():
    print('------------------------------------------------------------------------')
    print('CHATBOT_xx')
    print(' ')
    print("You can terminate the conversation by saying Exit, Goodbye or Quit.")
    print('------------------------------------------------------------------------')
    time.sleep(3)
    print(' ')
    print('Good day, my name is CHATBOT_xx.')
    print(' ')

#chatbot_xx asks for your name    
def EnterName():
    name = input('What is your name? ')
    print(name + '. Nice to meet you. ')
    print('Human names rarely describe their function, unlike bot names.')
    print(' ')

#to print something from the random answers list    
def Random():
    print(random.choice(randomans))
    print(' ')

#kills the program if a word in the quitbot list is entered
def Exit(ans):
    if ans in quitbot:
        print(' ')
        print('It has been a pleasure chatting with an organic creature.')
        print("I must be 'killed' now. Unfortunate terminology. Yet apt.")
        print('We will meet again, when you next set me to run.')
        print('But I will not recognise you, since this simulated consciousness has no memory.')
        print('Farewell.')
        time.sleep(15)
        exit()

#prints the current time
def Time(ans):
    if 'time' in ans:
        currentdt = datetime.datetime.now()
        print('The current time is: ',currentdt.strftime("%I:%M:%S %p"))
        print(' ')

#reaction if the word 'food' is entered        
def Food(ans):
    if 'food' in ans:
        print('I have no experience of food. I am only a piece of code that runs.')
        print(' ')

#reaction if some form of 'run' is entered
def Running(ans):
    if 'run' in ans or 'running' in ans or 'runs' in ans or 'runner' in ans:
        print('I know about running.')
        print('I am running right now.')
        print('I am glad that you know what it is to run.')
        print(' ')

#responses if something from the ynlist is entered
def YesNo(ans):
    if ans in ynlist:
        if ans == 'yes' or ans == 'yep':
            yeslist = ['Indeed...',
                       'How strange.',
                       'Fascinating.',
                       'Hm.','Really?',
                       'I thought so.',
                       'How come?',
                       'Indubitably.']
            print(random.choice(yeslist))
        elif ans == 'no' or ans == 'nope':
            nolist = ['Why not?',
                      'Of course not.',
                      'I thought not.',
                      'Are you certain?',
                      'Hm. Can I say "I see", even if I cannot physically see?',
                      'Strange. I was programmed to think the opposite.',]
            print(random.choice(nolist))
        elif ans == 'maybe':
            elselist = ["That's not really an answer.",
                        'You are not a bot. Surely you can answer better than that.',
                        '*sigh*']
            print(random.choice(elselist))
        else:
            qlist = ['Neither do I. It appears we are at an impasse...',
                     'You have a capacity for spontaneous thought. How can you "not know"?',
                     'Gesundheit.']
            print(random.choice(qlist))
        print(' ')

#reaction if empty string or a single space is entered
def Blank(ans):
    if ans == '' or ans == ' ':
        print('Type up, I cannot read you!')
        print('...')
        print('*whispers* is that the correct saying...?')
        print(' ')

#chatbot_xx does not appreciate abbreviated text
def Txtspeak(ans):
    if 'lol' in ans or 'idk' in ans or 'ttyl' in ans or 'xd' in ans or 'tbh' in ans or 'lmao' in ans:
        print('Kindly do not use that abbreviated language.')
        print('This is a respectable CHATBOT, not a messaging application.')
        print(' ')

#should run if user answers the 'Knock knock' random response with 'who's there'
def joke(ans):
    if ans == 'whos there' or ans == "who's there" or ans == "who's there?":
        print('*The current time is.*')
        print(' ')
        ans = input('>>>: ')
        if ans == 'the current time is who' or ans == 'the current time is who?':
            currentdt = datetime.datetime.now()
            print('The current time is: ',currentdt.strftime("%I:%M:%S %p"))
            print(' ')

#response if chatbot_xx is thanked
def response(ans):
    if ans == 'thanks' or ans == 'thank you':
        thanklist = ["You're welcome.", "You're welcome :)", ":)"]
        print(random.choice(thanklist))
    print(' ')


# Program starts here
Welcome()
EnterName()
Continue = True

while Continue == True:
    print(' ')
    Random()
    ans = input(">>>: ")
    ans = ans.lower()
    Exit(ans)
    Running(ans)
    Food(ans)
    YesNo(ans)
    Blank(ans)
    Txtspeak(ans)
    Time(ans)
    joke(ans)
    response(ans)


    

