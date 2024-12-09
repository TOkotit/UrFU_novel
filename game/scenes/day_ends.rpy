label end_first_day:
    scene bg coworking
    show gg calm1
    with fade
    play music evening_chill fadeout 2.0
    "На улице темнеет, люди начинают собирать вещи, чтобы идти домой. Офис постепенно пустеет, скоро он закроется. Тебе тоже пора идти домой."
    "Ты глядишь на свой жёлтенький блокнот, и понимаешь, что этого вполне достаточно чтобы хотя бы начать делать игру."
    "Ты выходишь из офиса и возвращаешься домой."

    scene bg ggroom_dark
    show gg calm1
    with fade
    maincharacter "Уже довольно поздно, думаю, не буду себя загружать сегодня. Начну разработку завтра."
    "Ты ложишься спать."
    scene black
    hide gg calm1 
    with Dissolve(1.0)

    "..."
    "Тебе снится, как ты попал 3D-шутер с огромными роботами, которыми ты можешь управлять."
    "Взрывы, выстрелы, экшен, невероятные сцены."
    "Ты не осознаешь, что это сон, и ты действительно хочешь остаться здесь, во сне."
    stop music fadeout 1.0
    jump day_2_begin

label end_day_2:
    scene black
    with fade
    stop music fadeout 1.0
    jump day_3_begin

label end_day_3:
    scene black
    with fade
    stop music fadeout 1.0
    jump day_4_begin