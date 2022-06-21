import random

class card:
    def __init__(self):
        """card: the card job is to generate two cards that can be used by the director to facilitate the hilo game
    
    

    Attributes:
        card_num: card number randomly generated
    """
        self.card_num = 0

    def draw_1(self):
        """Determines whether or not the Player has received cards.
        
        Args:
            self (card): instance of card
        """
        
        if self.card_num == 0:
            self.card_num += 1
            return True

        else:
            self.card_num += 1
            return False   

    def draw(self):
        """Chooses a random number. 
        Args: 
            self (card): An instance of card.
        """
        card = random.randint(1, 14)
        return card