from card import Card

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.hand = []
        self.top_cards = []
        self.hidden_cards = []

    def play(self, card_stack: list[Card]) -> Card | str:
       last_stack_card = card_stack[-1]
       return "to be continued"
