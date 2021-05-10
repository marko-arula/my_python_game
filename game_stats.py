class GameStats():
    """Game Stats"""
    def __init__(self, game_settings):
        """Initialize statistics"""
        self.game_settings = game_settings
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics, change during the game"""
        self.cars_left = self.game_settings.car_limit
        self.score = 0

