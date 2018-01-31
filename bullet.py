import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""construct a bullet to be fired from the ship"""
	
	def __init__(self, settings, screen, doodle):
		"""bullet to be fired from Doodlebob's current location"""
		super().__init__()
		self.screen = screen

		# Create bullet at (0, 0) and then set its correct position
		self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
		self.rect.centerx = doodle.rect.centerx
		self.rect.top = doodle.rect.top

		# Store height position as a float
		self.y = float(self.rect.y)

		self.color = settings.bullet_color
		self.speed_factor = settings.bullet_speed_factor

	def update(self):
		# make the bullet travel upward
		self.y -= self.speed_factor
		# Now update self.rect.y
		self.rect.y = self.y

	def draw_bullet(self):
		# Draw the bullet to the screen
		pygame.draw.rect(self.screen, self.color, self.rect)