from steganography.steganography import Steganography #importing Steganography module
from datetime import datetime#importing date time
from spy_details import spy      #import spy dictionary from the file spy_details

time=datetime.now() # current date and time
print time          #print current time and date
print "hello\n  Let's get started" #greeting, initializing
STATUS_MESSAGE=["Available","Sleeping","At the gym","In a meeting","At work","At the movies","Busy","feeling wow!!"] #introducing list
friends=[{"name": "Divyanshu","age": 22,"rating": 5.0,"is_online":True,"chats": []},{"name": "Kaaju","age": 21,"rating":4.5,"is_online":True,"chats": []}]#dictionary within a list

def add_status(c_status):   #define a function
    if c_status != None:    #condition
        print "Your current status is "+ c_status #print current status
    else:                   #conditional statement
        print"You don't have any status currently.."
    existing_status=raw_input("You want to select from old status? Y/N")#giving option old/new
    if existing_status.upper()=="N":   #if user wants to use new status
        new_status=raw_input("Enter your status : ") #input new status
        if len(new_status)>0:#checking length of status
            STATUS_MESSAGE.append(new_status)        #adding new status to list..
    elif existing_status.upper()=="Y": #if select from old status
        serial_no=1          #set serial_no
        for old_status in STATUS_MESSAGE:    #introducing for loop
            print str(serial_no)+old_status  #print old status with serial no.
            serial_no=serial_no+1            #increment serial no.
        user_choice=input("Enter your choice :")#input choice
        new_status=STATUS_MESSAGE[user_choice-1]#set status
    current_status=new_status #set status current status
    return current_status     #return status

def add_friend():             #define add friend function
    frnd= {"name":"",         #set a dictionary (frnd)
           "age":0,
           "rating":0.0,
           "is_online":True,
           "chats":[]
           }
    frnd["name"]=raw_input("What is your friend's name ? ") #input friend's name
    frnd["age"]=input("What is your friend's age ?")        #input friend's age
    frnd["rating"]=input("What is your friend's rating ?")  #input friend's rating
    frnd["is_online"]=True    #set friend is online
    if len(frnd["name"])>2 and 12<frnd["age"]<50 and frnd["rating"]>spy["rating"] :#check condition for adding friend
       friends.append(frnd)   #add friend to friend list
    else:
        print 'Friend cannot be added..'   #conditional statement
    return len(friends)       #return no of friends
def select_frnd():            #define a function
    serial_no=1               #set serial no.
    for frnd in friends:      # traversing the dictionary friends to show the friends.
        print str(serial_no)+'.'+frnd['name']#print friend's name with serial no.
        serial_no=serial_no+1 #inceament
    user_selected_frnd=input('Enter your choice : ')#enter choice
    user_selected_frnd_index=user_selected_frnd-1 #decrementing b/c list doesn't start with zero
    return user_selected_frnd_index  #returning value to the function

def send_message():            #sending a message
    select_friend=select_frnd()#index value
    original_image = raw_input('What is the name of your image ? ')  # asking the user for an input of image
    secret_text = raw_input('What is your secret text ? ')# secret text to be entered
    output_path = "secretout.png" #predefined name of an image
    secret_text=str(select_friend)+secret_text#assigning the index with the text fro a reading a message validation
    Steganography.encode(original_image, output_path, secret_text)  # encoding the message with image
    print 'Your message has been successfully encoded..'#displaying for the user
    new_chat = {               # dictionary
        'message': secret_text,
        'time': datetime.now(),#current date and time
        'sent_by_me': True
    }
    friends[select_friend]['chats'].append(new_chat)  # appending the friend chat detail
    print'Your secret message is ready.'#displaying for the user

def read_message():
    select_friend = select_frnd()  # index value
    output_path = raw_input('Which image you want to decode ? ')  # asking the user for an input of image
    secret_text = Steganography.decode(output_path)  # decoding message
    a = int(secret_text[:1])  # checking if the right person is decoding the message or not
    if a == select_friend:
        secret_text = secret_text.replace(str(a), '')
        print 'Secret text is:' + secret_text  # Displaying for the user
        new_chat = {                           # dictionary
            'message': secret_text,
            'time': datetime.now(),
            'sent_by_me': False
            }
        friends[select_friend]['chats'].append(new_chat)  # appending the friend chat detail
        print'Your secret message has been saved...'  # Displaying for the user
    else:
        print "You are not correct person for decoding this message"  # displaying it for the user


def start_chat(spy_name,spy_age,spy_rating):             #user define function created
    current_status=None
    print "Here are your options " +spy_name + "\nMENU"             #Message given to the user
    show_menu = True                                     #by default value true for validation
    while show_menu:                                     #using loop for multiple times show the same thing
        choice = input('What do you want to do ?\n1.Add a status\n2.Add a friend\n3.Send a message\n4.Read a message\n0.Exit ')#choices given to the userinput from the user
        if choice ==1:                                   #conditional Statement
            current_status = add_status(current_status)
            print"Updated status is " + current_status
        elif choice==2:                                  #conditional Statement
            no_of_friends=add_friend()
            print "You have" + str(no_of_friends) + "friends"
        elif choice==3:
            send_message()   #calling send function for encoding
        elif choice==4:
            read_message()   #calling read function for decoding
        elif choice==0:                                  #conditional Statement
            show_menu=False                              #Terminating the program
        else:                                            #conditional Statement
            print "Invalid option selected by you.!! "   #Message for the user

spy_exist=raw_input("Are you a new user? Y/N  ")         #asking to the user (new user or not)
if spy_exist.upper()=="N":                               #conditional statement
    print "Welcome BACK....... %s \n age: %d \n rating: %d" %(spy["name"],spy['age'],spy['rating'])#displaying details of the user
    start_chat(spy['name'],spy['age'],spy['rating'])     #calling a chat function
elif spy_exist.upper()=="Y":                             #conditional statement
    spy['name']= raw_input("what is your name?  ")          #message for the user to input NAME
    if spy['name'].isalpha():                               #checking the user name correct or not

        if len(spy['name'])>=2:                             #checking the lenth of the characters
            print "Welcome " + spy['name'] + " \n glad to have you with us. " # Welcome with user name
            spy['salutation'] = raw_input("what should we call you(Mr or Ms)?     ") # Message for the user and input from the user
            if spy['salutation'].upper() == "MR" or spy['salutation'].upper() == "MS" :  #conditional statement
                spy['name']=spy['salutation'].upper()+" "+spy['name'].upper()     #Concatinating  2 string (name and salutation)
                print "alright  " + spy['name'] + "   i'd like to know little more about you....." #asking for more details
                spy['age']=input("what is your age?   ")    #asking age for input
                if 12<spy['age']<50:                        #conditional statement (is age correct or not)
                    print "your age is correct"          #message user's age is right
                    spy['rating']=input("what is your rating?   ") # input rating of user
                    if spy['rating']>5.0:                   #conditional statement (check rating)
                        print "Great spy....."           #message for the user
                    elif 3.5<spy['rating']<=5.0:            #check rating
                        print "Good spy"                 #message
                    elif 2.5<spy['rating']<3.5:             #check rating
                        print"Bad spy..."                #message
                    else :                               #conditional statement
                        print "who hired you...."        #massage for user
                    spy['is_online'] = True                 #initiating the variable
                    print "Authentication is complete.  Welcome " + spy['name'] + "\n age: " + str(spy['age']) + " \n Rating: " + str(spy['rating']) + "\n Proud to have you onboard"#concatination
                                                         #authentication complete massage
                                                         #And final Welcome
                    start_chat(spy['name'], spy['age'], spy['rating']) #calling a function
                else: print "You are not eligible to be a spy. " #conditional message- if age is not valid

            else: print "sorry, Invalid salutation. "    #conditional statement- if salutation not valid
        else :                                           #conditional statement
            print "a spy need to have a valid name. Try again please " #message if name's character lenth is smaller then 2
    else : "invalid name"                                #massage if name is not valid

else: print "Invalid option"                             #if user type wrong key