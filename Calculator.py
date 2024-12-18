import Unit
import tkinter as tk
from tkinter import *
from tkinter.simpledialog import askstring
from tkinter import ttk
import sys
from tkinter import *



def CalculateHits(attacker, defender):
        hits = attacker.attacks * MathsToHit(attacker, defender)
        print(hits, "hits caused")
        return (hits)
    
def MathsToHit(attacker, defender):
        AWS = attacker.ws
        print ("attacker WS is: ", AWS)
        DWS = defender.ws
        print ("defender WS is: ", DWS)
        if (AWS>DWS):
            if (AWS>=(DWS*2+1)):
                toHit = 5/6
            else:
                toHit = 4/6
        elif (AWS*2+1<=DWS):
            toHit = 2/6
        else:
            toHit = 3/6
        print("the attacker hits: ", toHit, " of the time")
        return (toHit)

def CalculateWounds(attacker, defender):
        hits = CalculateHits(attacker, defender)
        wounds = MathsToWound(attacker, defender, hits)
        unsavedWounds = MathsToSave(attacker, defender, wounds)
        print(unsavedWounds, "wounds caused")
        return (unsavedWounds)

#currently only does base strength vs toughness
def MathsToWound(attacker, defender, hits):
        
        strength = attacker.strength
        print("attacker S is: ", strength)
        toughness = defender.toughness
        print("defender T is: ", toughness)
        if (strength>toughness):
            if (strength>=toughness+2):
                toWound = 5/6
            else:
                toWound = 4/6
        elif (strength<toughness):
            if (strength<=toughness-2):
                toWound = 1/6
            else: 
                toWound = 2/6  
        else:
            toWound = 3/6    
        print("the attacker wounds: ", toWound, " of the time")
        wounds = hits * toWound
        return (wounds)

# currently only does armor saves
def MathsToSave(attacker, defender, wounds):
    #saves stack and are done one after the other
    wounds_after_armor = ArmorSave(attacker, defender, wounds)
    wounds_after_ward = WardSave(attacker, defender, wounds_after_armor)
    wounds_after_regen = RegenSave(attacker, defender, wounds_after_ward)
    return (wounds_after_regen)

def ArmorSave(attacker, defender, wounds):
        # placeholder for implementation of Ap
        modifiers = 0
        save = defender.armor + modifiers
        #if the AP negates a save entirely
        if (save >= 7 ):
            toSave = 0/6
        else:
            #if not for case(1) save could be "7-(save)/6"
            #matches save value to necessary result
            match save:
                    case 6:
                        toSave = 1/6
                    case 5:
                        toSave = 2/6
                    case 4:
                        toSave = 3/6
                    case 3:
                        toSave = 2/6
                    case 2:
                        toSave = 5/6
                    case 1:
                        toSave = 5/6
            print(save,"+ to save via armor")
        saved = wounds * toSave
        unsaved = wounds - saved
        return (unsaved)

def WardSave(attacker, defender, wounds):
        # placeholder for implementation of Ap
        modifiers = 0
        save = defender.ward + modifiers
        if (save >= 7 ):
            toSave = 0/6
        else:
            #if not for case(1) save could be "7-(save)/6"
            #matches save value to necessary result
            match save:
                    case 6:
                        toSave = 1/6
                    case 5:
                        toSave = 2/6
                    case 4:
                        toSave = 3/6
                    case 3:
                        toSave = 2/6
                    case 2:
                        toSave = 5/6
                    case 1:
                        toSave = 5/6
            print(save,"+ to save via ward")
        saved = wounds * toSave
        unsaved = wounds - saved
        return (unsaved)

def RegenSave(attacker, defender, wounds):
        # placeholder for implementation of Ap
        modifiers = 0
        save = defender.regen + modifiers
        #if the AP negates a save entirely
        if (save >= 7 ):
            toSave = 0/6
        else:
            #if not for case(1) save could be "7-(save)/6"
            #matches save value to necessary result
            match save:
                    case 6:
                        toSave = 1/6
                    case 5:
                        toSave = 2/6
                    case 4:
                        toSave = 3/6
                    case 3:
                        toSave = 2/6
                    case 2:
                        toSave = 5/6
                    case 1:
                        toSave = 5/6
            print(save,"+ to save via regeneration")
        saved = wounds * toSave
        unsaved = wounds - saved
        return (unsaved)

     #TODO factor in mounts/multiple combatants (likely its own method, later)
     #TODO factor in combat rounds, since some rules depend on it
     #TODO determine winner via generated combat resolution 
     #TODO impact hits/stomps, charging

#basic "container" function, loops combat between units until one dies, then announces winner
#currently only works for 1v1
def Combat(unit1, unit2, charger):
     print (unit2.name, " has ", unit2.wounds, "wounds remaining")
     print (unit1.name, " has ", unit1.wounds, "wounds remaining") 

     #does the initiative steps

     charging_unit = charger
     if charger == unit1:
        defending_unit = unit2
     else:
        defending_unit = unit1
    
     init1 = charging_unit.initiative
     init2 = defending_unit.initiative
     #defauls to 3 for now, will be set to a dynamic variable later (such as for rear charges)
     charge_bonus = 3
     round = 1
     #combat only occurs while both parties are alive
     while (unit1.wounds > 0 and unit2.wounds > 0):
        #unit 1 is assumed to charge

            if (round == 1):
                    init1 += charge_bonus
            else:
                    init1 = unit1.initiative

            if (init1 > init2):
                    unit2.wounds = unit2.wounds - CalculateWounds(unit1, unit2)
                    print (unit2.name, " has ", unit2.wounds, "wounds remaining")
                    if (unit2.wounds >0):
                       unit1.wounds = unit1.wounds - CalculateWounds(unit2, unit1)
                       print (unit1.name, " has ", unit1.wounds, "wounds remaining") 
                    round+=1  
            elif(init2 > init1):
                    unit1.wounds = unit1.wounds - CalculateWounds(unit2, unit1)
                    print (unit1.name, " has ", unit1.wounds, "wounds remaining") 
                    if (unit1.wounds >0):
                       unit2.wounds = unit2.wounds - CalculateWounds(unit1, unit2)
                       print (unit2.name, " has ", unit2.wounds, "wounds remaining") 
                    round+=1 
 
            else:
                unit2.wounds = unit2.wounds - CalculateWounds(unit1, unit2)
                print (unit2.name, " has ", unit2.wounds, "wounds remaining")
                unit1.wounds = unit1.wounds - CalculateWounds(unit2, unit1)   
                print (unit1.name, " has ", unit1.wounds, "wounds remaining")   
                round+=1 


     if (unit1.wounds > 0 and unit2.wounds <=0):
          winner = unit1.name
     elif(unit1.wounds > 0 and unit2.wounds <=0):
          winner = unit2.name
     else:
          winner = "DRAW"
     print("winner is:", winner)







#GUI section
window=tk.Tk()

window.title('Calculator')
window.geometry("1000x1100")

#container for central features
overframe = Frame(window)
overframe.pack(side = TOP)



#frames for temp unit entry


#list of units, to be replaced with a generated list eventually
Unit1 = Unit.Unit("Unit1", 3, 3, 3, 3, 1, 2, 7, 5, 7, 7)
Unit2 = Unit.Unit("Unit2", 4, 3, 4, 3, 1, 1, 7, 5, 7, 7) 
Unit3 = Unit.Unit("Unit3", 7, 3, 2, 3, 1, 1, 7, 5, 7, 7)   
units = [Unit1, Unit2, Unit3]
#creates a list of unit names which maps onto the list of units
unit_names = []
for unit in units:
    unit_names.append(unit.name)
#since the list of unit names maps onto the list of units, this allows for the selection of a unit from the list of unit names

def unit_1_select(self):
    chosen_unit = units[unit_names.index(clicked.get())]
    label1.config( text = chosen_unit.name) 
    print(chosen_unit.name)
    global selected_unit_1
    selected_unit_1 = chosen_unit

def unit_2_select(self):
    chosen_unit = units[unit_names.index(clicked2.get())]
    label2.config( text = chosen_unit.name) 
    print(chosen_unit.name)
    global selected_unit_2 
    selected_unit_2 = chosen_unit


#Frame1
frame1 = Frame(overframe, bg= "red", borderwidth=30, padx=10, pady=10)
frame1.pack(side = LEFT)
#selector 1
clicked = StringVar() 
clicked.set(unit_names[0]) 
drop = OptionMenu(frame1, clicked , *unit_names ) 
drop.pack()
label1 = Label(frame1 , text = " " )
label1.pack()
button = Button(frame1 , text = "Select unit 1")
button.pack()  
button.bind('<Button-1>', unit_1_select)

#Frame2
frame2 = Frame(overframe, bg= "blue", borderwidth=30, padx=10, pady=10)
frame2.pack(side = LEFT)

#selector 2
clicked2 = StringVar() 
clicked2.set(unit_names[0]) 
drop = OptionMenu(frame2, clicked2 , *unit_names ) 
drop.pack() 
label2 = Label(frame2 , text = " " )
label2.pack()
button2 = Button(frame2 , text = "Select unit 2" )
button2.pack() 
button2.bind('<Button-1>', unit_2_select)


#frame for output
frame3 = Frame(overframe, bg="grey", borderwidth=30, padx=10, pady=10)
frame3.pack(side = LEFT)

#frame for control buttons
frame4 = Frame(window)
frame4.pack(side = BOTTOM)


#container function for testing
def runtest(self):
     Combat(selected_unit_1, selected_unit_2, Unit1)

#button to run combat
cbtn=Button(frame4, text="run combat")
cbtn.bind('<Button-1>', runtest)
cbtn.place(relx=50, rely=50)
cbtn.pack()

#where the combat log will be printed
output_text = tk.Text(frame3, bg="black", fg="white", height=70, width=40)
output_text.pack()

#prints the combat log to an output in the UI
def print_to_text_widget(*args, **kwargs):
    text = " ".join(map(str, args)) #+ "\n"
    output_text.insert(tk.END, text)
    output_text.see(tk.END) 

#redirects printing to the UI
sys.stdout.write = print_to_text_widget




window.mainloop()