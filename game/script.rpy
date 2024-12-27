label start:
    stop music fadeout 1.0
    $ gg_name = renpy.input("Как зовут вашего персонажа?\n")
    pause 1.0
    play sound "audio/sounds/day_begining.mp3"
    scene bg day_1
    pause 5.0
    scene bg ggroom_bright with fade
    show gg calm1

    # show screen button_book

    play music mus_morning
    voice "dictor/line1_8am.ogg"
    "{bt=100}8 утра ☠️{/bt}"
    voice "main_character/start_lines_whos_writing.ogg"
    maincharacter "{cps=15}Кто-то пишет?\nКому я вообще сдался в такую рань?{/cps}" 
    show gg looktophone_:
        xalign 0.8
        yalign 1.05
    with move
    gendir_phone  "Напоминаем вам, что для успешного принятия на работу вы должны были сделать видеоигру, иначе мы будем вынуждены отказать вам в трудоустройстве"
    gendir_phone "До дедлайна осталось 7 дней"
    gendir_phone "Хотелось поинтересоваться, как ваш прогресс?"
    gendir_phone "С уважением,  директор компании."
    nvl clear
    stop music fadeout 1.0
    show gg calm1 at center 
    with move
    voice "main_character/start_lines_a_WEEK.ogg"
    maincharacter "{cps=100}НЕДЕЛЯ?!{/cps}"

    play music mus_aWeekNoWay
    scene bg ggroom_bright
    show gg shock_
    with Dissolve(10.0)


    ""
    voice "main_character/start_lines_i_forgor.ogg"
    maincharacter "ЧЁРТ! КАК Я МОГ ОБ ЭТОМ ЗАБЫТЬ? РАБОТА МОЕЙ МЕЧТЫ, А Я ПРО НЕЁ ПРОСТО ЗАБЫЛ!!"
    show gg facepalm_
    with fade
    voice "main_character/start_lines_clueles.ogg"
    maincharacter "Не стоило откладывать это дело на потом." 
    stop music fadeout 1.0
    play music chill_1 fadeout 1.0
    voice "main_character/start_lines_shurly_the_game_is_ready.ogg"
    maincharacter "Нужно написать, что всё в порядке, и игра почти готова."

    "Ты отправляешь ответное письмо работодателю, в котором пишешь, что всё под контролем, и нужно сделать финальные штрихи перед отправкой"

    show gg think_
    maincharacter "Так, [gg_name], сосредоточься, нужно придумать что-то."


    maincharacter "Уж лучше расспрошу коллег, вдруг расскажут чего полезного про разработку и про то, как оценивают игру."
    maincharacter "Нужно найти информацию о том, как сделать игру. Но где? Где можно встретить коллег, у которых можно что-то спросить?"
    maincharacter "Хм, я слышал у них в офисе есть классное помещение... как его там... "
    maincharacter "Коворкинг. Место, куда люди приходят, чтобы вместе или в одиночку поработать над чем-то."
    "Ты выходишь из дома и направляешься в офисный коворкинг компании, в которую трудоустраиваешься."
    jump street

    return

    

    

