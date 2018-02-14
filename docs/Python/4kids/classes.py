

class Things:
    pass

class Animate(Things):
    def breathe(self):
        print('делает вдох')
        
    def move(self):
        print('идёт вперёд')
        
    def eat(self):
        print('усиленно жуёт')

class Mammals(Animate):
    def feed_with_milk(self):
        print('кормит детёныша молоком')

class Giraffes(Mammals):
    def __init__(self, spots):
        self.giraffe_spots = spots
        
    def eat_leaves_from_trees(self):
        self.eat_food()
        
    def find_food(self):
        self.move()
        print("Нашёл еду!")
        self.eat_food()
        
    def horovod(self):
        self.move()
        self.move()
        self.move()
        self.move()

    def left_foot_forward(self):
        print('переставляет левую ногу вперёд')

    def right_foot_forward(self):
        print('переставляет правую ногу вперёд')

    def left_foot_backward(self):
        print('переставляет левую ногу назад')

    def right_foot_backward(self):
        print('переставляет правую ногу назад')

    def dance(self):
        left_foot_forward(self)
        left_foot_backward(self)
        right_foot_forward(self)
        right_foot_backward(self)
        left_foot_forward(self)
        right_foot_forward(self)
        left_foot_backward(self)
        right_foot_backward(self)

Gyro = Giraffes(60)

Harry = Giraffes(77)

Gyro.move()
Harry.feed_with_milk()
