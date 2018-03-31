from spy_details import spy_name,spy_age,spy_rating      #import a file
print "hello\n  Let's get started"                       #greeting, initializing

STATUS_MESSAGE=["Available","Sleeping","At the gym","In a meeting","At work","At the movies","Busy","feeling wow!!"] #introducing list


def add_status(c_status):
    if c_status != None:
        print "Your current status is "+ c_status
    else:
        print"You don't have any status currently.."
    existing_status=raw_input("You want to select from old status? Y/N")
    if existing_status.upper()=='N':
        new_status=raw_input('Enter your status : ')
        if len(new_status)>0:
            STATUS_MESSAGE.append(new_status)            #adding new status to list..
    elif existing_status.upper()=='Y':
        serial_no=1
        for old_status in STATUS_MESSAGE:
            print str(serial_no)+old_status
            serial_no=serial_no+1
        user_choice=input('Enter your choice :')
        new_status=STATUS_MESSAGE[user_choice-1]
    current_status=new_status
    return current_status


def start_chat(spy_name,spy_age,spy_rating):             #user define function created
    current_status=None
    print 'Here are your options ' +spy_name             #Message given to the user
    show_menu = True                                     #by default value true for validation
    while show_menu:                                     #using loop for multiple times show the same thing
        choice = input('What do you want to do ?\n1.Add a status\n2.Add a friend\n0.Exit ')#choices given to the userinput from the user
        if choice ==1:                                   #conditional Statement
            current_status = add_status(current_status)
            print'Updated status is ' + current_status
        elif choice==2:                                  #conditional Statement
            print 'This will add a friend'               #Message for the user
        elif choice==0:                                  #conditional Statement
            show_menu=False                              #Terminating the program
        else:                                            #conditional Statement
            print 'Invalid option selected by you.!! '   #Message for the user

spy_exist=raw_input("Are you a new user? Y/N  ")         #asking to the user (new user or not)
if spy_exist.upper()=="N":                               #conditional statement
    print "Welcome BACK....... %s \n age: %d \n rating: %d" %(spy_name,spy_age,spy_rating)#displaying details of the user
    start_chat(spy_name,spy_age,spy_rating)              #calling a chat function
elif spy_exist.upper()=="Y":                             #conditional statement
    spy_name= raw_input("what is your name?  ")          #message for the user to input NAME
    if spy_name.isalpha():                               #checking the user name correct or not

        if len(spy_name)>=2:                             #checking the lenth of the characters
            print "Welcome " + spy_name + " \n glad to have you with us. " # Welcome with user name
            spy_salutation = raw_input("what should we call you(Mr. or Ms.)?     ") # Message for the user and input from the user
            if spy_salutation.upper() == "MR." or spy_salutation.upper() == "MS." :  #conditional statement
                spy_name=spy_salutation.upper()+" "+spy_name.upper()     #Concatinating  2 string (name and salutation)
                print "alright  " + spy_name + "   i'd like to know little more about you....." #asking for more details
                spy_age=input("what is your age?   ")    #asking age for input
                if 12<spy_age<50:                        #conditional statement (is age correct or not)
                    print "your age is correct"          #message user's age is right
                    spy_rating=input("what is your rating?   ") # input rating of user
                    if spy_rating>5.0:                   #conditional statement (check rating)
                        print "Great spy....."           #message for the user
                    elif 3.5<spy_rating<=5.0:            #check rating
                        print "Good spy"                 #message
                    elif 2.5<spy_rating<3.5:             #check rating
                        print"Bad spy..."                #message
                    else :                               #conditional statement
                        print "who hired you...."        #massage for user
                    spy_is_online = True                 #initiating the variable
                    print "Authentication is complete.  Welcome " + spy_name + "\n age: " + str(spy_age) + " \n Rating: " + str(spy_rating) + "\n Proud to have you onboard"#concatination
                                                         #authentication complete massage
                                                         #And final Welcome
                    start_chat(spy_name, spy_age, spy_rating) #calling a function
                else: print "You are not eligible to be a spy. " #conditional message- if age is not valid

            else: print "sorry, Invalid salutation. "    #conditional statement- if salutation not valid
        else :                                           #conditional statement
            print "a spy need to have a valid name. Try again please " #message if name's character lenth is smaller then 2
    else : "invalid name"                                #massage if name is not valid

else: print "Invalid option"                             #if user type wrong key