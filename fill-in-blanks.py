def exit_program():
        #this function to exit the quiz directly
        exit = raw_input("Thank you SO Press enter to exit program. Good bye ")


def correct(text):
        """
this function appear when the user got all the answers are true
and the whole text will appear
"""
        #if all user's answers true , this gonna appear
        print text
        print ''
        print "Congratulations ! You nailed it ! You won "
        exit_program()
        

def check_answer(text,answers):
        
        """
        first we should know what level user chooses and the we
        ask the user to fill the blanks one by one by while loop
        and then if his answer was right the word gonna replaced
        instead of the blank
        """
           
        index = 0
        blanks_space = ['---1---','---2---','---3---','---4---','---5---']
        while index < len(answers):
                print ''
                print text
                print ''
                answer=raw_input("What is the best word you should put it in "+str(blanks_space[index])+' ?  ')
                
                while answer.lower() not in answers[index]:
                        print ''
                        print 'oh gosh it is wronge please try again '
                        answer = raw_input("What is the best word you should put it in "+str(blanks_space[index])+' ?  ')
                        
                if answer.lower() in answers[index]:
                        print ''
                        text = text.replace(blanks_space[index],answers[index])   
                        index += 1
                      
        correct(text)

    
easy_text = "Friendship isn't something that you can ---1--- easly. When you talk about ---2--- , you are talking about ---3---, loyalty, honesty and ---4--- ."
easy_answers =['describe','friendship','love','trust']
medium_text = "Mothers are the lovely and greatest ---1--- in the life. I love my ---2--- because she is the one who born ---3---. Always she take ---4--- for me ."
medium_answers = ['person','mother','me','care']
hard_text = "Saudi Arabia is the biggest Country in middle ---1--- . The Capital city of Saudi Arabia is ---2--- . It's a Country of the Two ---3--- Mosques . ---4--- is The Bride of Red Sea . There are the King Fahad's ---5---"
hard_answers = ['east' ,'riyadh' ,'holy' ,'jeddah' ,'fountain']

            
def level():
        #asked the user about level choice
        while True :
                
                user_level = raw_input("Please type in a difficulty level (easy , medium or hard ) : ").lower()

                if user_level == 'easy':
                        return check_answer(easy_text,easy_answers)
                elif user_level == 'medium':
                        return check_answer(medium_text,medium_answers)                        
                elif user_level == 'hard':
                        return check_answer(hard_text,hard_answers)
                else:
                        print "There is no "+user_level+" in our levels , Pick again !! "


def question():
        #asked the user if he wants to start or does not
        start = raw_input("Do you wanna start the quiz ?: ").lower()
        if start == 'yes':
                level()
        else:
                exit_program()


def greating():
        #asked the user about his name and say welcome to him
        name = raw_input("Hello there , What is your name ? ")
        print ''
        print 'Welcome  ' + name
        print ''
        print 'Here I gonna play with you a simple game that improve  '
        print 'your skills : '
        print ''
        print ''
        
#first
greating()
#second
question()
