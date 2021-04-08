class Settings:
    """A class to store all setting for the example game"""

    def __init__(self):
        """Initialize the game settings"""
        # screen settings
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (52,210,235)
        # car settings
        self.car_speed_factor = 0.5
        # bullet
        self.bullet_speed_factor = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 64, 64, 64
        self.bullets_allowed = 3