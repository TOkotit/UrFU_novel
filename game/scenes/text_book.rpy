#кнопка
screen button_book:
    imagebutton :
        idle "book_button2"
        hover "book_button1"
        action ui.callsinnewcontext("afq_screen_label")
        xalign 0.02 ypos 94

#первый экран
screen afq_screen:
    frame:
        background "gui/bg_book.png" # фон
        has vbox:
            spacing 15

    viewport:
        xalign 0.07 ypos 130 xysize (250, 500)
        child_size (1000, None)
        scrollbars "vertical"
        spacing 5
        draggable True
        mousewheel True
        arrowkeys True

        vbox:
            label "Потрепаная терадь"
            label "{color=#000000}{size=-5}........................{/size}{/color}"
            label "{size=-5}Верхний мир{/size}"
            label "{color=#000000}{size=-5}.............................{/size}{/color}"
            label "{size=-5}Легенды{/size}"
            textbutton "Великая Война" action Show("article_12")

label afq_screen_label:
    call screen afq_screen
    return

#второй экран

screen article_12:
    tag article
    frame:
        background "gui/bg_book2.png" # фон
        has vbox:
            spacing 15
    viewport:
        xalign 0.6 ypos 130 xysize (400, 500)
        child_size (1000, None)
        scrollbars "vertical"
        spacing 5
        draggable True
        mousewheel True
        arrowkeys True
        vbox:
            xalign 0.8 ypos 0.2
            text "{color=#653bcf}{size=+10}Великая Война{/size}{/color}  "
            text "{color=#000000}{size=-4} ваш текст {/size}{/color}  "
