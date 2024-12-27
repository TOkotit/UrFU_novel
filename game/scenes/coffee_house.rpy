label coffee_house:
    scene bg think_fast_chucklenuts with fade
    voice "audio/sounds/think-fast-chucklenuts.mp3"
    ""
    scene bg white_space
    voice "audio/sounds/bzzzzzzzzzzzzzzzzzzzzzz.mp3"
    ""
    "А я говорил, что не закончено"
    jump seeking_for_team
    return

init:
    transform txt_up:
        yalign 1.5
        linear 300 yalign -50

init python:
    f = open(renpy.loader.transfn("resources/b_movie_script.txt"),"r")
    s = f.readlines()
    my_credits = ''.join(s)
    f.close()

label credits:
    scene bg end with fade
    pause 5
    # scene black with dissolve
    # show text my_credits at txt_up
    # pause 15
    return