init:
    $ screen_center = Position(xpos = 0.5, ypos = 0.5)

label start:

    scene bg room

    call create_character

    show screen stats_button

    show screen map_button
    "Какие возможности игры ты хочешь посмотреть?"

    menu:
        "Тестовая битва":
            call battle_loop

    "На этом пока что все"

    return

