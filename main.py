from tkinter import *
import time

from settings import *
from objects import *

tk = Tk() #объект ткинтера, наше игровое поле

tk.title(GAME_NAME)
tk.resizable(0,0) # чтобы окно не дивгалось
tk.wm_attributes('-topmost', 1) #чтобы ничего не перекрывалось, был поверх всех форм

canvas = Canvas(tk, width=WIDTH, height=HEIGHT, highlightthickness=0) #высота, ширина обводка в рамке
canvas.pack() # указываем, что есть координаты
tk.update() #обновление после отрисовки

paddle = Paddle(canvas, COLOR_PADDLE)
score = Score(canvas, COLOR_SCORE)
ball = Ball(canvas, paddle, score, COLOR_BALL)

while not ball.hit_bottom:

    if paddle.start_game:
        ball.draw(COLOR_END_TEXT)
        paddle.draw()

    tk.update_idletasks() #дорисовка
    tk.update() #обновление самого окна'''
    
    time.sleep(0.01) #плавность движений, с небольшой задержкой

time.sleep(3)





