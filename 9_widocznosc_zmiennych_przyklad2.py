class HouseProject:

    def __init__(self, area, number_of_floors):
        self.__area = area
        self.__number_of_floors = number_of_floors

    def info(self):
        print(f'Area: {self.__area}')
        print(f'Number of floors: {self.__number_of_floors}')


def info_ext(instance):
    print(f'Area: {instance._HouseProject__area}')
    print(f'Number of floors: {instance._HouseProject__number_of_floors}')


project = HouseProject(100, 1)
project.info()

info_ext(project)
