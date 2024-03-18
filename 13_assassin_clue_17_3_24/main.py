from game import AssassinClueGame

def main():
    players_number = int(input("enter the game players number please:\n"))
    assassin_clue_game = AssassinClueGame(players_number=players_number)
    assassin_clue_game.game_start()
    
    
if __name__ == "__main__":
    main()