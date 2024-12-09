
define count_question = 0
define first_question = False
define second_question = False
define third_question = False


label Now_its_definitely_coworking:
    scene bg coworking 
    with fade

    "Ты заходишь в офисный коворкинг. Здесь довольно уютно."
    "В этой большой комнате ты видишь: одного довольно стильного парня, который усердно над чем-то работает в своём ноутбуке. Рядом с ним стоит пустой стакан с кофе. Кажется, сидит он тут довольно давно."

    "Справа от того парня, в углу, сидят двое - парень и девушка, они также чем-то заняты, каждый смотрит в свой ноутбук. Иногда они переговариваются, обсуждая что-то"
    "Ну что, к кому подойдёшь?"
    menu:
        "Парень, который сидит один.":
            jump one_dude
        "Дуо в углу.":
            jump duo_dudes

    return


label one_dude:
    play music kostyan_theme
    show kostya calm1 with moveinleft:
        xalign 0.2
        yalign 1.05
    show gg calm1 with moveinright:
        xalign 0.8
        yalign 1.05
    
    "Ты приближаешься к тому самому парню, который сидит один за своим ноутбуком"

    "На вид ему лет 25, на нём солнцезащитные очки. В здании."
    "В облачную погоду. Но на этом странности не заканчиваются, ведь на нём надета качественная кожаная куртка, хотя здесь, кажется, жарковато."

    "У него светлые ухоженные волосы средней длины. Можно сказать, он тщательно следит за своей внешностью."

    maincharacter "Привет! Можно мне присесть рядом?"

    kostya "Да, конечно."

    show gg calm2:
        xalign 0.8
        yalign 1.05
    maincharacter "Ну..."
    maincharacter "Ээ..."
    maincharacter "Ты умеешь создавать игры?"

    show kostya calm3:
        xalign 0.2
        yalign 1.05
    kostya "Умею ли я? Хе-хе."
    kostya "Если бы я не умел, меня бы здесь не было, дружище!"
    kostya "Уточню: я не то чтобы умею именно ДЕЛАТЬ игры, я умею делать игры ХОРОШИМИ."

    maincharacter "А, вот оно как. А что это, собственно значит? Кто ты?"

    kostya "Меня зовут Костян, и я дизайнер. Но иногда и геймдизанер, тут всё по случаю."
    show gg speak_:
        xalign 0.8
        yalign 1.05
    maincharacter  "Расскажешь об этом подробнее?"
    show kostya calm2:
        xalign 0.2
        yalign 1.05
    kostya "Видишь ли, самое главное в игре - привлечь внимание игрока своим видом."
    kostya "Дизайн игры, механика, графика, саунд-дизайн, стилистика, и даже... Нет, *особенно* музыка!"
    kostya "Игра должна выделяться, удивлять, вызывать вопросы!"

    "Теперь ты понимаешь, что его вид - часть его образа геймдизайнера, олицетворение его работы. Ты удивлённо продолжаешь слушать."
    show kostya calm3:
        xalign 0.2
        yalign 1.05
    kostya "Музыкой я не занимаюсь, а вот остальное - это моё дело, и я это обожаю."

    maincharacter "Я впечатлён. Ты, видимо, довольно опытный, можешь дать совет?"

    kostya  "Да, конечно, что тебя интересует?"

    while count_question < 3:
        menu:
            "Как придумать игру? Подскажи пару идей.":
                if first_question:
                    kostya "Ты уже это спрашивал"
                else:
                    $ first_question = True
                    $ count_question += 1
                    show gg calm1:
                        xalign 0.8
                        yalign 1.05
                    maincharacter "Я ещё не начал делать игру, подскажи пожалуйста, какую вообще игру мне стоит делать?"
                    show kostya calm3:
                        xalign 0.2
                        yalign 1.05
                    kostya "Если ты еще не определился с жанром, то советую делать какой-нибудь платформер с уникальными механиками, которые ты, конечно же, придумаешь сам. Или может какая-нибудь аркада, которая с течением времени становится сложнее."
                    kostya "Может быть, тебе захочется какую-нибудь простую казуальную игру, например, где главный герой работает в кофейне и должен обслуживать клиентов."
                    kostya "Игры в этих жанрах вполне можно реализовать в короткие сроки, если изрядно постараться."

                    if count_question == 2:
                        kostya "Ладно, давай последний вопрос и я пойду. Дела появились."
            "Какую игру лучше сделать? 2D или 3D?":
                if second_question:
                    kostya "Ты уже это спрашивал"
                else:
                    $ count_question += 1
                    $ second_question = True
                    show gg calm1:
                        xalign 0.8
                        yalign 1.05
                    maincharacter "Какую игру лучше сделать? 2D или 3D?"
                    show kostya calm3:
                        xalign 0.2
                        yalign 1.05
                    kostya "Ой, ну ты выдал. Очевидно же, что 2D. 2D-графика требует меньше ресурсов и времени на создание спрайтов и анимаций, использует меньше технологий и инструментов, имеет упрощённую физику."
                    kostya "Если ты конечно собираешься делать амбициозный проект, на который уйдёт целая уйма времени, то ты можешь выбрать 3D графику, но в твоём случае тебе такое точно не нужно."

                    maincharacter "Использовать 2D графику.... записал! Если бы не ты, я бы мог начать пытаться сделать 3D игру и потратить кучу времени впустую. Спасибо тебе."
                    if count_question == 2:
                        kostya "Ладно, давай последний вопрос и я пойду. Дела появились."
            "Какие программы использовать для графики игры?":
                if third_question:
                    kostya "Ты уже это спрашивал"
                else:
                    $ count_question += 1
                    $ third_question = True
                    show gg calm1:
                        xalign 0.8
                        yalign 1.05
                    maincharacter "Какие программы ты используешь для графики в 2D играх?"
                    show kostya calm3:
                        xalign 0.2
                        yalign 1.05
                    kostya "Ну, обычно спрайты рисую Photoshop'е, программа мастхэв для художника. А вот анимации я иногда рисую в Spline."
                    kostya "Кстати, насчёт спрайтов. Если сроки у тебя сжатые, то лучше возьми спрайты с интернета и не парься, серьёзно."

                    maincharacter "А мне за это ничего не будет?"

                    kostya "Не будет, если ты их используешь исключительно для тестового задания. Однако если собираешься выпустить свою игру на какой-нибудь площадке на публику, ознакомься с лицензией спрайтов, являются ли они общественным достоянием, также узнай условие использования."

                    maincharacter "Понято, принято. Думаю, лучше всё-таки использую готовые спрайты и анимации из интернета. Если буду доделывать игру и выпускать на публику, то просто поменяю спрайты... наверное."

                    kostya "Трудоёмкая работа, но ты сам знаешь как поступить."
                    if count_question == 2:
                        kostya "Ладно, давай последний вопрос и я пойду. Дела появились."
            
    maincharacter  "Спасибо тебе! Твои советы очень помогут в разработке."
    kostya "Ага, Надеюсь, ещё увидимся, но уже как полноценные коллеги. До встречи."
    jump end_first_day


label duo_dudes:
    play music chill_2 fadeout 2
    show nastya speak with moveinright:
        xalign 0.9
        yalign 1.05
    show pavel calm1 with moveinright:
        xalign 0.6
        yalign 1.05
    show gg calm1 with moveinleft:
        xalign 0.2
        yalign 1.05   
    "За одним из столов сидят двое сотрудников – парень и девушка. Парень сосредоточенно работает за компьютером, а девушка что-то рисует на графическом планшете."
    show gg speak_:
        xalign 0.2
        yalign 1.05

    maincharacter "Привет! Извините, что отвлекаю. Я... эм... Мне было поручено сделать видеоигру, и если я её успешно сделаю, то меня примут к вам на работу."
    maincharacter "Осталась всего неделя, и мне... нужна помощь."

    show pavel calm2:
        xalign 0.6
        yalign 1.05
    "Парень отрывается от экрана и удивлённо смотрит на главного героя."

    pavel "Видеоигру?"
    pavel "За неделю?"
    pavel "Ты серьёзно?"

    show nastya calm2:
        xalign 0.9
        yalign 1.05
    nastya "Смелое заявление. У тебя уже что-нибудь готово?"

    show gg calm2:
        xalign 0.2
        yalign 1.05   
    maincharacter "Ну..."

    nastya "Что, только начал?"

    show gg facepalm_:
        xalign 0.2
        yalign 1.05  
    maincharacter  "Ещё не начал..."

    pavel "Боже... Можем помочь чем-нибудь?"
    show gg speak_:
        xalign 0.2
        yalign 1.05  
    maincharacter "Да, кем вы вообще работаете?"

    nastya  "Меня зовут Настя. Ну, я дизайнер, то есть художник. Моя задача — создавать концепты персонажей, окружения и интерфейса."
    nastya  "Всё, что видит игрок, проходит через мои руки. Например, сейчас я работаю над дизайном персонажей для нашего нового проекта."

    pavel "Меня зовут Павел, и я – программист. То, что рисует наша художница, остаётся просто картинкой, пока я не сделаю её интерактивной."
    pavel "Моя задача – реализовать все игровые механики, чтобы игрок мог управлять персонажами, взаимодействовать с миром и проходить уровни."

    menu:
        "Спросить совет у дизайнера.":
            maincharacter "Можете посоветовать что-нибудь по поводу дизайна в видеоигре за 7 дней?"
            show nastya calm2:
                xalign 0.9
                yalign 1.05
            nastya "Да, попробуй не переусложнять с графикой. Сделай стиль минималистичным, чтобы успеть всё нарисовать. Даже простые, но стильные персонажи могут отлично работать."
            nastya "Пиксельная графика идеально подойдёт для таких сроков, легкореализуемая и выглядит эстетично, рекомендую"
            nastya "Также не усложняй анимацию, чтобы не тратить на неё много времени. Анимируй мало-помалу лишь самые важные элементы. Создание анимаций не должно занимать больше времени, дизайн персонажа."
            nastya "Насчёт программ, я лично использую Aseprite для пиксельной графики, и очень даже рекомендую."

            show gg think_:
                xalign 0.2
                yalign 1.05  
            maincharacter "Вау! Очень полезные советы, записал, благодарю."

            nastya  "Всегда рада помочь!"

            "Вдруг телефон на столе начинает звенеть, ты видишь, что сработал будильник"
            show nastya calm1:
                xalign 0.9
                yalign 1.05
            nastya "Ой! У нас планёрка через 5 минут начинается, нам нужно спешить."

            show pavel calm3:
                xalign 0.6
                yalign 1.05
            pavel "Жаль, что не вышло нормально тебе помочь, может, ещё увидимся, а сейчас нам пора, бывай."

            maincharacter "Ничего страшного, и да, думаю, мы ещё встретимся."
        "Спросить совет у программиста.":
            maincharacter "Слушай, а можешь рассказать поподробнее про программирование? Какие есть важные моменты? С чего вообще начать?"
            show pavel calm3:
                xalign 0.6
                yalign 1.05
            pavel "Ну, смотри. Всё начинается с выбора движка. Если у тебя совсем нет времени, то лучше взять что-то простое, вроде Unity или Godot. Они удобны и хорошо подходят для инди-игр."
            pavel "Godot, например, имеет свой собственный язык GDscript, который ну уж ОЧЕНЬ прост в освоении, и своим синтаксисом очень похож на Python."
            pavel "Написать что-то на GDscript, например, логику игры, не составит труда, потому что сам язык очень простой и туториалов в интернете много, в общем, рекомендую."
            pavel "На Unity обычно пишут на языке C#. Язык хороший, но не такой простой в освоении, как GDscript, если ты с ним не знаком, то не рекомендую с ним работать."
            show pavel calm1:
                xalign 0.6
                yalign 1.05
            pavel "Далее, создание игровой логики."
            pavel "Коллизия. Система коллизий позволяет персонажу взаимодействовать с окружением: например, не проваливаться сквозь землю или сталкиваться с врагами. Обычно, это делается через физические движки, встроенные в Unity или Godot."
            pavel "Управление. С управлением всё понятно, разберёшься, просто обрабатываешь нажатия и привязываешь к объекту персонажа."
            show gg think_:
                xalign 0.2
                yalign 1.05  
            maincharacter  "А что насчёт прыжков в платформере? как это реализуется?"

            pavel "Обычно, для прыжка достаточно простой команды в коде, которая добавляет импульс вверх. Например, в Unity это AddForce, а в Godot – метод apply_impulse."
            pavel "А чтобы персонаж не прыгал бесконечно, можно добавить проверку, касается ли он земли, всё просто."
            pavel "И на последок скажу: ни в коем случае не используй Unreal Engine для быстрой разработки, тем более этот движок предназначен для 3D-игр, но никак не для 2D."

            maincharacter "И... дописано! Спасибо за советы, можно еще спросить про..."   

            "Вдруг телефон на столе начинает звенеть, ты видишь, что сработал будильник"
            show nastya calm1:
                xalign 0.9
                yalign 1.05
            nastya "Ой! У нас планёрка через 5 минут начинается, нам нужно спешить."

            show pavel calm3:
                xalign 0.6
                yalign 1.05
            pavel "Жаль, что не вышло нормально тебе помочь, может, ещё увидимся, а сейчас нам пора, бывай."

            maincharacter "Ничего страшного, и да, думаю, мы ещё встретимся."
    
    
    jump end_first_day