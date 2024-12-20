label big_scene_1:
    scene bg ggroom_bright
    show gg calm1
    with fade
    if game_choice == "blue":
        jump blue_scene_1
    if game_choice == "pink" or game_choice == "violet":
        scene bg ggroom_bright
        show gg calm1
        play music Holy_Moly_Mountain        
        "Очередной день. Кажется, ты уже начинаешь уставать. Но не время унывать! Игра уже считай готова, нужны лишь спрайты и уровни."
        "Начнём со спрайтов, текстур, дизайна."
        "Итак, можно взять спрайты из интернета или попробовать нарисовать всё самим."
        "Откуда возьмёшь спрайты?"
        menu:
            "Из интернета":
                if game_choice == "pink":
                    jump pink_scene_1
                else:
                    jump violet_scene_1
            "Сделаю сам":
                if game_choice == "pink":
                    jump pink_scene_1
                else:
                    jump violet_scene_1

    elif game_choice == "salat":
        jump salat_scene_1
    elif game_choice == "green":
        jump green_scene_1
    elif game_choice == "yellow":
        jump yellow_scene_1

label big_scene_2:
    stop music fadeout 2
    "Телефон" "*звенит*"
    show gg looktophone_
    maincharacter "М? Кто это может быть?"
    show gg talktophone_
    maincharacter "Алло?"
    "Алекс" "Привет! Это Алекс из отдела кадров. Есть небольшая новость, которую нужно до вас донести."
    "Алекс" "Видите ли, у нас тут произошла маленькая перестановка в графике."
    "Алекс" "К сожалению, наш босс решил, что прототип, который вы готовите, нужно будет предоставить раньше, чем планировалось."
    "Алекс" "На самом деле, срок сдачи передвинули. Вам нужно показать игру уже... послезавтра."

    maincharacter "{sc=5}{b=10}{color=#ff0000}Послезавтра?!{/color}{/b}{/sc}"
    maincharacter "{sc=5}{b=10}{color=#ff0000}Вы издеваетесь?{/color}{/b}{/sc}"

    "Алекс" "Знаю, это не очень удобно, но, понимаете, нашему боссу нужно всё увидеть как можно скорее, чтобы принять решение."
    "Алекс" "Если получится хоть что-то показать, пусть даже и не идеально... думаю, это произведёт впечатление."
    "Ты в ужасе осознаешь, что у тебя остаётся гораздо меньше времени."
    "Алекс" "Вы не можете ничего с этим поделать, а я пожелаю вам удачи. До свидания!"
    show gg looktophone_
    "Телефон" "~гудки~"
    show gg calm2
    if game_choice == "blue":
        jump blue_scene_2
    elif game_choice == "pink":
        jump pink_scene_2
    elif game_choice == "violet":
        jump violet_scene_2
    elif game_choice == "salat":
        jump salat_scene_2
    elif game_choice == "yellow":
        jump yellow_scene_2
    elif game_choice == "green":
        jump green_scene_2
    jump big_scene_2

label big_scene_3:
    scene bg ggroom_bright
    show gg calm1
    with fade
    "Ты просыпаешься за столом, совсем не выспавшийся. У тебя болит голова."
    "Итак, на четвертый день, едва открыв глаза, ты чувствуешь, как накопившаяся усталость давит на тебя."
    "Последние три дня были настоящим испытанием: работа над механиками, бесконечное тестирование, настройка спрайтов — всё это стало невыносимо тяжёлым."
    maincharacter "О боже, как же мне хреново..."
    maincharacter "Завтра мне нужно будет показать мою игру работодателю..."
    maincharacter "Голова раскалывается, я думаю мне стоит выйти на свежий воздух, зайти в кофейню рядом с офисом, может, там кто-то может помочь улучшить мою игру."

    scene bg coffeeroom
    show gg calm1
    with fade
    "И вот ты наконец зашёл в кофейню, запах кофе подбадривает, и тебе становится немного лучше."
    "Ты заказываешь двойной эспрессо. Вдруг твой взгляд захватывает Павел, тот самый программист, которого ты повстречал в коворкинге несколько дней назад."
    menu:
        "Подойти к нему и расспросить насчёт игры.":
            show gg speak_:
                xalign 0.8
                yalign 1.05
            show pavel calm1:
                xalign 0.2
                yalign 1.05
            "Ты собираешься духом и подходишь к Павлу, в надежде, что тот тебе поможет"
            maincharacter "Привет! Не ожидал тебя здесь встретить, — ты пытаешься начать разговор с легкой улыбкой, надеясь, что Павел будет расположен помочь."

            pavel "О, привет! Ты как раз работаешь над тестовым заданием для нашей компании, верно? Как продвигается?"

            maincharacter "Всё путём, вроде... Ну, я сюда за тем и пришёл, чтобы получить помощь, что скажешь, найдётся немного времени для столь важной для меня игры?"

            pavel "Эх, ну раз для тебя это так важно... Давай сюда ноутбук, посмотрим."
            if game_choice == "blue":
                jump blue_scene_3
            elif game_choice == "pink":
                jump pink_scene_3
            elif game_choice == "violet":
                jump pink_scene_3
            elif game_choice == "salat":
                jump salat_scene_3
            elif game_choice == "yellow":
                jump yellow_scene_3
            elif game_choice == "green":
                jump green_scene_3
            jump big_scene_3

        "Не подходить к нему, просто выпить кофе и отдохнуть.":
            jump UNDERTALE_reference_OOaAoaoAOaAAOo

label UNDERTALE_reference_OOaAoaoAOaAAOo:
    "Ты расслабляешься, наслаждаешься видом из окна и, наконец, немного отдыхаешь. Тебе явно этого не хватало"
    "Теперь ты полон сил, энергичен, и готов наконец закончить эту игру!"
    play sound "audio/sounds/savepoint.mp3" 
    "{b=10}{color=#ffff00}ВЫ НАПОЛНЯЕТЕСЬ РЕШИМОСТЬЮ{/color}{/b}"
    jump big_scene_5


label big_scene_4:
    pavel "Мгм. Теперь всё должно работать как нужно. Код, кстати очень \"грязный\". Не помешал бы рефакторинг."

    maincharacter "Рефакто-что?"

    pavel "Рефакторинг. Видишь ли, ты БУДЕШЬ работать в команде, когда устроишься на работу."
    maincharacter "А когда ты работаешь в команде, то каждый должен с лёгкостью понимать, за что отвечает та или иная часть кода."
    maincharacter "Раздели код, сделай приятным для глаза, сделай более понятным. Думаю, НАШ босс оценит это."

    pavel "-Так, смотрим дальше..."
    pavel "Знаешь, этой игре очень не хватает саунд-дизайна."
    pavel "Ну то есть звуков всяких, чтобы игра ощущалась более тактильной и всё такое. Звук вообще чудеса творит."

    maincharacter "-О-о-окей. Звук. А где мне его взять?"

    pavel "-О-о-о, давай покажу."

    "Павел показывает тебе несколько сайтов с различными библиотеками звуков"

    pavel "Но знаешь, у меня есть своя личная коллекция классных звуков. Я даже знаю какие подойдут именно для твоей игры!"
    
    "Павел показывает тебе звуки, которые действительно бы подошли к твоей игре - звуки прыжка, стрельбы, ходьбы."

    pavel "А теперь давай подключим эти звуки. Не бойся, это не долго."

    "Вы вместе подключаете звуки к проекту, это занимает всего 15 минут."

    maincharacter "Воу! Стало гораздо лучше, спасибо!"
    if game_choice == "blue":
        pavel "Это ещё не все улучшения. У тебя есть стрельба, но нет врагов."
        pavel "Давай по-быстрому реализуем врагов с простым алгоритмом действия, как в Марио. Можно конечно сделать сложнее, но это долго, у нас сейчас нет на это времени"
    
    elif game_choice == "pink":
        pavel "Это ещё не все улучшения."
        pavel "У тебя есть уровни, но они слишком лёгкие."
        pavel "Давай по-быстрому реализуем врагов с простым алгоритмом действия, как в Марио. Можно конечно сделать сложнее, но это долго, у нас сейчас нет на это времени"
    
    elif game_choice == "violet":
        pavel "Это ещё не все улучшения."
        pavel "У тебя есть уровни, но они слишком лёгкие."
        pavel "Давай по-быстрому реализуем врагов с простым алгоритмом действия, как в Марио. Можно конечно сделать сложнее, но это долго, у нас сейчас нет на это времени"
    
    elif game_choice == "salat":
        pavel "-Это ещё не все улучшения. У тебя есть стрельба, но нет врагов."
        pavel "Давай по-быстрому реализуем врагов с простым алгоритмом действия, как в Марио. Можно конечно сделать сложнее, но это долго, у нас сейчас нет на это времени."
    
    elif game_choice == "yellow":
        pavel "Это ещё не все улучшения. Я вижу, что со временем игра никак не меняется, такое же количество клиентов, такие же потребности, а улучшений всё больше, что сильно упрощает игру."
        pavel "Давай сделаем постепенное усложнение, чтобы игра становилась сложнее с каждым днём"
    
    elif game_choice == "green":
        pavel "-Это ещё не все улучшения. У тебя есть стрельба, но нет врагов."
        pavel "Давай по-быстрому реализуем врагов с простым алгоритмом действия. Можно конечно сделать умный ИИ, но это долго, у нас сейчас нет на это времени"
    


    maincharacter "Я не то чтобы знаю, как это делается..."

    pavel "Ну, не зря же ты ко мне пришёл, сейчас мы мигом всё порешаем."
    pavel "Напишем небольшой алгоритм... - говорит он, печатая при этом со скоростью света в редакторе кода."
    pavel "Теперь подключим спрайт, который, кстати, у тебя уже есть. И... готово!"

    maincharacter "У меня нет слов..."

    if game_choice == "blue":
        pavel "Ничего не говори, просто смотри и запоминай. Пригодится."
        pavel "И вот я уже прошёл игру... Скудновато по уровням. Ну, уровни ты, надеюсь, сам дополнишь."
        pavel "С тебя кофе, кстати, хе-хе."
        
        maincharacter "Оу, да, конечно."
        "Ты заказываешь ему большой стакан капучино"
        maincharacter "Ты мне невероятно помог, спасибо тебе!"
        jump big_scene_for_blue_pink_violet_and_salat_way

    elif game_choice == "pink":
        pavel "Ничего не говори, просто смотри и запоминай. Пригодится."
        pavel "И вот я уже прошёл игру... Скудновато по уровням. Ну, уровни ты, надеюсь, сам дополнишь."
        pavel "С тебя кофе, кстати, хе-хе."

        maincharacter "Оу, да, конечно."
        "Ты заказываешь ему большой стакан капучино"
        maincharacter "Ты мне невероятно помог, спасибо тебе!"
        jump big_scene_for_blue_pink_violet_and_salat_way

    elif game_choice == "violet":
        pavel "Ничего не говори, просто смотри и запоминай. Пригодится."
        pavel "И вот я уже прошёл игру... Скудновато по уровням. Ну, уровни ты, надеюсь, сам дополнишь."
        pavel "С тебя кофе, кстати, хе-хе."

        maincharacter "Оу, да, конечно."
        "Ты заказываешь ему большой стакан капучино"
        maincharacter "Ты мне невероятно помог, спасибо тебе!"
        jump big_scene_for_blue_pink_violet_and_salat_way

    elif game_choice == "salat":
        pavel "Ничего не говори, просто смотри и запоминай. Пригодится."
        pavel "И вот я уже прошёл игру... Скудновато по уровням. Ну, уровни ты, надеюсь, сам дополнишь."
        pavel "С тебя кофе, кстати, хе-хе."

        maincharacter "Оу, да, конечно."
        "Ты заказываешь ему большой стакан капучино"
        maincharacter "Ты мне невероятно помог, спасибо тебе!"
        jump big_scene_for_blue_pink_violet_and_salat_way


    elif game_choice == "yellow":
        pavel "Ничего не говори, просто смотри и запоминай. Пригодится."
        pavel "И вот я уже купил все улучшения в игре... Быстро как-то получилось."
        pavel "Ну, дополнишь если надо. А в остальном - прекрасный прототип игры!"
        pavel "Мне нравится. А с тебя кофе, кстати, хе-хе."

        maincharacter "Оу, да, конечно."
        "Ты заказываешь ему большой стакан капучино"
        maincharacter "Ты мне невероятно помог, спасибо тебе!"
        jump big_scene_for_yellow_way

    elif game_choice == "green":
        pavel "Ничего не говори, просто смотри и запоминай. Пригодится."
        pavel "Тут я конечно мало чем смогу помочь, в игре всё как-то скудно-бедно."
        pavel "Слишком много нужно сделать, займись этим. Доработать механики, исправить баги, геймплей. А ещё..."
        pavel "Я же не за просто так тебе помогал, я бы сейчас не отказался от капучино, смекаешь?"

        maincharacter "Оу, да, конечно."
        "Ты заказываешь ему большой стакан капучино"
        maincharacter "Ты мне невероятно помог, спасибо тебе!"
        jump big_scene_for_green_way

    pavel "Да без проблем, рад был помочь за чашечку кофе. Увидимся на работе!"
    "Оставшуюся часть последнего дня ты решаешь провести рефакторинг кода, сделать его более читаемым, исправить некоторые баги, дополнить уровни."

label big_scene_for_blue_pink_violet_and_salat_way:
    scene ggroom_dark
    show gg calm1
    with fade

    "После четырёх изнурительных дней работы над игрой ты понимаешь, что до завершения проекта остался всего один день."
    "Ты решаешь провести интенсивную финальную сессию, чтобы довести игру до минимально приемлемого уровня качества и избежать катастрофических багов, которые могут сорвать презентацию игры работодателю."
    
    "Шаг 1: Подготовка к рефакторингу"
    "Рефакторинг... ты гуглишь, что это такое и как его делать."
    "{b}Рефакторинг{/b} — это процесс изменения внутренней структуры программы, не затрагивающий её внешнего поведения и имеющий целью облегчить понимание её работы."
    "Ты понимаешь, что твой код сейчас — это скопление хаотичных решений, принятых в спешке."
    "Никто сразу и не поймёт, что ты тут понаписал. Поэтому, прежде чем делать что-то серьёзное, ты начинаешь с ревизии основных компонентов: открываешь ключевые файлы с кодом и на листочке помечаешь самые хаотичные участки."
    "Ты знаешь, что полный рефакторинг невозможен, но хочешь сделать код хотя бы немного чище."

    "Шаг 2: Минимизация хаоса в коде"
    "Ты начинаешь с самых проблемных функций — тех, которые отвечают за передвижение игрока и коллизию с объектами уровня." 
    "Слишком много «магических чисел»(плохая практика программирования, когда в исходном коде встречается числовое значение и неочевиден его смысл), вложенных условий и временных переменных, которые запутывают логику." 
    "Ты терпеливо заменяешь «магические числа» на осмысленные константы, переименовываешь переменные на более говорящие названия, комментируешь сложные части, где это нужно."
    "В процессе ты находишь два дублирующихся куска кода, которые управляли анимацией персонажа, и выносишь их в отдельную функцию. Это не только упрощает код, но и даёт шанс избежать досадных ошибок при добавлении новых уровней."

    "Шаг 3: Исправление критических багов"
    "Переключившись на исправление багов, ты сосредотачиваешься на главных проблемах, которые могут убить всё впечатление от игры:"
    "Баг с падением сквозь платформы: он замечаешь, что при прыжке персонаж иногда проваливается сквозь платформу, если нажать клавишу слишком быстро." 
    "Он добавляет небольшой таймер, чтобы обработка коллизии происходила с небольшой задержкой, предотвращая такие ситуации."

    "Шаг 4: Финализация уровней"
    "Убедившись, что критические баги исправлены, ты переходишь к завершению дизайна уровней."

    "Ты понимаешь, что у тебя нет времени создавать новые элементы, поэтому сосредотачиваешься на «полировке» уже существующих"
    "Добавляешь несколько сложных платформ в последний уровень, чтобы игроку было интересно проходить его."
    "Прячешь несколько бонусов для тех, кто исследует уровни вдумчиво."
    "Ты понимаешь, что идеала тебе уже не достичь, но ты стараешься, чтобы игровой процесс выглядел цельным и доставлял удовольствие."
    "Всё."
    "Игра готова."
    "Облегчение."
    "Спокойствие."
    "Гора с плеч."
    "Засыпай... Спокойной ночи."

    jump big_scene_for_blue_pink_and_violet_way

label big_scene_for_green_way:
    scene ggroom_dark
    show gg calm1
    with fade
    "После четырёх изнурительных дней работы над игрой ты понимаешь, что до завершения проекта остался всего один день."
    "Ты решаешь провести интенсивную финальную сессию, чтобы довести игру до минимально приемлемого уровня качества и избежать катастрофических багов, которые могут сорвать презентацию игры работодателю."
    
    "Шаг 1: Подготовка к рефакторингу"
    "Рефакторинг... ты гуглишь, что это такое и как его делать."
    "{b}Рефакторинг{/b} — это процесс изменения внутренней структуры программы, не затрагивающий её внешнего поведения и имеющий целью облегчить понимание её работы."
    "Ты понимаешь, что твой код сейчас — это скопление хаотичных решений, принятых в спешке."
    "Никто сразу и не поймёт, что ты тут понаписал. Поэтому, прежде чем делать что-то серьёзное, ты начинаешь с ревизии основных компонентов: открываешь ключевые файлы с кодом и на листочке помечаешь самые хаотичные участки."
    "Ты знаешь, что полный рефакторинг невозможен, но хочешь сделать код хотя бы немного чище."

    "Шаг 2: \"Полировка\" игры."
    "Ты не в восторге от своей игры, потому что она выглядит совсем не так, как ты её видел в своём сне." 
    "Поэтому ты решаешь хоть немного улучшить игровой процесс, хотя сделать его просто хотя бы хорошим вряд ли представляется возможным."
    "Ты не в восторге от своей игры, потому что она выглядит совсем не так, как ты её видел в своём сне. Поэтому ты решаешь хоть немного улучшить игровой процесс, хотя сделать его просто хотя бы хорошим вряд ли представляется возможным."
    "Ты немного улучшаешь стрельбу, следуя туториалам из интернета."
    "Тебе нужно какое-то разнообразие, иначе игра выйдет совсем скучной."
    "Ты добавляешь частоту появления врагов и небольшие улучшения, по типу скорости стрельбы и увеличение скорости."

    "Ты понимаешь, что у тебя нет времени создавать новые элементы, поэтому сосредотачиваешься на «полировке» уже существующих"
    "Добавляешь несколько сложных платформ в последний уровень, чтобы игроку было интересно проходить его."
    "Прячешь несколько бонусов для тех, кто исследует уровни вдумчиво."
    "Ты понимаешь, что идеала тебе уже не достичь, но ты стараешься, чтобы игровой процесс выглядел цельным и доставлял удовольствие."
    "Всё."
    "Игра готова."
    "Облегчение."
    "Спокойствие."
    "Гора с плеч."
    "Засыпай... Спокойной ночи."
    jump big_scene_for_green_way

label big_scene_for_yellow_way:
    scene ggroom_dark
    show gg calm1
    with fade
    "После четырёх изнурительных дней работы над игрой ты понимаешь, что до завершения проекта остался всего один день."
    "Ты решаешь провести интенсивную финальную сессию, чтобы довести игру до минимально приемлемого уровня качества и избежать катастрофических багов, которые могут сорвать презентацию игры работодателю."
    
    "Шаг 1: Подготовка к рефакторингу"
    "Рефакторинг... ты гуглишь, что это такое и как его делать."
    "{b}Рефакторинг{/b} — это процесс изменения внутренней структуры программы, не затрагивающий её внешнего поведения и имеющий целью облегчить понимание её работы."
    "Ты понимаешь, что твой код сейчас — это скопление хаотичных решений, принятых в спешке."
    "Никто сразу и не поймёт, что ты тут понаписал. Поэтому, прежде чем делать что-то серьёзное, ты начинаешь с ревизии основных компонентов: открываешь ключевые файлы с кодом и на листочке помечаешь самые хаотичные участки."
    "Ты знаешь, что полный рефакторинг невозможен, но хочешь сделать код хотя бы немного чище."

    "Шаг 2: Минимизация хаоса в коде"
    "Ты начинаешь с самых проблемных функций — тех, которые отвечают за передвижение игрока и коллизию с объектами уровня." 
    "Слишком много «магических чисел»(плохая практика программирования, когда в исходном коде встречается числовое значение и неочевиден его смысл), вложенных условий и временных переменных, которые запутывают логику." 
    "Ты терпеливо заменяешь «магические числа» на осмысленные константы, переименовываешь переменные на более говорящие названия, комментируешь сложные части, где это нужно."
    "В процессе ты находишь два дублирующихся куска кода, которые управляли анимацией персонажа, и выносишь их в отдельную функцию. Это не только упрощает код, но и даёт шанс избежать досадных ошибок при добавлении новых уровней."

    "Шаг 3: Исправление критических багов"
    "Переключившись на исправление багов, ты сосредотачиваешься на главных проблемах, которые могут убить всё впечатление от игры:"
    "Баг с падением сквозь платформы: он замечаешь, что при прыжке персонаж иногда проваливается сквозь платформу, если нажать клавишу слишком быстро." 
    "Он добавляет небольшой таймер, чтобы обработка коллизии происходила с небольшой задержкой, предотвращая такие ситуации."

    "Шаг 4: Финализация уровней"
    "Убедившись, что критические баги исправлены, ты переходишь к завершению дизайна уровней."

    "Добавляешь возможность расширить свою игровую кафешку, чтобы приходило больше посетителей."
    "Добавляешь систему найма работников, чтобы автоматизировать работу внутриигровой межпланетной кафешки."

    "Ты понимаешь, что у тебя нет времени создавать новые элементы, поэтому сосредотачиваешься на «полировке» уже существующих"
    "Добавляешь несколько сложных платформ в последний уровень, чтобы игроку было интересно проходить его."
    "Прячешь несколько бонусов для тех, кто исследует уровни вдумчиво."
    "Ты понимаешь, что идеала тебе уже не достичь, но ты стараешься, чтобы игровой процесс выглядел цельным и доставлял удовольствие."
    "Всё."
    "Игра готова."
    "Облегчение."
    "Спокойствие."
    "Гора с плеч."
    "Засыпай... Спокойной ночи."
    jump big_scene_for_yellow_way








