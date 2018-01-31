import pygame, sys

from time import sleep

from kim import Kim
from bullet import Bullet


def check_events(settings, screen, doodle, kim_squad, bullets, stats, play_button):
	"""Detects keyboard and mouse movements"""
	for event in pygame.event.get():
		if stats.game_active == False:
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				
				# Check if the Play Button was clicked
				check_play_button(settings, screen, doodle, kim_squad,
					bullets, stats, play_button, mouse_x, mouse_y)

				# Set initial game settings
				settings.initialize_dynamic_settings()

				# Make the mouse invisible once the play button is pressed
				pygame.mouse.set_visible(False)

			# Check if 'q' was pressed in order to quit
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
				sys.exit()
		
		elif event.type == pygame.QUIT:
			sys.exit()
		
		elif stats.game_active == True:
			if event.type == pygame.KEYDOWN:
				check_keydown(event, settings, screen, doodle, bullets)
		
			elif event.type == pygame.KEYUP:
				check_keyup(event, doodle)


def check_keydown(event, settings, screen, doodle, bullets):
	"""Keydown event"""
	
	if event.key == pygame.K_RIGHT:
		doodle.moving_right = True
	elif event.key == pygame.K_LEFT:
		doodle.moving_left = True	
	elif event.key == pygame.K_SPACE:
		if len(bullets) < settings.bullets_allowed:
			new_bullet = Bullet(settings, screen, doodle)
			bullets.add(new_bullet)	
	elif event.key == pygame.K_q:
		sys.exit()


def check_keyup(event, doodle):	
	"""Keyup event"""
	
	if event.key == pygame.K_RIGHT:
		doodle.moving_right = False
	elif event.key == pygame.K_LEFT:
		doodle.moving_left = False


def check_play_button(settings, screen, doodle, kim_squad, bullets,
	stats, play_button, mouse_x, mouse_y):
	"""Reset stats and instances in order to start a new game"""
	if play_button.rect.collidepoint(mouse_x, mouse_y):
		stats.reset_stats()
		stats.game_active = True

		reset_game(settings, screen, doodle, kim_squad, bullets)


def update_screen(settings, screen, doodle, kim_squad, bullets,
	stats, play_button):
		screen.fill(settings.bg_color)

		if stats.game_active == True:
		# Redraw all bullets behind ship and aliens
			for bullet in bullets.sprites():
				bullet.draw_bullet()

		doodle.blitme()
		kim_squad.draw(screen)

		if not stats.game_active:
			play_button.draw_button()

		# Show the most recently drawn screen
		pygame.display.flip()


def update_bullets(settings, screen, doodle, kim_squad, bullets):
	"""update position of bullets and delete when off screen"""
	bullets.update()

	# Get rid of bullets that exit the screen
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	check_collision(settings, screen, doodle, kim_squad, bullets)
	

def check_collision(settings, screen, doodle, kim_squad, bullets):
	# Check for bullets that have collided with a Kim, delete both if True
	collisions = pygame.sprite.groupcollide(bullets, kim_squad, True, True)

	# Check if all the Kims are eliminated, create new squad and speed_up if True
	if len(kim_squad) == 0:
		bullets.empty()
		settings.speed_up()
		create_squad(settings, screen, doodle, kim_squad)


def get_squad_number_x(settings, kim_width):
	# Create an alien to calculate the number of aliens in a squad
	# One full kim width between each kim
	available_space_x = settings.screen_width - (2 * kim_width)
	kim_squad_size =  int(available_space_x / (2.2 * kim_width))

	return kim_squad_size


def get_squad_rows(settings, doodle_height, kim_height):
	# Number of rows of kims
	available_space_y = (settings.screen_height - (3 * kim_height)
		- doodle_height)
	squad_rows = int(available_space_y / (1.5 * kim_height))

	return squad_rows


def create_kim(settings, screen, kim_squad, kim_number, row_number):
	"""Create a kim to place in row"""
	kim = Kim(settings, screen)
	kim_height = kim.rect.height
	kim.x = kim.rect.width + (2 * kim.rect.width * kim_number)
	kim.rect.x = kim.x
	kim.rect.y = kim.rect.height + (2 * kim.rect.height * row_number)
	kim_squad.add(kim)


def create_squad(settings, screen, doodle, kim_squad):
	"""Fully yeeted squad of kims"""
	kim = Kim(settings, screen)

	kim_squad_size = get_squad_number_x(settings, kim.rect.width)
	squad_rows = get_squad_rows(settings,
		doodle.rect.height, doodle.rect.height)

	# create the squad
	for row in range(squad_rows):
		for kim_number in range(kim_squad_size):
			create_kim(settings, screen, kim_squad, kim_number, row)
	

def update_squad(settings, screen, doodle, kim_squad, bullets, stats):
	"""Update positions of full squadron"""
	check_squad_edges(settings, kim_squad)

	kim_squad.update()

	"""call doodle_hit() when collision occurs"""
	if pygame.sprite.spritecollideany(doodle, kim_squad):
		doodle_hit(settings, screen, doodle, kim_squad, bullets, stats)

	check_squad_bottom(settings, screen, doodle, kim_squad, bullets, stats)


def check_squad_edges(settings, kim_squad):
	"""Run check_edges, and change direction if True"""
	for kim in kim_squad.sprites(): # Don't really understand the sprites concept
		if kim.check_edges():
			change_direction(settings, kim_squad)
			break


def check_squad_bottom(settings, screen, doodle, kim_squad, bullets, stats):
	"""Check if squad hits the bottom"""
	screen_rect = screen.get_rect()

	for kim in kim_squad.sprites():
		if kim.rect.bottom >= screen_rect.bottom:
			doodle_hit(settings, screen, doodle, kim_squad, bullets, stats)


def change_direction(settings, kim_squad):
	"""Drop the squad and change settings.squad_direction"""
	for kim in kim_squad.sprites():
		kim.rect.y += settings.kim_drop_factor

	settings.squad_direction *= (-1)


def doodle_hit(settings, screen, doodle, kim_squad, bullets, stats):
	"""Actions taken at Doodle collision"""
	# Check if lives remain
	if stats.lives_left > 0:
		# Lose life
		stats.lives_left -= 1

		reset_game(settings, screen, doodle, kim_squad, bullets)

	else:
		stats.game_active = False

		# Reset mouse visibility
		pygame.mouse.set_visible(True)


def reset_game(settings, screen, doodle, kim_squad, bullets):
	"""Reset the game after start is pressed, or a life is lost"""
	# Empty Bullets and Kims, Reposition Doodle
	bullets.empty()
	kim_squad.empty()
	doodle.center_doodle()

	# Create New Squad
	create_squad(settings, screen, doodle, kim_squad)

	# Pause game
	sleep(.5)

