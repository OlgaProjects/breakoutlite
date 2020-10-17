import random

class Ball:
    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color) #отрисовка шарика
        self.canvas.move(self.id, 250, 100) #координаты перемещения
        self.canvas_width = self.canvas.winfo_width()

        starts = [-2, -1, 1, 2] # задаём список возможных направлений для старта

        random.shuffle(starts) #перемешали рандомно позиции

        self.x = starts[0] #горизонтально
        self.y = -2 # вертикально

        self.canvas_height = self.canvas.winfo_height() #изменение координат, обозначение высоты, определение по у
        self.canvas_weight = self.canvas.winfo_width() # ширина

        self.hit_bottom = False # узнать не коснулся ли мяч


    def hit_paddle(self, pos): # определяем когда коснется платформы
        paddle_pos = self.canvas.coords(self.paddle.id)
        # условия касания
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:

                self.score.add_point()
                return True

        return False

    def draw(self, color_end_text): # сама отрисовка шарика и платформы
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id) # координаты шарика
        # если шарик падает сверху
        if pos[1] <= 0: # не падает ли вниз
            self.y = 2  # низ

        if pos[3] >= self.canvas_height: # платформа за пределами шарика
            self.hit_bottom = True #игра завершает действие
            self.canvas.create_text(250, 120, text='Game over :(', font=('Courier', 30), fill=color_end_text) #font шрифт
            
        if self.hit_paddle(pos) == True: #если шарик коснулся платформы
            self.y = -2 # вверх

        if pos[0] <= 0:
            self.x = 2 # левая стенка

        if pos[2] >= self.canvas_width: #если будет касаться правой стенки
            self.x = -2


class Paddle:

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)

        start_1 = [40, 60, 120, 150, 180, 200]
        random.shuffle(start_1)

        self.start_pos_x = start_1[0]
        self.canvas.move(self.id, self.start_pos_x, 450) #стартовая позиция, всегда сверху 300 px

        self.x = 0 # пока платформа никуда не движется, поэтому изменений по оси х нет
        self.canvas_width = self.canvas.winfo_width() # платформа узнаёт свою ширину

        self.game_started = False

        self.canvas.bind_all("<KeyPress-Right>", self.turn_right) # если нажата стрелка вправо — выполняется метод turn_right()
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)  # если стрелка влево — turn_left()
        self.canvas.bind_all("<KeyPress-Return>", self.start_game) # нанчло игры


        # движемся вправо 
    def turn_right(self, event):
            # будем смещаться правее на 2 пикселя по оси х 
            self.x = 2

    def turn_left(self, event):
            # будем смещаться левее на 2 пикселя по оси х
            self.x = -2

    def start_game(self, event):
        self.game_started = True

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id) #получаем стартовые позиции

        if pos[0] <= 0:
            self.x = 0

        elif pos[2] >= self.canvas_width: # если зашла за границы правого края - stop
            self.x = 0


class Score:

    def __init__(self, canvas, color):

        self.canvas = canvas
        self.score = 0
        self.id = canvas.create_text(450, 10, text=self.score, font=('Courier', 20), fill=color)

    def add_point(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score) # пишем новое значение счёта









