from tkinter import *
import random



        

class game:
    def __init__(self):
        self.root=Tk()
        self.RUN = False

        self.frame = Frame(bg="#006c96")#0a1c03
        self.frame.pack()

        self.canvas = Canvas(self.frame, bg="#000a2d",width=600,height=400)
        self.canvas.pack()

##        self.scores=Label(self.frame, bg="black", fg="white")
##        self.scores.pack()



        self.button=Button(self.frame, bg="#2ac4ff", fg="#03325e", text="Click to start" ,command = self.start)
        self.button.pack()


    def start(self):
        self.RUN = True
        self.height = 400
        self.width = 600
        self.x = 20
        self.y = 20
        
        self.score = 0
        self.speed_x=20
        self.speed_y=0
        self.speed = 150
##        self.speedX = 20
##        self.speedY = 0
        self.speed_v=20

        self.canvas.bind('<KeyPress>',self.kb_callback)
        self.canvas.focus_set()
        self.run()


    def run(self):  
        if self.RUN is True:
##            self.scores["text"] = "Score: " + str(self.score) 
            self.create_food()
            self.create_snake()
            self.create_box()
            self.create_box2()
            self.create_box3()
            self.draw()
            self.paint()


    def paint(self):
        self.button.destroy()
        self.canvas.delete(ALL)
        self.create_box()
        self.create_box3()
        self.create_box2()
        self.create_food()
        self.create_snake()


            


    def create_food(self):
        self.posx = 20 * random.randint(1, (self.width - 20)/20 )
        self.posy = 20 * random.randint(1, (self.height - 20)/20 )
##        self.posx = 300
##        self.posy = 200
        self.food = self.canvas.create_oval(self.posx, self.posy, self.posx + 20,self.posy+20, fill = "red")
        


    def create_snake(self):
        self.snake = self.canvas.create_rectangle(self.x, self.y, self.x+20,
                                                  self.y+20, fill = "#0078ff")

    def create_box (self):
        self.boxX = 0
        self.boxY = 0
        self.box = self.canvas.create_rectangle(self.boxX , self.boxY  , self.boxX + 240, self.boxY + 140, fill="#08227c")

    def create_box2 (self):
        self.box2X = 300
        self.box2Y = 200
        self.box2 = self.canvas.create_rectangle(self.box2X + 60,self.box2Y +60, self.box2X -60, self.box2Y -60, fill= "#f69500")

    def create_box3(self):
        self.box3X = 600
        self.box3Y = 400
        self.trap = self.canvas.create_rectangle(self.box3X , self.box3Y  , self.box3X -240 , self.box3Y -140, fill="#08227c")



    def eat_food(self):
        if self.pos_x == self.x and self.pos_y == self.y:
            self.score = self.score + 50
            self.canvas.delete(self.food)
            self.create_food()

    def eat_inbox(self):
        if self.boxX   < self.pos_x and  self.boxY  < self.pos_y:
            if self.boxX +240 > self.pos_x and self.boxY +  140  > self.pos_y:
                if self.pos_x == self.x and self.pos_y == self.y:
                    self.speed -= 10
                    self.score = self.score + 5
                    self.canvas.delete(self.food)
                    self.create_food()

    def eat_inbox2(self):
        if self.box2X  - 60 < self.pos_x and  self.box2Y - 60 < self.pos_y:
            if self.box2X + 60 > self.pos_x and self.box2Y +  60  > self.pos_y:
                if self.pos_x == self.x and self.pos_y == self.y:
                    self.speed += 100
                    self.score = self.score + 5
                    self.canvas.delete(self.food)
                    self.create_food()

    def eat_inbox3(self):
        if self.box3X  > self.pos_x and  self.box3Y   > self.pos_y:
            if self.box3X - 240 <= self.pos_x and self.box3Y - 140  <= self.pos_y:
                if self.pos_x == self.x and self.pos_y == self.y:
                    self.speed -= 10

                    self.score = self.score + 5
##                    self.canvas.delete(self.snake)
                    self.canvas.delete(self.food)
##                    self.snake = self.canvas.create_rectangle(self.x, self.y, self.x+20, self.y+20, fill = "#ae0072")
                    self.create_food()

            
        
    def kb_callback(self, event):
        if event.keysym == "w" or event.keysym == "W":
            self.speed_x= 0
            self.speed_y= -self.speed_v
        elif event.keysym == "s" or event.keysym == "S":
            self.speed_x = 0
            self.speed_y = self.speed_v
        elif event.keysym == "a" or event.keysym == "A" :
            self.speed_x = -self.speed_v
            self.speed_y = 0
        elif event.keysym == "d" or event.keysym == "D" :
            self.speed_x = self.speed_v
            self.speed_y = 0

    def hit_wall(self):
        if self.x <= -1 or self.x >= 600 or self.y <= -1 or self.y >= 400:
            
            self.RUN = False
            self.canvas.delete(ALL)
            self.canvas.create_text(300, 200, text="Score : "+ str(self.score),font="Hobostd 30", fill="#004ed2")

    def update_food(self):
        self.pos_x = self.posx
        self.pos_y = self.posy
        
            
            

    def update_snake(self):
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y


        
    def draw(self):
        if self.RUN is True:
            self.update_food()
            self.update_snake()

            self.eat_inbox()
            self.eat_inbox2()
            self.eat_inbox3()
            self.hit_wall()
            self.canvas.move(self.snake, self.speed_x, self.speed_y)
    
            self.update_food()
            self.eat_food()
            
            self.canvas.after(self.speed, self.draw)
        


game()


