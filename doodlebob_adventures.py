import pygame, sys
from pygame.sprite import Group

from doodlebob import Doodle
from doodle_settings import Settings
import doodle_functions as df 
from game_stats import GameStats 
from button import Button


def run_game():
	"""function that will run the game"""
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode(
		(settings.screen_width, settings.screen_height))
	pygame.display.set_caption('Doodlebob Adventures')
	
	
	# Create instances of Doodlebob, a group of bullets, and a squad of Kims
	doodle = Doodle(settings, screen)
	bullets = Group()
	kim_squad = Group()

	df.create_squad(settings, screen, doodle, kim_squad)
	
	# Create an instance of GameStats
	stats = GameStats(settings)

	#Create play button
	play_button = Button(settings, screen, 'Play')


	while True:
		df.check_events(settings, screen, doodle, kim_squad, bullets, stats, play_button)

		if stats.game_active == True:
			doodle.update()
			df.update_bullets(settings, screen, doodle, kim_squad, bullets)
			df.update_squad(settings, screen, doodle, kim_squad, bullets, stats)
			
		df.update_screen(settings, screen, doodle, kim_squad, bullets, stats, play_button)

run_game()


