class Settings():
	"""Screen settings, for now"""
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (0, 30, 60)

		# Bullet Settings
		self.bullet_width = 500
		self.bullet_height = 15
		self.bullet_color = (0, 250, 0)
		self.bullets_allowed = 3

		# Kim Jong Un Settings
		self.kim_drop_factor = 30
		
		# Stat Settings
		self.life_limit = 2

		# Level-Up Settings for Game Speed
		self.speedup_factor = 1.5

		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		"""Settings that change throughout the game"""
		self.doodle_speed_factor = 8
		self.bullet_speed_factor = 15
		self.kim_speed_factor = 5

		# Direction factor: 1 is right, -1 is left
		self.squad_direction = 1


	def speed_up(self):
		"""Speed up the game when level-up"""
		self.doodle_speed_factor *= self.speedup_factor
		self.bullet_speed_factor *= self.speedup_factor
		self.kim_speed_factor *= self.speedup_factor
