import Unit

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

def MathsToSave(attacker, defender, wounds):
        # placeholder for implementation of Ap
        modifiers = 0
        save = defender.save + modifiers
        if (save >= 7 ):
            toSave = 0/6
        else:
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
        print(save,"+ to save")
        saved = wounds * toSave
        unsaved = wounds - saved
        return (unsaved)

#basic "container" function, loops combat between units until one dies, then announces winner
def Combat(unit1, unit2):
     print (unit2.name, " has ", unit2.wounds, "wounds remaining")
     print (unit1.name, " has ", unit1.wounds, "wounds remaining")  
     while (unit1.wounds > 0 and unit2.wounds > 0):
            if (unit1.initiative > unit2.initiative):
                    unit2.wounds = unit2.wounds - CalculateWounds(unit1, unit2)
                    print (unit2.name, " has ", unit2.wounds, "wounds remaining")
                    if (unit2.wounds >0):
                       unit1.wounds = unit1.wounds - CalculateWounds(unit2, unit1)
                       print (unit1.name, " has ", unit1.wounds, "wounds remaining")  
            elif(unit2.initiative > unit1.initiative):
                    unit1.wounds = unit1.wounds - CalculateWounds(unit2, unit1)
                    print (unit1.name, " has ", unit1.wounds, "wounds remaining") 
                    if (unit1.wounds >0):
                       unit2.wounds = unit2.wounds - CalculateWounds(unit1, unit2)
                       print (unit2.name, " has ", unit2.wounds, "wounds remaining")  
            else:
                unit2.wounds = unit2.wounds - CalculateWounds(unit1, unit2)
                print (unit2.name, " has ", unit2.wounds, "wounds remaining")
                unit1.wounds = unit1.wounds - CalculateWounds(unit2, unit1)   
                print (unit1.name, " has ", unit1.wounds, "wounds remaining")    
     if (unit1.wounds > 0 and unit2.wounds <=0):
          winner = unit1.name
     elif(unit1.wounds > 0 and unit2.wounds <=0):
          winner = unit2.name
     else:
          winner = "DRAW"
     print("winner is:", winner)


#container function for testing
def runtest():
     Unit1 = Unit.Unit("Unit1", 3, 3, 3, 3, 1, 2, 7, 5)
     Unit2 = Unit.Unit("Unit2", 4, 3, 4, 3, 1, 1, 7, 5)  
     Combat(Unit1, Unit2)

runtest()