import pygame

class Doodle():
	"""settings for doodle placement"""
	def __init__(self, settings, screen):
		self.screen = screen # need doodle.screen in order to reference/use the original screen
		self.settings = settings

		self.image = pygame.image.load('images/doodlebob.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect() 

		# set position for doodlebob
		self.rect.centerx = self.screen_rect.centerx # these are part of the API
		self.rect.bottom = self.screen_rect.bottom

		# Decimal value for doodle.rect, since it is currently stored as integer
		self.center = float(self.rect.centerx)

		# Set moving flags as False
		self.moving_right = False
		self.moving_left = False


	def update(self):
		"""update movement of Doodlebob based on moving flags"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.settings.doodle_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.settings.doodle_speed_factor

		# Update the position of the ship
		self.rect.centerx = self.center


	def blitme(self):
		"""Draw doodle at current position"""
		self.screen.blit(self.image, self.rect)


	def center_doodle(self):
		"""Center doodle at bottom of screen"""
		self.center = self.screen_rect.centerx