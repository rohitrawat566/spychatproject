print "hello"
spy_name= raw_input("what is your name?  ")
if len(spy_name)>=2:
    print "Welcome " + spy_name + " \n glad to have you with us. "
    spy_salutation = raw_input("what should we call you(Mr. or Ms.)?     ")
    if spy_salutation == "Mr" or spy_salutation == "Ms" :
        spy_name=spy_salutation+" "+spy_name
        print "alright  " + spy_name + "   i'd like to know little more about you....."
    else: print "sorry, Invalid salutation. "
else :
    print "a spy need to have a valid name. Try again please "