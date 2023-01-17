#!/usr/bin/env python3

# Created by: Kyanh Pham
# Created on: Jan 20223
# This program is the "DodgeBall" program on the PyBadge

import random
import time

import constants
import stage
import ugame


def splash_scene():
    # this function is the splash scene game loop

    # get sound ready
    coin_sound = open("coin.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    # an image bank for CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y
    )

    # create a stage for the background to show up on
    #  and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = [background]
    # render background
    game.render_block()

    while True:
        time.sleep(1.0)
        menu_scene()


def menu_scene():
    # This function is the main game game_scene

    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # add text objects
    text = []
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    # set the background to image 0 in the image bank
    background = stage.Grid(
        image_bank_background, constants.SCREEN_X, constants.SCREEN_Y
    )

    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    # create a stage for the background to show up on
    #  and set the frame rate to 60 fps
    game = stage.Stage(ugame.display, constants.FPS)

    # set the layers of all sprites, items show up in order
    game.layers = text + [background]

    game.render_block()

    # repeat forever, game loop
    while True:
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            game_scene()

        game.tick()


def game_scene():
    # This function is the main game game_scene

    # for score
    ball_count = 0
    score = 0

    score_text = stage.Text(
        width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))

    def show_ball():
        # this function takes an alien from off screen and moves it on screen
        for ball_number in range(len(balls)):
            if balls[ball_number].x < 0:
                balls[ball_number].move(
                    random.randint(
                        0 + constants.SPRITE_SIZE,
                        constants.SCREEN_X - constants.SPRITE_SIZE,
                    ),
                    constants.OFF_TOP_SCREEN,
                )
                break

    image_bank_background = stage.Bank.from_bmp16("dodgeball_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("dodgeball_sprite.bmp")

    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    player = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

    ball = stage.Sprite(
        image_bank_sprites,
        9,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )

    # create list of lasers for when we shoot
    balls = []
    for ball_number in range(constants.TOTAL_NUMBER_OF_BALLS):
        a_single_ball = stage.Sprite(
            image_bank_sprites, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        balls.append(a_single_ball)
    # place 1 alien on the screen
    show_ball()

    game = stage.Stage(ugame.display, 60)
    game.layers = [score_text] + [player] + balls + [background]
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            if player.x <= (constants.SCREEN_X - constants.SPRITE_SIZE):
                player.move((player.x + constants.SPRITE_MOVEMENT_SPEED), player.y)
            else:
                player.move((constants.SCREEN_X - constants.SPRITE_SIZE), player.y)

        if keys & ugame.K_LEFT:
            if player.x >= 0:
                player.move((player.x - constants.SPRITE_MOVEMENT_SPEED), player.y)
            else:
                player.move(0, player.y)
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass

            # each frame move the aliens down, that are on the screen
        for ball_number in range(len(balls)):
            if balls[ball_number].x > 0:
                balls[ball_number].move(
                    balls[ball_number].x,
                    balls[ball_number].y + constants.BALL_SPEED,
                )
                if balls[ball_number].y > constants.SCREEN_Y:
                    balls[ball_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )
                    show_ball()
                    show_ball()
                    show_ball()
                    score = score + 1
                    score_text.clear()
                    score_text.cursor(0, 0)
                    score_text.move(1, 1)
                    score_text.text("Score: {0}".format(score))

        game.render_sprites(balls + [player])
        game.tick()


if __name__ == "__main__":
    splash_scene()
