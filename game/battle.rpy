screen battle_loop:
    frame:
        align(0.5, 0.05)
        vbox:
            text "Тестовый враг"
            bar:
                xalign 0.5
                xmaximum 220
                range enemy_max_hp 
                value enemy_hp
            text "[enemy_hp] / [enemy_max_hp]":
                xalign 0.5
    frame:
        align(0.5, 0.5)
        image "enemy_sprite.png"
    frame:
        align(0.5, 0.9)
        vbox:
            text "[player_name]":
                xalign 0.5
            bar:
                xmaximum 220
                range player_max_hp
                value player_hp
            text "[player_hp] / [player_max_hp]":
                xalign 0.5

screen battle_buttons:
    frame:
        align (0.1, 0.5)
        vbox:
            spacing 20
            textbutton _("Атака"):
                action Return("atk")
            textbutton _("Лечение"):
                action Return("heal")

label battle_loop:

    hide mc_image

    hide screen stats_button

    show screen battle_loop

    show screen battle_buttons

    while ((player_hp > 0) and (enemy_hp > 0)):
        $ res = ui.interact()

        if res == "atk":
            call attack
        if res == "heal":
            call heal

        if (enemy_hp <= 0):
            hide screen battle_loop
            hide screen battle_buttons
            "Враг побежден"
            return

        $ enemy_attack = renpy.random.randint(1, 10)
        $ player_hp -= enemy_attack
        "Вам нанесли [enemy_attack] урона" 

        if (player_hp <= 0):
            hide screen battle_loop
            hide screen battle_buttons
            "Вы проиграли"
            return        

label attack:
    $ player_attack = renpy.random.randint(min_atk, max_atk)
    $ enemy_hp -= player_attack
    "Вы нанесли [player_attack] урона"
    return

label heal:
    $ player_hp += 20
    if player_hp > player_max_hp:
        $ player_hp = player_max_hp
        "Здоровье полностью восстановленно"
    else:
        "Вы восстановили 20 здоровья"
        return
