class Transport:
    counter = 0
    def __init__(self, model, year,color):
        self.model = model
        self.year = year
        self.color = color
        Transport.counter +=1

    def change_color(self, new_color):
            self.color = new_color
class Plane(Transport):
    def __init__(self,model,year,color):
        super().__init__(model,year,color)




class Car(Transport):

    def  __init__(self,model,year,color,):
        super().__init__(model,year,color)

    def drive(self,city):
        print(f'Car {self.model} is to driving to {city}')



print(f'Factory Car produced:{Car.counter}')
my_number = 7

honda_car = Car(      f'Honda civic', f'2000' , f'blue'    )
print(f'MODEL:{honda_car.model}',f'YEAR:{honda_car.year}',
       f'COLOR:{honda_car.color}')

BMW_car = Car(model='M5',year='2005',color= 'black')
BMW_car.change_color('white')
print(f'MODEL:{BMW_car.model}',f'YEAR:{BMW_car.year}',
       f'COLOR:{BMW_car.color}')
honda_car.drive('OSH')
plane_fly = Plane(f'samalet' , f'2022',f'red' )
print(f'MODEL:{plane_fly.model}',f'YEAR:{plane_fly.year}',f'COLOR:{plane_fly.color}')
Car.counter +=1
print(f'Factory Car produced:{Car.counter}')

# print(honda_car.drive)



