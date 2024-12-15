class Computer:
    def __init__(self,cpu,memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu
    @property
    def memory(self):
        return self.__memory
    @cpu.setter
    def cpu(self,value):
         self.__cpu = value
    @memory.setter
    def memory(self,value):
        self.__memory = value

    def make_computations(self):


    def __lt__(self, other):
        return self.__memory < other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory


class Phone:
    def __init__(self,sim_cards_list):
        self.call_to_number = None
        self.sim_card_list = None
        self.__sim_cards_list = sim_cards_list

    @property
    def get_sim(self):
        return self.__sim_cards_list
    @get_sim.setter
    def get_sim(self,values):
        self.__sim_cards_list = values

    def call(self, sim_card_number,call_to_number):

        self.sim_card_list = sim_card_number
        self.call_to_number = call_to_number

    def __str__(self):
        return f"Идет звонок на номер {self.call_to_number} c сим карты {self.sim_card_list}"

class Smartphone(Computer,Phone):
    def __init__(self,__cpu,__memory,sim_cards_list):
        Computer.__init__(self,__cpu,__memory,)
        self.sim_card_list = sim_cards_list

    def use_gps(self,location):
        print(f'building route to {location}')



