init:
    $init_creation_points = 10
    $creation_points = init_creation_points

    #Сила
    $strength_max = 10
    $strength_points = 0
    #Ловкость
    $dexterity_max = 10
    $dexterity_points = 0
    #Выносливость
    $endurance_max = 10
    $endurance_points = 0
    #Интелект
    $intelligence_max = 10
    $intelligence_points = 0
    #Харизма
    $charisma_max = 10
    $charisma_points = 0

    $ player_max_hp = 100
    $ enemy_max_hp = 100
    $ player_hp = player_max_hp
    $ enemy_hp = enemy_max_hp
    $ min_atk = 1
    $ max_atk = 10


define m = Character("[player_name]")
default race = None
default player_class = None

screen select_character():
    default selected_character = None
    hbox:
        spacing 50
        align(0.5, 0.5)
        if race == "Человек":
            frame:
                background("#da8b31" if selected_character == "human_male.png" else "#ffffff")
                imagebutton:
                    idle "human_male.png"
                    action SetScreenVariable('selected_character', "human_male.png")
            frame:
                background("#da8b31" if selected_character == "human_female.png" else "#ffffff")
                imagebutton:
                    idle "human_female.png"
                    action SetScreenVariable('selected_character', "human_female.png")
        
        if race == "Орк":
            frame:
                background("#da8b31" if selected_character == "orc_male.png" else "#ffffff")
                imagebutton:
                    idle "orc_male.png"
                    action SetScreenVariable('selected_character', "orc_male.png")
            frame:
                background("#da8b31" if selected_character == "orc_female.png" else "#ffffff")
                imagebutton:
                    idle "orc_female.png"
                    action SetScreenVariable('selected_character', "orc_female.png")

        if race == "Эльф":
            frame:
                background("#da8b31" if selected_character == "elf_male.png" else "#ffffff")
                imagebutton:
                    idle "elf_male.png"
                    action SetScreenVariable('selected_character', "elf_male.png")
            frame:
                background("#da8b31" if selected_character == "elf_female.png" else "#ffffff")
                imagebutton:
                    idle "elf_female.png"
                    action SetScreenVariable('selected_character', "elf_female.png")

    if selected_character != None:
        textbutton _("Выбрать"):
            align(0.5, 0.9)
            action Return(selected_character)

default mc_image_name = 'human_male.png'
image mc_image = "[mc_image_name]"

screen stats_create:
    frame:
        align(0.5, 0.5)
        style_group "creation_points_style"
        has vbox
        hbox:
            text "Осталось очков: [creation_points]"
        hbox:
            if creation_points == 0:
                textbutton ("Сила") xminimum 200 action None
            else:
                textbutton ("Сила") xminimum 200 action [SetVariable("strength_points", strength_points + 1), SetVariable("creation_points", creation_points - 1)]
            bar range strength_max value strength_points xmaximum 200
            text "[strength_points]"
        hbox:
            if creation_points == 0:
                textbutton ("Ловкость") xminimum 200 action None
            else:
                textbutton ("Ловкость") xminimum 200 action [SetVariable("dexterity_points", dexterity_points + 1), SetVariable("creation_points", creation_points - 1)]
            bar range dexterity_max value dexterity_points xmaximum 200 
            text "[dexterity_points]"
        hbox:
            if creation_points == 0:
                textbutton ("Выносливость") xminimum 200 action None
            else:
                textbutton ("Выносливость") xminimum 200 action [SetVariable("endurance_points", endurance_points + 1), SetVariable("creation_points", creation_points - 1)]
            bar range endurance_max value endurance_points xmaximum 200
            text "[endurance_points]"
        hbox:
            if creation_points == 0:
                textbutton ("Интелект") xminimum 200 action None
            else:
                textbutton ("Интелект") xminimum 200 action [SetVariable("intelligence_points", intelligence_points + 1), SetVariable("creation_points", creation_points - 1)]
            bar range intelligence_max value intelligence_points xmaximum 200
            text "[intelligence_points]"
        hbox:
            if creation_points == 0:
                textbutton ("Харизма") xminimum 200 action None
            else:
                textbutton ("Харизма") xminimum 200 action [SetVariable("charisma_points", charisma_points + 1), SetVariable("creation_points", creation_points - 1)]
            bar range charisma_max value charisma_points xmaximum 200
            text "[charisma_points]"
        hbox:
            textbutton ("Сбросить") action [SetVariable("strength_points", 0), SetVariable("dexterity_points", 0), SetVariable("endurance_points", 0), SetVariable("intelligence_points", 0), SetVariable("charisma_points", 0), SetVariable("creation_points", init_creation_points)]
            if creation_points == 0:
                textbutton ("Закончить") action Return()
            else:
                textbutton ("Закончить") action None

label create_character:
    python:
        player_name = renpy.input("Для начала скажи свое имя: ", length=32)
        player_name = player_name.strip()

        if not player_name:
            player_name = "Джон"

    "[player_name]? Интересное имя..."

    "Начнем с прокачки статов:"

    call screen stats_create

    menu:
        "Теперь выбери расу"
        "Человек":
            $ race = "Человек"
            $ dexterity_points += 1
            $ charisma_points += 2
            "Вы выбрали человека\nВаша ловкость и харизма увеличены"
        "Орк":
            $ race = "Орк"
            $ strength_points += 2
            $ endurance_points += 1
            "Вы ыбрали орка\nВаша сила и выносливость увеличены"
        "Эльф":
            $ race = "Эльф"
            $ intelligence_points += 2
            "Вы выбрали эльфа\n Ваш интелект увеличен"

    "Выберите, как выглядит ваш персонаж"
    call screen select_character
    $ mc_image_name = _return
    show mc_image
    m "Выгляжу неплохо"

    menu:
        "Теперь выберите класс"
        "Воин":
            $ player_class = "Воин" 
            $ strength_points += 2
            $ endurance_points += 2
            "Воин! хорош во владении мечом и щитом\nХороший выбор"
        "Охотник":
            $ player_class = "Охотник"
            $ dexterity_points += 2
            "Охотник! мастер во владении лука\nХороший выбор"
        "Маг":
            $ player_class = "Маг"
            $ intelligence_points += 2
            "Маг! вашему уму любой может позавидовать\nХороший выбор"
    
    $ player_max_hp += (10*endurance_points)
    $ player_hp = player_max_hp
    $ min_atk += (2*strength_points)
    $ max_atk += (2*strength_points)

    return