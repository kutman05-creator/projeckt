class Figure:
    unit = "cm"
    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass
class Square(Figure):
    def __init__(self,side_length):
        self.__side_length = side_length

    def calculate_area(self):

        return self.__side_length**2
    def info(self):
        print(f'Square side length:{self.__side_length} {self.unit} , area:{self.calculate_area()} {self.unit}')
class Rectangle(Figure):
    def __init__(self,length,width):
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length *self.__width

    def info(self):
        print(f'Rectangle length :{self.__length} {self.unit} , width:{self.__width} {self.unit},area:{self.calculate_area()} {self.unit}')

list1 = [Square(5),Square(17),Rectangle(8,6,),Rectangle(9,3),Rectangle(10,13)]
for i in list1:
    i.info()

#

