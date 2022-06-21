from game.Cards import card

class Director:

    def __init__(self):
        """Director: A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card (Cards): cards drawn
        is_playing (boolean): Whether or not the game is being played.
        total_score (int): The score for the game.
    """
        
        self.total_score = 300
        self.card = card()
        self.draw_1 = 0
        self.draw_2 = 0
        self.is_playing = True


    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            if self.is_playing:
                self.get_cards()
                self.check_score()
                self.do_outputs()

    def get_inputs(self):
        """The user decides whether or not they want to play again.
        Args:
        self (Director): An instance of Director.
        """
        play_again = input('Play again? [y/n] ')
        self.is_playing = (play_again == "y")
        if play_again == "n":
            print("Go enjoy your money!")
            print(f"You earned ${self.total_score}!!")

    def higher_or_lower(self):
        """Runs each card through the function to check if it is higher or lower 
        than the previous card. Updates score accordingly.
        Args:
            self (Director): An instance of Director.
        """
        guess_input = input("Higher or Lower? [h/l] ")
        if self.draw_1 < self.draw_2 and guess_input == 'h':
            self.total_score += 100
        elif self.draw_1 > self.draw_2 and guess_input == 'l':
            self.total_score +=100
        else:
            self.total_score -= 75


    def check_score(self):
        """Checks the player score to be sure it is over 0.

        Args:
            self (Director): An instance of Director.
        """
        print(f'The card is: {self.draw_1}')
        self.higher_or_lower()
        if self.total_score <= 0:
            self.total_score = 0 
            self.is_playing = False


    def do_outputs(self):
        """Displays the second card and the score. 

        Args:
            self (Director): An instance of Director.
        """
        print(f"Next card was: {self.draw_2}")
        print(f"Your score is: {self.total_score}")
        if self.is_playing == False:
            print("You're broke. Go spend more money please!")
            
    def get_cards(self):
        """Runs the draw function from cards and stores the output as variables. 

        Args:
            self (Director): An instance of Director.
        """
        self.draw_1 = card.draw(self)
        self.draw_2 = card.draw(self)