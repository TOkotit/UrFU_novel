label day_2_begin:
    pause 1.0
    play sound "audio/sounds/day_begining.mp3"
    scene bg day_2
    pause 5.0
    scene bg ggroom_bright 
    show gg calm2
    with fade
    play music morning_chill
    "Ты неохотно просыпаешься, и понимаешь, что это был сон. Ты разочарован, ведь тебе там так сильно нравилось."
    "Тебе очень хочется вернуться туда, тот сон был действительно классным, он зародил в тебе идею масштабной амбициозной игры."
    menu:
        "Попытаться вновь уснуть, чтобы опять попасть в этот сон.":
            scene black with fade
            "Ты закрываешь глаза, расслабляешься и, наконец, засыпаешь."
            "Опять."
            "Проходит время..."
            "..."
            scene bg ggroom_bright
            show gg looktophone_
            with fade
            "Ты просыпаешься, однако в этот раз тебе ничего не снилось."
            "Ты берёщь телефон в руку"
            stop music fadeout 2.0
            "16:00"
            show gg shock
            maincharacter "СКОЛЬКО?!"
            maincharacter "КАК Я МОГ ПРОСПАТЬ ПОЛДНЯ, КОГДА У МЕНЯ РАЗРАБОТКА ВИДЕОИГРЫ НА НОСУ, ЧЁРТ ПОДЕРИ!!!"
            show gg calm2
            maincharacter ""
            maincharacter "В любом случае, пора за работу!"
            jump sit_to_the_laptop

        "Встать с кровати, начать делать игру.":
            jump sit_to_the_laptop

label day_3_begin:
    pause 1.0
    play sound "audio/sounds/day_begining.mp3"
    scene bg day_3
    pause 5.0
    jump big_scene_1


label day_4_begin:
    pause 1.0
    play sound "audio/sounds/day_begining.mp3"
    scene bg day_4
    pause 5.0
    jump big_scene_3
