label blue_scene_1:
    "И вот, спустя день трудностей и написания костылей, ты наконец подготовил всё нужное для создания прототипа платформера на UnrealEngine."
    "И ты чувствуешь..."
    "..."
    play music I_WANT_PANDEMONIKA
    show gg angry_
    "{cps=100}{sc=10}{b=40}{color=#ff0000}ЯРОСТЬ{/color}{/b}{/sc}{/cps}"

    maincharacter "{cps=50}{sc=10}{b=40}{color=#ff0000}БОЖЕ{/color}{/b}{/sc}{/cps}"
    maincharacter "{cps=50}{sc=10}{b=40}{color=#ff0000}МОЙ{/color}{/b}{/sc}{/cps}"
    maincharacter "{cps=50}{color=#ff0000}ПОЧЕМУ ТУТ ВСЁ ТАК СЛОЖНО?{/color}{/cps}"
    maincharacter "{cps=50}РАЗРАБОТКА ЕЩЁ НЕ НАЧАЛАСЬ, А У МЕНЯ УЖЕ КУЧА КОСТЫЛЕЙ В ПРОЕКТЕ.{/cps}"
    maincharacter "{cps=20}Чтобы понять, как нормально сделать этот чёртов {bt=6}{color=#1cd3a2}Tilemap{/color}{/bt} мне понадобилось {sc=10}{color=#ff0000}несколько часов{/color}{/sc}!{/cps}"
    maincharacter "{cps=20}Такое чувство, что движок создавался не совсем для 2D игр.{/cps}"
    stop music fadeout 5
    maincharacter "{cps=20}Стоп.{/cps}"
    maincharacter "{cps=20}Возможно, так и есть...{/cps}"
    maincharacter "{cps=20}Но не время унывать! У меня есть ещё время в запасе, я справлюсь!{/cps}"
    jump big_scene_2

label blue_scene_2:
    maincharacter "Без паники! у меня уже почти всё готово!"
    maincharacter "Нужно лишь реализовать пару простых механик, сделать уровни и украсть... "
    maincharacter "ой, то есть одолжить спрайты из интернета! Не будет мне никакого отдыха в эти 2 дня! За работу!!"

    "Ты начинаешь работать в усиленном темпе. Ты реализуешь двойной прыжок и стрельбу из оружия."
    "Получается, конечно, не без багов, но сейчас нет времени их исправлять."
    "Ты в спешке берёшь первый понравившийся тебе сет спрайтов из интернета, без раздумья скачивая и подключая его к своей игре через Tilemap. Далее ты заимствуешь два простеньких уровня из другого популярного платформера и реализуешь их."
    "Эту ночь ты практически не спишь... До четырёх часов ночи ты работаешь как никогда раньше, и у тебя..."
    "...Получилось! Ты сделал это! Спрайты для игры готовы, механики тоже. Ты засыпаешь прямо на столе перед ноутбуком."
    jump end_day_3

label blue_scene_3:
    maincharacter "Я работаю над платформером, но некоторые вещи всё еще не успел реализовать."
    maincharacter "Если честно, мне бы очень пригодилась помощь с финальными доработками — багами и оптимизацией."

    "Ты даёшь ему сыграть в твой прототип игры."
    
    pavel "Хм, ну, выглядит неплохо, давай проверим механики..."
    pavel "..."
    pavel "Ага! Если слишком часто нажимать кнопку стрельбы, то возможность стрелять ломается. Сейчас исправим!"

    "Он молниеносно находит эту механику в коде и исправляет её, а ты даже не успеваешь уследить за его действиями"
    jump big_scene_4