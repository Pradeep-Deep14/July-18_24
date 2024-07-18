class Vehicle:
    def __init__(self,color):
        self.color=color

class Car(Vehicle):
    def __init__(self,color,model):
        super().__init__(color)
        self.model=model

my_car=Car("Red","Toyota")
print(my_car.model)