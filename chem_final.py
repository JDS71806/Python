from dataclasses import dataclass
import random

@dataclass
class Element:
    symbol:str
    name:str
    group:int
    period:int
    atomic_mass:float
    protons:int
    
def random_element() -> Element:
    r = random.randint(1,88)
    if r == 1:
        return Element('H','Hydrogen',1,1,1.008,1)
    elif r == 2:
        return Element('He','Helium',18,1,4.003,2)
    elif r == 3:
        return Element('Li','Lithium',1,2,6.941,3)
    elif r == 4:
        return Element('Be','Beryllium',2,2,9.012,4)
    elif r == 5:
        return Element('B','Boron',13,2,10.811,5)
    elif r == 6:
        return Element('C','Carbon',14,2,12.011,6)
    elif r == 7:
        return Element('N','Nitrogen',15,2,14.007,7)
    elif r == 8:
        return Element('O','Oxygen',16,2,15.999,8)
    elif r == 9:
        return Element('F','Flourine',17,2,18.998,9)
    elif r == 10:
        return Element('Ne','Neon',18,2,20.180,10)
    elif r == 11:
        return Element('Na','Sodium',1,3,22.990,11)
    elif r == 12:
        return Element('Mg','Magnesium',2,3,24.305,12)
    elif r == 13:
        return Element('Al','Aluminium',13,3,26.982,13)
    elif r == 14:
        return Element('Si','Silicon',14,3,28.086,14)
    elif r == 15:
        return Element('P','Phosphorus',15,3,30.974,15)
    elif r == 16:
        return Element('S','Sulfur',16,3,32.066,16)
    elif r == 17:
        return Element('Cl','Chlorine',17,3,35.453,17)
    elif r == 18:
        return Element('Ar','Argon',18,3,39.948,18)
    elif r == 19:
        return Element('K','Potassium',1,4,39.098,19)
    elif r == 20:
        return Element('Ca','Calcium',2,4,40.078,20)
    elif r == 21:
        return Element('Sc','Scandium',3,4,44.956,21)
    elif r == 22:
        return Element('Ti','Titanium',4,4,47.867,22)
    elif r == 23:
        return Element('V','Vanadium',5,4,50.942,23)
    elif r == 24:
        return Element('Cr','Chromium',6,4,51.996,24)
    elif r == 25:
        return Element('Mn','Manganese',7,4,54.938,25)
    elif r == 26:
        return Element('Fe','Iron',8,4,55.845,26)
    elif r == 27:
        return Element('Co','Cobalt',9,4,58.933,27)
    elif r == 28:
        return Element('Ni','Nickel',10,4,58.693,28)
    elif r == 29:
        return Element('Cu','Copper',11,4,63.546,29)
    elif r == 30:
        return Element('Zn','Zinc',12,4,65.38,30)
    elif r == 31:
        return Element('Ga','Gallium',13,4,69.723,31)
    elif r == 32:
        return Element('Ge','Germanium',14,4,72.631,32)
    elif r == 33:
        return Element('As','Arsenic',15,4,74.922,33)
    elif r == 34:
        return Element('Se','Selenium',16,4,78.971,34)
    elif r == 35:
        return Element('Br','Bromine',17,4,79.904,35)
    elif r == 36:
        return Element('Kr','Krypton',18,4,84.798,36)
    elif r == 37:
        return Element('Rb','Rubidium',1,5,86.468,37)
    elif r == 38:
        return Element('Sr','Strontium',2,5,87.62,38)
    elif r == 39:
        return Element('Y','Yttrium',3,5,88.906,39)
    elif r == 40:
        return Element('Zr','Zicronium',4,5,91.224,40)
    elif r == 41:
        return Element('Nb','Niobium',5,5,92.906,41)
    elif r == 42:
        return Element('Mo','Molybdenum',6,5,95.95,42)
    elif r == 43:
        return Element('Tc','Technetium',7,5,98.907,43)
    elif r == 44:
        return Element('Ru','Ruthenium',8,5,101.07,44)
    elif r == 45:
        return Element('Rh','Rhodium',9,5,102.906,45)
    elif r == 46:
        return Element('Pd','Palladium',10,5,106.42,46)
    elif r == 47:
        return Element('Ag','Silver',11,5,107.868,47)
    elif r == 48:
        return Element('Cd','Cadium',12,5,112.414,48)
    elif r == 49:
        return Element('In','Indium',13,5,114.818,49)
    elif r == 50:
        return Element('Sn','Tin',14,5,118.711,50)
    elif r == 51:
        return Element('Sb','Antimony',15,5,121.760,51)
    elif r == 52:
        return Element('Te','Tellurium',16,5,127.6,52)
    elif r == 53:
        return Element('I','Iodine',17,5,126.904,53)
    elif r == 54:
        return Element('Xe','Xenon',18,5,131.294,54)
    elif r == 55:
        return Element('Cs','Cesium',1,6,132.905,55)
    elif r == 56:
        return Element('Ba','Barium',2,6,137.328,56)
    elif r == 57:
        return Element('Hf','Hafnium',4,6,178.49,72)
    elif r == 58:
        return Element('Ta','Tantalum',5,6,180.948,73)
    elif r == 59:
        return Element('W','Tungsten',6,6,183.84,74)
    elif r == 60:
        return Element('Re','Rhenium',7,6,186.207,75)
    elif r == 61:
        return Element('Os','Osmium',8,6,190.23,76)
    elif r == 62:
        return Element('Ir','Iridium',9,6,192.217,77)
    elif r == 63:
        return Element('Pt','Platinum',10,6,195.085,78)
    elif r == 64:
        return Element('Au','Gold',11,6,196.967,79)
    elif r == 65:
        return Element('Hg','Mercury',12,6,200.592,80)
    elif r == 66:
        return Element('Tl','Thallium',13,6,204.383,81)
    elif r == 67:
        return Element('Pb','Lead',14,6,207.2,82)
    elif r == 68:
        return Element('Bi','Bismuth',15,6,208.980,83)
    elif r == 69:
        return Element('Po','Polonium',16,6,208.982,84)
    elif r == 70:
        return Element('At','Astatine',17,6,209.987,85)
    elif r == 71:
        return Element('Rn','Radium',18,6,222.018,86)
    elif r == 72:
        return Element('Fr','Francium',1,7,223.020,87)
    elif r == 73:
        return Element('Ra','Radium',2,7,226.025,88)
    elif r == 74:
        return Element('Rf','Rutherfordium',4,7,262,104)
    elif r == 75:
        return Element('Db','Dubnium',5,7,261,105)
    elif r == 76:
        return Element('Sg','Seaborgium',6,7,266,106)
    elif r == 77:
        return Element('Bh','Bohrium',7,7,264,107)
    elif r == 78:
        return Element('Hs','Hassium',8,7,269,108)
    elif r == 79:
        return Element('Mt','Meitnerium',9,7,278,109)
    elif r == 80:
        return Element('Ds','Darmstadtium',10,7,281,110)
    elif r == 81:
        return Element('Rg','Roentgenium',11,7,280,111)
    elif r == 82:
        return Element('Cn','Copernicium',12,7,285,112)
    elif r == 83:
        return Element('Nh','Nihonium',13,7,286,113)
    elif r == 84:
        return Element('Fl','Flerovium',14,7,289,115)
    elif r == 85:
        return Element('Mc','Moscovium',15,7,289,116)
    elif r == 86:
        return Element('Lv','Livermonium',16,7,293,116)
    elif r == 87:
        return Element('Ts','Tennessine',17,7,294,117)
    else:
        return Element('Og','Oganesson',18,7,294,118)
    
def game_3(charge1:int, charge2:int) -> str:
    if charge1*2 + charge2 == 0:
        return 'X2Y'
    elif charge1 + charge2*2 == 0:
        return 'XY2'
    elif charge1*2 + charge2*3 == 0:
        return 'X2Y3'
    elif charge1*3 + charge2*2 == 0:
        return 'X3Y2'
    elif charge1 + charge2*3 == 0:
        return 'XY3'
    elif charge1*3 + charge2 == 0:
        return 'X3Y'
    else:
        return 'XY'
    
def game_5(element:Element) -> [str]:
    if element.protons <= 2:
        answer += '1s' + str(element.protons)
    if element.protons <= 4:
        return '1s2 2s' + str(element.protons-2)
    if element.protons <= 10:
        return '1s2 2s2 2p' + str(element.protons-4)
    if element.protons <= 12:
        return '1s2 2s2 2p6 3s' + str(element.protons -10)
    if element.protons <= 18:
        return '1s2 2s2 2p6 3s2 3p' + str(element.protons-12)
    if element.protons <= 20:
        return '1s2 2s2 2p6 3s2 3p6 4s' + str(element.protons-18)   
    if element.protons <= 30:
        return '1s2 2s2 2p6 3s2 3p6 4s2 3d' + str(element.protons-20)       
    if element.protons <= 36:
        return '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p' + str(element.protons-30)    
    if element.protons <= 38:
        return '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s' + str(element.protons-36)
    if element.protons <= 48:
        return '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d' + str(element.protons-38)    
    if element.protons <= 54:
        return '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p' + str(element.protons-48)
    if element.protons <= 56:
        return '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s' + str(element.protons-54)
    if element.protons <= 70:
        return '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f' + str(element.protons-56)
    if element.protons <= 80:
        return '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d' + str(element.protons-70)
    if element.protons <= 86:
        return '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p' + str(element.protons-80)
    if element.protons <= 88:
        return '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s' + str(element.protons-86)
    if element.protons <= 102:
         return '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f' + str(element.protons-88)
    if element.protons <= 112:
         return '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d' + str(element.protons-102)
    if element.protons <= 118:
         return '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p' + str(element.protons-112)
        
    
def game_5e(guess:str) -> str:
    if 'He' in guess:
        return '1s2'
    if 'Ne' in guess:
        return '1s2 2s2 2p6'
    if 'Ar' in guess:
        return '1s2 2s2 2p6 3s2 3p6'
    if 'Kr' in guess:
        return '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6'
    if 'Xe' in guess:
        return '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6'
    if 'Rn' in guess:
        return '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6'
    if 'Og' in guess:
        '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p6'
             
def play_game():
    print('available games: \n1 = guess the element\n2 = find the element\n3 = atomic symbol\n4 = bonding atoms\n5 = molar mass\n6 = electron configuration\n')
    u_input = input("Enter the number representing the game you would like to play or type 'Leave': ")
    if u_input.isdigit() == True:
        while u_input != 'Leave':
        
            if u_input == '1':
                element = random_element()
                print('\nThis element has ' + str(element.protons) + ' protons. Enter your answer as symbol , name')
                guess = input('Answer : ')
                
                if element.symbol.lower() in guess.lower() and element.name.lower() in guess.lower():
                    print('You are correct, the element is : ' + element.symbol + ' , ' + element.name + '\n')
                    u_input = input("Enter the number representing the game you would like to play or type 'Leave': ")
                    
                elif element.symbol.lower() in guess.lower():
                    print('You had the correct symbol, but the correct name was ' + element.name + '\n')
                    u_input = input("Enter the number representing the game you would like to play or type 'Leave': ")
                    
                elif element.name.lower() in guess.lower():
                    print('You had the correct name, but the correct symbol was ' + element.symbol + '\n')
                    u_input = input("Enter the number representing the game you would like to play or type 'Leave': ")
                    
                else:
                    print('Incorrect, the correct answer was : ' + element.symbol + ' , ' + element.name + '\n')
                    u_input = input("Enter the number representing the game you would like to play or type 'Leave': ")
                    
            if u_input == '2':
                element = random_element()
                print('\nIdentify the element if the group is ' + str(element.group) + ', and the period is ' + str(element.period) + '\n')
                guess = input('Enter your answer here as symbol, name : ')
                if element.symbol in guess and element.name in guess:
                    print('\nYou are correct! The correct Answer was : ' + element.symbol + ', ' + element.name + '\n')
                    u_input = input("Enter the number representing the game you would like to play or type 'Leave': ")
                else:
                    print('You are incorrect! the correct answer was : ' + element.symbol + ', ' + element.name + '\n')
                    u_input = input("Enter the number representing the game you would like to play or type 'Leave': ")
                    
            if u_input == '3':
                neutrons = random.randint(0,100)
                electrons = random.randint(-5,5)
                element = random_element()
                print('\nElement : ' + element.symbol + ' , ' + element.name)
                print('\nIf this element has a mass number of ' + str(element.protons + neutrons) + ' and a charge of ' + str(electrons))
                print('\nFind the amount of protons, neutrons, and electrons\n')
                guess = input('Enter your answer as protons, neurtons, electrons : ')
                
                if str(element.protons + electrons) in guess and str(neutrons - electrons) in guess and str(abs(electrons)) in guess:
                    print('You are correct!, The answer was ' + str(element.protons + electrons) + ' , ' + str(element.protons + electrons + neutrons) + ' , ' + str(electrons) + '\n')
                    u_input = input("Enter the number representing the game you would like to play or type 'Leave': ")
                
                elif str(abs(electrons)) not in guess and str(element.protons + electrons) in guess and str(neutrons - electrons) in guess:
                    print ('You had the correct protons and neutrons but the correct amount of electrons was ' + str(electrons) + '\n')
                    u_input = input("Enter the number representing the game you would like to play or type 'Leave': ")
                
                elif str(neutrons - electrons) not in guess and str(element.protons + electrons) in guess and str(abs(electrons)) in guess:
                    print('You had the correct amount of protons and electrons, but the correct amount of neutrons was : ' + str(neutrons) + '\n')
                    u_input = input("Enter the number representing the game you would like to play or type 'Leave': ")
                
                elif str(element.protons + electrons) not in guess and str(neutrons - electrons) in guess and str(abs(electrons)) in guess:
                    print('You had the correct amount of neutrons and electrons, but the correct amount of protons was : ' + str(element.protons+electrons))
                    u_input = input("Enter the number representing the game you would like to play or type 'Leave': ")
                    
                elif str(element.protons + electrons) not in guess and str(neutrons - electrons) not in guess and str(abs(electrons)) in guess:
                    print('You had the correct amount of electrons, but the correct amount of protons and neutrons was : ' + str(element.protons+electrons) + ' , ' + str(neutrons))
                    u_input = input("Enter the number representing the game you would like to play or type 'Leave': ")
                    
                elif str(element.protons + electrons) not in guess and str(abs(electrons)) not in guess and str(neutrons - electrons) in guess:
                    print('You had the correct amount of neutrons, but the correct amount of protons and electrons was : ' + str(element.protons + electrons) + ' , ' + str(electrons))
                    u_input = input("Enter the number representing the game you would like to play or type 'Leave': ")
                    
                elif str(neutrons - electrons) not in guess and str(element.protons + electrons) in guess and str(abs(electrons)) not in guess:
                    print('You had the correct amount of protons, but the correct amoun of neutrons and electrons was : ' + str(neutrons) + ' , ' + str(electrons))
                    u_input = input("Enter the number representing the game you would like to play or type 'Leave': ")
                
                else:
                    print('\nYou are incorrect. The correct answer was : ' + str(element.protons + electrons) + ' , ' + str(element.protons + electrons + neutrons) + ' , ' + str(electrons) + '\n')
                    u_input = input("Enter the number representing the game you would like to play or type 'Leave': ")
                    
            if u_input == '4':
                x_charge = random.randint(1,3)
                y_charge = random.randint(-3,-1)
                print('\nBond elements X and Y when X has a charge of ' + str(x_charge) + ', and Y has a charge of ' + str(y_charge) + '\n')
                guess = input('Enter your answer with X and then Y : ')
                
                if guess == game_3(x_charge, y_charge):
                    print('\nYou are correct! The answer was : ' + game_3(x_charge, y_charge) + '\n')
                    u_input = input("Enter the number representing the game you would like to play or type 'Leave': ")
                
                else:
                    print('\nYou are incorrect! The answer was : ' + game_3(x_charge, y_charge) + '\n')
                    u_input = input("Enter the number representing the game you would like to play or type 'Leave': ")
                    
            if u_input == '5':
                r1 = random.randint(1,3)
                r2 = random.randint(1,3)
                r3 = random.randint(1,3)
                element1 = random_element()
                element2 = random_element()
                element3 = random_element()
                print('\nYou are given a molecule containing ' + str(r1) + ' ' + element1.name + ', ' + str(r2) + ' ' + element2.name + ', and ' + str(r3) + ' ' + element3.name)
                print('\nWhat is the molar (atomic) mass of the molecule?\n')
                guess = input('Enter your answer as a decimal you have a margin of error of 0.5: ')
                
                if guess <= str(element1.atomic_mass*r1 + element2.atomic_mass*r2 + element3.atomic_mass*r3 + 0.5) and guess >= str(element1.atomic_mass*r1 + element2.atomic_mass*r2 + element3.atomic_mass*r3 - 0.5):
                    print('\nYou are Correct! The answer was : ' + str(element1.atomic_mass*r1 + element2.atomic_mass*r2 + element3.atomic_mass*r3) + ' Au')
                    u_input = input("Enter the number representing the game you would like to play or type 'Leave': ")
                
                else:
                    print('You are Incorrect. The answer was : ' + str(element1.atomic_mass*r1 + element2.atomic_mass*r2 + element3.atomic_mass*r3) + ' Au')
                    u_input = input("Enter the number representing the game you would like to play or type 'Leave': ")
                
            if u_input == '6':
                element = random_element()
                print('\nYou are given the element ' + element.symbol + ' , ' + element.name + ' write the electron configuration for that element')
                guess = input("Enter your answer seperated by spaces and do not use carrots noble gas configuration is allowed : ")
                if '[' in guess:
                    if (game_5e(guess) + guess[len(game_5e(guess)) + 1:-1]) in game_5(element):
                        print('\nYou are Correct!')
                        u_input = input("Enter the number representing the game you would like to play or type 'Leave': ")
                    else:
                        print('\nYou are incorrect. The correct answer was : ' + game_5(element))
                        u_input = input("Enter the number representing the game you would like to play or type 'Leave': ")
                else:
                    if guess == game_5(element):
                        print('\nYou are correct!')
                    else:
                        print('\nYou are incorrect. The correct answer was : ' + game_5(element))
                        u_input = input("Enter the number representing the game you would like to play or type 'Leave': ")
            
            else:
                print('Unkown Command')
                u_input = input("Enter the number representing the game you would like to play or type 'Leave': ")
    
    print('\nThanks for playing have a nice day :]')
                    
play_game()   