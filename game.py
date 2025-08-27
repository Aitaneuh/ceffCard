from card import Card
from deck import Deck
from player import Player
import random

class Game:
    def __init__(self, players: list[Player]) -> None:
        self.players = players
        self.stack = []
        self.deck = Deck()

    def play_one_game(self):
        self.deck.shuffle()
        self.deal_cards()
        random.shuffle(self.players)
        play_count = 0
        while True:
            play_count += 1
            for player in self.players:
                res = player.play(self.stack)
                if res == "cant":
                    player.hand.append(self.stack)
                    self.stack = []
                else:
                    self.stack.append(res)

                if player.hand == [] and player.top_cards == [] and player.hidden_cards == []:
                    self.players.remove(player)
            if len(self.players) < 2:
                break

    
    def deal_cards(self) -> None:
        player_count = len(self.players)
        if player_count <= 4:
            table_cards_count = 5
        elif player_count == 5:
            table_cards_count = 4
        elif player_count == 6:
            table_cards_count = 3
        else:
            table_cards_count = 2

        for player in self.players:
            player.hand.append(self.deck.draw(3))
            player.hidden_cards.append(self.deck.draw(table_cards_count))
            player.top_cards.append(self.deck.draw(table_cards_count))