# Foster Cavender
# CS1400 online 7 week

import pygame
from player import Player
from treasure import Treasure
from enemy import Enemy

SCREEN_WIDTH = 600  # Use constants here to be able to use in different places
SCREEN_HEIGHT = 600
CLOCK_TICK = 30
TITLE = "Extreme Apple Hunter"


def main():
    # Setup the pygame window and clock
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    # Set up game media images, sound
    player_image = pygame.image.load("./assets/boar.png")
    enemy_image = pygame.image.load("./assets/enemy.png")
    treasure_image = pygame.image.load("./assets/apple.png")
    background_image = pygame.image.load("./assets/grass_background.png")

    collect_sound = pygame.mixer.Sound("./assets/collect.mp3")
    splat_sound = pygame.mixer.Sound("./assets/splat.mp3")
    end_sound = pygame.mixer.Sound("./assets/game_win.mp3")
    lose_sound = pygame.mixer.Sound("./assets/game_loss.mp3")
    pygame.mixer.music.load("./assets/background_music.mp3")
    pygame.mixer.music.play(-1)

    font = pygame.font.SysFont(None, 48)
    game_lose = font.render("You Lose!", True, "red")
    game_win = font.render("Congrats! You Win!", True, "purple")

    # create objects used in game
    player = Player(player_image)
    enemy = Enemy(enemy_image)
    treasure_list = []
    for x in range(0, 10):
        treasure_list.append(Treasure(treasure_image))

    # constants for movement
    PLAYER_SPEED = 5
    ENEMY_SPEED = 10

    # function for detecting object collisions
    def did_touch(item1, item2):
        distance_x = abs(item1.center_x - item2.center_x)
        distance_y = abs(item1.center_y - item2.center_y)
        combined_radius = item1.radius + item2.radius
        if distance_x < combined_radius and distance_y < combined_radius:
            return True
        return False

    # Game Loop
    game_over = False
    running = True
    win = True
    while running:
        ##########
        # Get Input/Events
        ##########
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # User clicked the window's X button
                running = False

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_SPACE] and game_over:
            ### Do Stuff to Reset Game ###
            game_over = False

            # reset player / enemy positions
            player.reset()
            enemy.reset()

            # create new treasure objects
            treasure_list = []
            for x in range(0, 10):
                treasure_list.append(Treasure(treasure_image))

            # restart music
            pygame.mixer.music.load("./assets/background_music.mp3")
            pygame.mixer.music.play(-1)

        ##########
        # Update state of components/data
        ##########

        #### Update if Game is Not Over ####
        if not game_over:
            ### In this block of code game_over = True will happen ###
            if did_touch(player, enemy):
                game_over = True
                pygame.mixer.Sound.play(lose_sound)
                win = False
            else:
                for x in range(0, len(treasure_list)):
                    if did_touch(player, treasure_list[x - 1]):
                        treasure_list.pop(x - 1)
                        pygame.mixer.Sound.play(collect_sound)
                        if len(treasure_list) == 0:
                            game_over = True
                            pygame.mixer.Sound.play(end_sound)
                            win = True

            ##########
            # movement control
            ##########

            # player movement
            if pressed[pygame.K_UP]:
                player.move_player([0, -PLAYER_SPEED])
            if pressed[pygame.K_DOWN]:
                player.move_player([0, PLAYER_SPEED])
            if pressed[pygame.K_LEFT]:
                player.move_player([-PLAYER_SPEED, 0])
            if pressed[pygame.K_RIGHT]:
                player.move_player([PLAYER_SPEED, 0])

            # enemy movement
            if enemy.move_enemy():
                pygame.mixer.Sound.play(splat_sound)

        #### Update if Game is Over ####
        else:
            pygame.mixer.music.stop()

        ##########
        # Update Display
        ##########

        #### Always Display ####
        screen.blit(background_image, (0, 0))

        #### Display while Game is being played ####
        if not game_over:
            for x in range(0, len(treasure_list)):
                screen.blit(treasure_list[x].image, (treasure_list[x].draw_x, treasure_list[x].draw_y))

            screen.blit(player.image, (player.draw_x, player.draw_y))
            screen.blit(enemy.image, (enemy.draw_x, enemy.draw_y))

        #### Display while Game is Over ####
        else:
            if win:
                screen.blit(game_win, (300 - game_win.get_width() / 2, 300 - game_win.get_height() / 2))
            else:
                screen.blit(game_lose, (300 - game_lose.get_width() / 2, 300 - game_lose.get_height() / 2))

        #### Draw changes the screen ####
        pygame.display.flip()

        #### Define the refresh rate of the screen ####
        clock.tick(CLOCK_TICK)


main()
