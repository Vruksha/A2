'''The following code will determine how the minivan will open or not open its
doors.'''

#This will ask the user if the master unlock is activated or not. If it is activated, the user is one step closer to unlocking the door.
masterUnlock = input("Master unlock - Enter \"0\" for not activated and \"1\" for activated:" )

if masterUnlock == ("0"):
    print ("Sorry, kids are stuck inside forever.")

elif masterUnlock == ("1"):
    print ("First step complete to open door.")
    
 #This will ask the user which setting the gear shift is in. If it is in anything other than "P", the car door cannot be opened. 
    gearShift = input('Gear shift - Enter P,N,D,1,2,3, or R for gear shift setting:')

    if gearShift != ("P"):
        print ("Sorry, kids are stuck inside forever.")

    elif gearShift == ("P"):
        print ('Second step complete to open door.')
        
#This will ask the user if the child lock is on. If it is, the car door cannot be opened. 
        childLock = input ("Child Lock - Enter \"0\" for off and \"1\" for activated:")

        if childLock == ("1"):
            print ("Sorry, kids are stuck inside forever.")

        elif childLock == ("0"):
            print ("Third step completed to open car door.")
            
#This will ask the user if the right dashboard switch is on, and if it is, the door will open itself.
            rightSwitch = input("Right switch - Enter \"0\" for off and \"1\" for activated:")

            if rightSwitch == ("0"):
                print ("Sorry, kids are stuck inside forever.")

            elif rightSwitch == ("1"):
                print ("Right door opens.")

#This will ask the user if the right outside handle is unlocked. If it is, the door can be unlocked from the outside. 
                rightOutside = input("Outside right handle - Enter \"0\" for activated and \"1\" for not activated:")

                if rightOutside == ("1"):
                    print ("Sorry, kids are stuck inside forever.")

                elif rightOutside == ("O"):
                    print ("Right door opens.")

#This will ask the user if the right inside handle is unlocked. If it is, the door can be unlocked from the inside.
                    rightInside = input ("Inside right handle - Enter \"0\" for activated and \"1\" for not activated:")

                    if rigthInside == ("1"):
                        print ("Sorry, kids are stuck inside forever.")

                    elif rightInside == ("0"):
                        print ("Right door opens!")

#This will ask the user if the left dashboard switch is on, and if it is, the door will open itself.
                        leftSwitch = input("Left switch - Enter \"0\" for off and \"1\" for activated:")

                        if leftSwitch == ("0"):
                            print ("Sorry, kids are stuck inside forever.")

                        elif  leftSwitch == ("1"):
                            print ("Left door opens.")

#This will ask the user if the left outside handle is unlocked. If it is, the door can be unlocked from the outside. 
                            leftOutside = input("Outside Left handle -Enter \"0\" for activated and \"1\" for not activated:")

                            if leftOutside == ("1"):
                                print ("Sorry, kids are stuck inside forever.")

                            elif leftOutside == ("0"):
                                print ("Left door opens.")

#This will ask the user if the left inside handle is unlocked. If it is, the door can be unlocked from the inside.
                                leftInside = input ("Inside left handle - Enter \"0\" for activated and \"1\" for not activated:")

                                if leftInside == ("1"):
                                    print ("Sorry, kids are stuck inside forever.")

                                elif leftInside == ("0"):
                                    print ("Left door opens.")

                                    print ('masterUnlock', 'gearShift', 'childLock', 'rightSwitch', 'rightOutside', 'rightInside', 'leftSwitch', 'leftOutside', 'leftInside') 

'''The code ends with either the car opening or remaining unlocked. If the door unlocks, it will print the user inputs as a string.'''                      
                       
        
