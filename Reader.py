empire = "Combat Probability Calculator\\Unit Stats\\Empire.txt"
woc = "Combat Probability Calculator\\Unit Stats\\WoC.txt"
ong = "Combat Probability Calculator\\Unit Stats\\OnG.txt"
he = "Combat Probability Calculator\\Unit Stats\\HE.txt"
bret = "Combat Probability Calculator\\Unit Stats\\Bret.txt"
dwarf = "Combat Probability Calculator\\Unit Stats\\Dwarf.txt"
factions = [empire, woc, ong, he, bret, dwarf]

for faction in factions:
    f = open(faction, "r")
    print(f.read())
    print("")