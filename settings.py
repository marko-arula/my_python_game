class Settings:
    """A class to store all setting for the example game"""

    def __init__(self):
        """Initialize the game settings"""
        # screen settings
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (52,210,235)
        # car settings

        self.car_limit = 3
        # bullet

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 64, 64, 64
        self.bullets_allowed = 10
        # aliens setting

        self.fleet_drop_speed = 5
        # speed up factor
        self.speedup_scale = 1.1
        self.init_dynamic_scale()

    def init_dynamic_scale(self):
        self.car_speed_factor = 0.5
        self.bullet_speed_factor = 0.5
        self.alien_speed_factor = 0.5
        # fleet direction
        self.fleet_direction = 1

        # points for killing aliens
        self.alien_points = 50


    def increase_speed(self):
        self.car_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale