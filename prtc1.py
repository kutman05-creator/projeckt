class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory


    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value


    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value


    def make_computations(self):
        return f"Результат вычислений: CPU x Memory = {self.__cpu * self.__memory}"


    def __str__(self):
        return f"Computer(CPU: {self.__cpu} GHz, Memory: {self.__memory} GB)"


    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __ge__(self, other):
        return self.memory >= other.memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list


    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value


    def call(self, sim_card_number, call_to_number):
        if sim_card_number == 1:
            return f'Идет звонок на номер{call_to_number} с сим-карты-{sim_card_number} beeline'
        elif sim_card_number == 2:
            return  f'Идет звонок на номер{call_to_number} с сим-карты-{sim_card_number} Megacom'

        else:
            return "Неверный номер SIM-карты"


    def __str__(self):
        return f"Phone(SIM Cards: {self.__sim_cards_list})"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)


    def use_gps(self, location):
        return f"Построение маршрута до {location}..."


    def __str__(self):
        return (f"SmartPhone(CPU: {self.cpu} GHz, Memory: {self.memory} GB, "
                f"SIM Cards: {self.sim_cards_list}")



computer = Computer(3.5, 16)
phone = Phone(["Beeline", "MegaCom", "O!"])
smartphone1 = SmartPhone(2.8, 8, ["Beeline", "MegaCom"])
smartphone2 = SmartPhone(3.2, 32, ["O!", "MegaCom"])


print(computer)
print(phone)
print(smartphone1)
print(smartphone2)


print("\n=== Методы объектов ===")
print(computer.make_computations())
print(phone.call(1, "+996 777 99 88 11"))
print(smartphone1.use_gps("Бишкек"))


print("\n=== Сравнение объектов ===")
print(smartphone1 < smartphone2)  # True
print(smartphone1 == computer)    # False
print(smartphone2 > smartphone1)  # True


print("\n=== Изменение атрибутов ===")
smartphone1.memory = 16
print(smartphone1)
print(smartphone1 == computer)  # True




