import pygame.font

class Button():
	def __init__(self, settings, screen, msg):
		"""Initialize Button attributes"""
		self.screen = screen
		self.screen_rect = screen.get_rect()

		# Attributes of the Button
		self.width, self.height = 200, 50
		self.button_color = (0, 250, 0)
		self.text_color = (250, 250, 250)
		self.font = pygame.font.SysFont(None, 48)

		# Build the button and center it
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		self.prep_msg(msg)


	def prep_msg(self, msg):
		"""Turn msg into a rendered image and center text on the button"""
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center


	def draw_button(self):
		"""Draw blank button and draw image to it"""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)