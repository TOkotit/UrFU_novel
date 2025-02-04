label sit_to_the_laptop:
    show gg think_
    play music chill_1 fadeout 1
    "Ты принимаешь душ, ешь, садишься за ноутбук."
    maincharacter "Ну, за дело!"
    maincharacter "Так, первое, начать нужно с... идеи! Концепт, механики, все дела."
    maincharacter "Я буду делать..."
    menu:
        "Пиксельный платформер с уникальными механиками.":
            jump ok_its_platformer
        "3D-шутер, где главный герой может управлять гигантскими роботами в сражении.":
            jump ok_its_shooter
        "Казуальная 2D-игра про кофейню, где нужно управлять заведением.":
            jump ok_its_casual
    jump sit_to_the_laptop

label ok_its_platformer:
    "Окей, пиксельный платформер, что будешь делать, по-быстрому нарисуешь заглушки, чтобы перейти к программированию логики и физики или нарисуешь полноценные спрайты?"
    menu:
        "Быстро нарисовать заглушки на время":
            show gg calm2
            "Ты нарисовал за пару минут заглушки, которые будут заменять разные объекты"
            "Так, теперь самое главное."
            "Где ты будешь разрабатывать игру?"
            menu:
                "Unreal Engine":
                    $ game_choice = "blue"
                    show gg think_
                    "Ты пытаешься разобраться в движке, как на нём работать, пытаешься адаптировать всё будущую 2D игру, пытаешься сделать тестовый уровень, сделать управление, коллизию и физику."
                    "На это уходит {sc}{color=#9b2d30}{b}ЦЕЛЫЙ ДЕНЬ{/b}{/color}{/sc}, и ты только сделал управление, коллизию и простенький уровень без каких-либо механик."
                    jump end_day_2
                "Godot":
                    $ game_choice = "violet"
                    show gg think_
                    "Ты выбираешь Godot и узнаешь, что на нём можно использовать либо C#, либо GDscript."
                    "Ты выбираешь встроенный язык GDScript, потому что он гораздо проще C# и является родным языком Godot."
                    "И вот ты Начинаешь делать тестовый уровень, управление и коллизию."
                    "Язык оказался очень простым для освоения, поэтому ты с лёгкостью написал всё нужное за {bt=5}{color=#f8f32b}полдня.{/color}{/bt}"
                    jump platformer_doing
    
                "Unity":
                    $ game_choice = "violet"
                    show gg think_
                    "Ты выбираешь Unity, находишь нужные библиотеки для создания видеоигры, подготавливаешь тестовый уровень, управление и коллизию."
                    "На это уходит {bt=3}{color=#b300b3}полдня{/color}{/bt}..."
                    jump platformer_doing

        "Начать рисовать полноценные спрайты":
            show gg calm2
            $ game_choice = "salat"
            "Ты когда-то увлекался рисованием, поэтому нарисовать что-то не было весомой проблемой."
            "Ты выбираешь Aseprite, потому что тебе когда-то рекомендовали эту программу для рисования пиксельной графики."
            "Несмотря на все плюсы, ты никогда не пользовался этой программе, и нужно ещё к ней привыкнуть и понять, что к чему."
            "Однако ты ещё не выбрал стиль, атмосферу и примерный вид игры. Ты взял из головы разные образы и приступил рисовать, постепенно изучая новую для себя программу."
            "Ты рисуешь, но, кажется, некоторые спрайты даже не будут нужны в твоей игре. Ты рисуешь всё подряд, и на это уходит {sc}{color=#9b2d30}{b}ЦЕЛЫЙ ДЕНЬ.{/b}{/color}{/sc}"
            jump end_day_2

label ok_its_shooter:
    show gg think_
    "Так-с, тот самый амбициозный шутер про роботов, который тебе снился. Не зря же, наверное, он тебе снился?"
    "Может, это знак?"
    "Займёмся дизайном уже после того, как сделаем прототип, а сейчас пора подготовить тестовую зону, физику и управление."
    "Какой игровой движок будешь использовать?"
    $ game_choice = "green"
    menu:
        "Unreal Engine":
            show gg calm1
            "Ты выбираешь Unreal Engine. Ты понимаешь, что использовать его довольно трудно для скромного проекта, но трудности тебя не пугают."
            "Также тут используется C++, не такой уж и лёгкий язык, однако его основы ты уже знаешь, нужно лишь вспомнить кое-что."
            "Ты начинаешь изучать, как всё устроено в это игровом движке и как работать с 3D графикой, начинаешь подготавливать тестовую зону, управление, геймплей."
            "На всё это у тебя уходит {sc}{color=#9b2d30}{b}ЦЕЛЫЙ ДЕНЬ{/b}{/color}{/sc}! Нелегка, однако, разработка такого проекта на этом движке."
        "Godot":
            show gg calm1
            "Ты выбираешь Godot и узнаешь, что на нём можно использовать либо C#, либо GDscript."
            "Ты выбираешь встроенный язык GDScript, потому что он гораздо проще C# и является родным языком Godot."
            "И вот ты начинаешь делать тестовую зону, управление, некоторые базовые механики, и из-за трудностей, связанных с 3D-графикой всё это занимает у тебя {sc}{color=#9b2d30}{b}ЦЕЛЫЙ ДЕНЬ{/b}{/color}{/sc}..."
        "Unity":
            show gg calm1
            "Мгм, Unity."
            "Значит, тебе придётся писать на C#. Ты, конечно, знаешь основы этого языка и его синтаксис, но кое-что нужно припомнить, и узнать, какие библиотеки использовать."
            "Чтобы всё вспомнить, понять как работать с 3D-графикой, подготовить, тестовую зону, геймплей, физику, управление, у тебя уходит{sc}{color=#9b2d30}{b}ЦЕЛЫЙ ДЕНЬ{/b}{/color}{/sc}."
    jump end_day_2

label ok_its_casual:
    show gg think_
    "Мгм, казуалка про кофейню. Графика в ней должна быть не пиксельной, иметь тёплые цвета и быть приятная глазу"
    "Ты тратишь немного времени, чтобы продумать точный концепт и геймплей."
    show gg calm1
    "Чтобы сделать игру оригинальной, ты будешь управлять {atl=0.3,drop_text~#~1.5}{color=#006400}\nинопланетным{/color}{/atl} кафе, где нужно обслуживать пришельцев."
    "Нужно будет улучшать заведение, закупать продукты, обновлять меню, обслуживать клиентов."
    "Теперь нужно понять, с чего начать, какой движок будешь использовать?"
    $ game_choice = "yellow"
    menu:
        "Godot":
            show gg calm1
            "Ты выбираешь Godot и  поскольку его родной язык GDScript, ты решаешь, что будешь писать именно на нём."
            "За пару часов ты подготовил тестовую зону, где будешь тестировать управление, механики и прочее."
        "Unity":
            show gg calm1
            "Мгм, Unity. Значит, тебе придётся писать на C#."
            "Ты, конечно, знаешь основы этого языка и его синтаксис, но кое-что нужно припомнить, и узнать, какие библиотеки использовать."
            "На вспоминание всего этого у тебя ушло {bt=7}{color=#f754e1}~2 часа{/color}{/bt} подготовки."
    "Ты начинаешь программировать логику игры, механику того, как приходят клиенты, что хотят, и сколько платят."
    "Также ты реализовываешь то, как будет копиться внутриигровая валюта."
    "На всё это у тебя уходит {sc}{color=#9b2d30}{b}ЦЕЛЫЙ ДЕНЬ{/b}{/color}{/sc} усердной работы..."
    jump end_day_2


label platformer_doing:
    show gg clam2
    "Ты пытливо работал над тем, чтобы создать объект персонажа, который можно передвигать клавишами W,A,S,D и его столкновение с объектами."
    "Ты сделал совсем немного, но ты чувствуешь гордость за то, что смог сделать. Запомни это чувство, оно будет мотивировать тебя."
    "Ты совсем не устал, наоборот, ты жаждешь продолжать работу над игрой, поэтому, отдохнув пару часиков и перекусив, ты снова продолжаешь делать проект."
    "На этот раз тебе нужно продумать уникальные для твоей игры механики."
    "Ты долго размышляешь над тем, какими механиками скрасить геймплей и внедряешь в свою игру..."
    "Двойной прыжок, прыжки от стен и переключение между мирами, чтобы определённые объекты существовали лишь в определённом мире."
    show gg think_
    "Двойной прыжок - довольно легкореализуемая механика, ты быстро с ней справляешься."
    "Однако прыжки от стен и переключение между мирами вызвали у тебя трудности, но ты ведь не из робких, тебе всё по плечу, ведь так?"
    "Именно. Найти интересующую тебя информацию в интернете оказалось проще простого! Куча туториалов и гайдов."
    "Ты реализовываешь почти все механики, которые ты хотел за один полный день."
    jump end_day_2




