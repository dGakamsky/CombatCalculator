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
    wounds_after_armor = ArmorSave(attacker, defender, wounds)
    wounds_after_ward = WardSave(attacker, defender, wounds_after_armor)
    wounds_after_regen = RegenSave(attacker, defender, wounds_after_armor)
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
def Combat(unit1, unit2):
     print (unit2.name, " has ", unit2.wounds, "wounds remaining")
     print (unit1.name, " has ", unit1.wounds, "wounds remaining") 

     #does the initiative steps
    
     init1 = unit1.initiative
     init2 = unit1.initiative
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


#container function for testing
def runtest():
     Unit1 = Unit.Unit("Unit1", 3, 3, 3, 3, 1, 2, 7, 5, 7, 7)
     Unit2 = Unit.Unit("Unit2", 4, 3, 4, 3, 1, 1, 7, 5, 7, 7)  
     Combat(Unit1, Unit2)

runtest()