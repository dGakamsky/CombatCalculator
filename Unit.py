class Unit:
    def __init__(self, name, ws, strength, toughness, initiative, wounds, attacks, leadership, armor, ward, regen, cost):
        self.name = name
        self.ws = ws
        self.strength = strength
        self.toughness = toughness
        self.initiative = initiative
        self.maxwounds = wounds
        self.currentwounds = wounds
        self.attacks = attacks
        self.leadership = leadership
        self.armor = armor
        self.ward = ward
        self.regen = regen
        self.points = cost