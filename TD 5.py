
from tkinter import Tk, Canvas, Label, Button, TOP, LEFT, RIGHT, BOTTOM
from random import randrange
from math import sqrt

class Target:

    def __init__(self):
        self.__root = Tk()
        self.__root.geometry()
        self.__canvas = Canvas(self.__root, width=400, height=400, bg="red")
        self.__canvas.pack(side=TOP, padx=5, pady=5)
        self.draw_target()
        quit_button = Button(self.__root, text="Quit", command=self.__root.destroy)
        quit_button.pack(side=RIGHT, padx=3, pady=3)
        self.__button_shoot = Button(self.__root, text="Shoot", command=self.__shoot)
        self.__button_shoot.pack(side=LEFT, padx=5, pady=5)
        self.__score = 0
        self.__label_score = Label(self.__root, text=f"score : {self.__score}")
        self.__label_score.pack(side=BOTTOM, padx=5, pady=5)
        self.__tries = 5
        self.__root.bind_all('f', self.__oneshot)



    def execute(self):
        self.__root.mainloop()

    def draw_circle(self, x, y, r, color):
        """Draw a circle of centre (x, y) and radius r."""
        self.__canvas.create_oval(x - r, y + r, x + r, y - r, outline='red', fill=color)

    def draw_target(self):
        """Draw the target on the canvas."""
        self.__canvas.create_line(200, 0, 200, 400, fill='red')
        self.__canvas.create_line(0, 200, 400, 200, fill='red')
        circle = 1
        for radius in range(180, 29, -30):
            if circle == 5:
                self.draw_circle(200, 200, radius, 'red')
                self.__canvas.create_text(190, 210 - radius, text=f"{circle}", font=('Times', '12', 'bold'), fill='ivory')
            else:
                self.draw_circle(200, 200, radius, 'ivory')
                self.__canvas.create_text(190, 210 - radius, text=f"{circle}", font=('Times', '12', 'bold'), fill='red')
            circle += 1
        self.__canvas.create_line(200, 0, 200, 400, fill='red')
        self.__canvas.create_line(0, 200, 400, 200, fill='red')

    def __increment_score(self, x, y):
        distance = sqrt((x - 200) ** 2 + (y - 200) ** 2)
        self.__score += (6 - distance // 30) * (distance < 6 * 30)

    def __oneshot(self,event):
        "shoot with the "f" touch"
        if self.__tries > 0 :
            self.__shootonce()
            self.__tries -= 1

    def __shoot(self):
        if self.__tries > 1:
            self.__shootonce()
            self.__tries -= 1
        else:
            self.__shootonce()
            self.__button_shoot['state'] = 'disabled'

    def __shootonce(self):
        (x,y) = (randrange(400),randrange(400))
        self.draw_shot(x,y)
        self.draw_circle(x, y, 5, 'black')
        self.__increment_score(x, y)
        self.__label_score['text'] = f"score : {self.__score}"

    def draw_shot(self, x, y):
        self.__canvas.create_oval(x - 5, y + 5, x + 5, y - 5, fill='black')




if __name__ == '__main__':
    target = Target()
    target.execute()
