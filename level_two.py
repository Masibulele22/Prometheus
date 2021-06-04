

map = [0.0,0.1,0.2,1.0,1.1,1.2,2.0,2.1,2.2]

XP = 50

Hero_location = map[0]

print("XP:",XP)

print("Location",Hero_location)

def moves():
    print(' 1. Up \n 2. Down \n 3. Right \n 4. Left')

moves()


tries = 0
XP = 50

while tries > -1:
    input_ = int(input("Please enter a move: "))
    tries +=1

    if input_ == 2:
         print("Wolf!!!....")
         print('Do you want to fight or run?')
         option = int(input("1. Fight \n 2. Run: "))
         if  option == 1:
             XP = XP - 30
             print("You beat the Wolf, -30 XP")
             print("XP: ", XP)
             print("Location", map[3])
             print(' ')
         else:
            print("You have chosen to Run now your new location is:",map[6])
            print('Nothing here')


    elif input_ == 3:
        print('well done you, you have the tresure + 20 XP')
        XP = XP + 20
        print("XP: ",XP)
        print("Location ", map[1])
        print(' ')

    elif input_ == 1:
         print("Sorry not a valid move, please retry...")
         
     	 
    elif input_ == 4:
         print("Sorry not a valid move, please retry...")
         
         
  
     

            


    
  
        
      
           
   
             
