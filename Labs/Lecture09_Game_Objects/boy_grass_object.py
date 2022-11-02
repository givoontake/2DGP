from pico2d import *
import random

# Game object class here

class Grass:
    def __init__(self):  # 생성자 - 객체의 속성에 대한 초기값을 만들어줌
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x, self.y = random.randint(100,700), 90
        self.frame = random.randint(0,7)

    def update(self): # 소년의 행위 구현
        self.x +=5 #속성값을 바꾸믕로써 행위(오른쪽으로 이동)을 구현
        self.frame = (self.frame+1) % 8

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


# grass = Grass() Grass 라는 클래스로부터, grass 객체를 생성한다.

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code

open_canvas()

grass = Grass()  # 잔디 객체 생성
# boy = Boy() # 소년 객체 생성

team = [Boy() for i in range(11)]

running = True

while running:
    handle_events()  # 키 입력 처리
    for boy in team:
       boy.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()

    delay(0.05)

# game main loop code

# finalization code