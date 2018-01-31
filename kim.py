import pygame
from pygame.sprite import Sprite 

class Kim(Sprite):
	"""Create an instance of Kim Jong Un"""

	def __init__(self, settings, screen):
		"""Initialize Kim and starting position"""
		super(Kim, self).__init__()
		self.screen = screen
		self.settings = settings

		# Load image and set rect
		self.image = pygame.image.load('images/kim.bmp')
		self.rect = self.image.get_rect()

		# Each Kim starts at the top left of the screen, with its own width and height in distance from corner
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store exact location
		self.x = float(self.rect.x)

		
	def blitme(self):
		"""Draw Kim at current location"""
		self.screen.blit(self.image, self.rect)

	
	def update(self):
		"""Move kim to the right"""
		# This can be applied to a Group()
		# Do I not have to make settings a parameter because its already defined in the class?
		self.x += (self.settings.kim_speed_factor * self.settings.squad_direction)
		self.rect.x = self.x

	
	def check_edges(self):
		"""Check if fleet is touching screen edge"""
		screen_rect = self.screen.get_rect()  # Create an instance of the screen rect in order to refer to it
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True


