class Player:
    def __init__(self, name):
        self.name = name
        self. last_visited_places = []
        self.favorite_weapons = []
        self.assassin = False

    def add_weapon(self, weapon):
        self.favorite_weapons.append(weapon)

    def add_place(self, place):
        self.last_visited_places.append(place)

    def delete_All_places(self):
        self.last_visited_places = []