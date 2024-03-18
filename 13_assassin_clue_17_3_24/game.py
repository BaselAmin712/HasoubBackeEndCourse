import random
from player import Player

class AssassinClueGame:
    def __init__(self, players_number):
        self.players_number = players_number
        self.players = []
        self.losers = []
        self.places_names = [
            "Tokyo",
            "Paris",
            "London",
            "Berlin",
            "Rome",
            "Moscow",
            "New Delhi",
            "Seoul",
            "Mexico City",
            "Cairo",
            "Athens",
            "Bangkok",
            "Dublin",
            "Madrid",
            "Stockholm",
            "Oslo",
            "Abu Dhabi",
            "Helsinki",
            "Buenos Aires",
            "Washington, D.C."
        ]
        self.weapons = [
            "Sword",
            "Bow and Arrow",
            "Dagger",
            "Crossbow",
            "Spear",
            "Axe",
            "Rifle",
            "Shotgun",
            "Pistol",
            "Flail"
        ]
        self.assassin :Player = None
    
    def game_start(self):
        self.create_players(self.players_number)
        self.pick_assassin()
        self.game_run


    def edit_player_last_places_randomly(self):
        pass

    def create_players(players_number):
        pass

    def pick_assassin(self):
        self.assassin = self.players[random.randint(0, self.players_number)]
        self.assassin.assassin = True

    def game_run(self):
        pass