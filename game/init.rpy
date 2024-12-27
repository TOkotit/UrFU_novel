$ renpy.music.set_volume(0.6)



define maincharacter = Character("[gg_name]", image="gg", color="#44e010", callback=name_callback, cb_name="gg")
define seva = Character("Сева", image="seva", color="#676346", callback=name_callback, cb_name="seva")
define kostya = Character("Костян", image="kostyan", color="#25292c", callback=name_callback, cb_name="kostyan")
define pavel = Character("Павел", image="pavel", color="#54575a", callback=name_callback, cb_name="pavel")
define nastya = Character("Настя", image="nastya", color="#678368", callback=name_callback, cb_name="nastya")
define boss = Character("Босс", image="boss", color="#ffffff", callback=name_callback, cb_name="boss")

define game_choice = "Not choiced"

image gg calm1 = At("gg stand", sprite_highlight("gg"))
image gg angry_ = At("gg angry", sprite_highlight("gg"))
image gg facepalm_  = At("gg facepalm", sprite_highlight("gg"))
image gg speak_ = At("gg speak", sprite_highlight("gg"))
image gg calm2 = At("gg stand1", sprite_highlight("gg"))
image gg think_ = At("gg think", sprite_highlight("gg"))
image gg talktophone_ = At("gg talkphone", sprite_highlight("gg"))
image gg looktophone_ = At("gg lookphone", sprite_highlight("gg"))
image gg shock_ = At("gg shock", sprite_highlight("gg"))

define gg_phone = Character("[gg_name]", kind=nvl, image="gg stand", callback=Phone_SendSound)
define gendir_phone = Character("Гендир", kind=nvl, callback=Phone_ReceiveSound)


image seva calm1 = At("seva stand", sprite_highlight("seva"))
image seva calm2 = At("seva stand1", sprite_highlight("seva"))
image seva thumbsup_ = At("seva thumbsup", sprite_highlight("seva"))

image kostya calm1 = At("kostyan stand", sprite_highlight("kostyan"))
image kostya calm2 = At("kostyan stand1", sprite_highlight("kostyan"))
image kostya calm3 = At("kostyan stand2", sprite_highlight("kostyan"))

image nastya calm1 = At("nastya stand", sprite_highlight("nastya"))
image nastya calm2 = At("nastya stand1", sprite_highlight("nastya"))
image nastya speak_ = At("nastya speak", sprite_highlight("nastya"))

image pavel calm1 = At("pavel stand", sprite_highlight("pavel"))
image pavel calm2 = At("pavel stand1", sprite_highlight("pavel"))
image pavel calm3 = At("pavel stand2", sprite_highlight("pavel"))


image boss hands_ = At("boss hands", sprite_highlight("boss"))
image boss calm = At("boss stand", sprite_highlight("boss"))
image boss speak_ = At("boss speak", sprite_highlight("boss"))

define audio.mus_morning = "audio/music/Sun_Arow_Deep_Cover.mp3"
define audio.mus_aWeekNoWay = "audio/music/Ben Salisbury, Geoff Barrow - The Alien.mp3"
define audio.seva_theme = "audio/music/She_Meditates.mp3"
define audio.kostyan_theme = "audio/music/bad to the kostyan.mp3"
define audio.chill_1 = "audio/music/Guided_Meditation.mp3"
define audio.chill_2 = "audio/music/Daisuke.mp3"
define audio.evening_chill = "audio/music/evening_chill.mp3"
define audio.morning_chill = "audio/music/morning_chill.mp3"
define audio.I_WANT_PANDEMONIKA = "audio/music/mist_of_pandemonika.mp3"
define audio.Kolmisilmä = "audio/music/Kolmisilmä.mp3"
define audio.Holy_Moly_Mountain = "audio/music/Holy Moly Mountain.mp3"
define audio.Daddy_Long_Legs_Surprise = "audio/music/Daddy Long-Leg's Surprise.mp3"
define audio.spooki_skary_coridor = "audio/music/mus_disturbing.mp3"
define audio.boss_like_hurting_other_people = "audio/music/Silver_Lights.mp3"

