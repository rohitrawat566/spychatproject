print "hello\n  Let's get started"
spy_name= raw_input("what is your name?  ")
if len(spy_name)>=2:
    print "Welcome " + spy_name + " \n glad to have you with us. "
    spy_salutation = raw_input("what should we call you(Mr. or Ms.)?     ")
    if spy_salutation == "Mr" or spy_salutation == "Ms" :
        spy_name=spy_salutation+" "+spy_name
        print "alright  " + spy_name + "   i'd like to know little more about you....."
        spy_age=input("what is your age?   ")
        if 12<spy_age<50:
            print "your age is correct"
            spy_rating=input("what is your rating?   ")
            if spy_rating>5.0:
                print "Great spy....."
            elif 3.5<spy_rating<=5.0:
                print "Good spy"
            elif 2.5<spy_rating<3.5:
                print"Bad spy..."
            else :
                print "who hired you...."
            spy_is_online = True
            print "Authentication is complete.  Welcome " + spy_name + " age " + str(spy_age) + " and rating of " + str(spy_rating) + " Proud to have you onboard"
        else: print "You are not eligible to be a spy. "

    else: print "sorry, Invalid salutation. "
else :
    print "a spy need to have a valid name. Try again please "