class GameStats():
	"""Track Stats within Doodlebob Adventures"""

	def __init__(self, settings):
		"""Runs for entirety of game session"""
		self.settings = settings
		self.reset_stats()

		# Game starts in inactive state until 'Start' is pressed
		self.game_active = False

	def reset_stats(self):
		"""Statistics that can change during the game"""
		self.lives_left = self.settings.life_limit

