screen stats_screen:
    frame:
        align(0.5, 0.5)
        style_group "creation_points style"
        has vbox
        spacing 10
        hbox:
            text "Статистика" xalign 0.5
        hbox:
            text "Имя: [player_name]"
        hbox:
            text "Раса: [race]"
        hbox:
            text "Класс [player_class]"
        hbox:
            text "Здоровье: [player_max_hp]"
        hbox:
            text "Сила" xminimum 200
            bar range strength_max value strength_points xmaximum 200
            text "[strength_points]"
        hbox:
            text "Ловкость" xminimum 200
            bar range dexterity_max value dexterity_points xmaximum 200
            text "[dexterity_points]"
        hbox:
            text "Выносливость" xminimum 200
            bar range endurance_max value endurance_points xmaximum 200
            text "[endurance_points]"
        hbox:
            text "Интелект" xminimum 200
            bar range intelligence_max value intelligence_points xmaximum 200
            text "[intelligence_points]"
        hbox:
            text "Харизма" xminimum 200
            bar range charisma_max value charisma_points xmaximum 200
            text "[charisma_points]"
        hbox:
            text "Урон: [min_atk] - [max_atk]"
        textbutton ("Закончить"):
            xalign 0.5
            action Hide("stats_screen")

screen stats_button:
    frame:
        align(0.9, 0.1)
        textbutton _("Статистика") action Show("stats_screen")