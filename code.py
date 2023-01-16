#!/usr/bin/env python3

# Created by: Kyanh Pham
# Created on: Jan 20223
# This program is the "DodgeBall" program on the PyBadge

import constants
import stage
import ugame


def menu_scene():
    # This function is the main game game_scene

    image_bank_background = stage.Bank.from_bmp16("dodgeball_background.bmp")

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
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

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

    game = stage.Stage(ugame.display, 60)
    game.layers = [player] + [ball] + [background]
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
        game.render_sprites([player] + [ball])
        game.tick()


if __name__ == "__main__":
    menu_scene()
