from services.finddiagonal import diag


'''Класс комната.
            angle - количество углов в комнате
            h - высота комнаты'''

class Room:
    def __init__(self, angle: int) -> None:
        self.name = ''
        self.angle_side_room = {chr(i+65)+chr(i+66): 0 for i in range(angle)}
        self.diagonal_room = diag(angle)
        self.height_room = 0
        self.perimetr = 0
        self.room_area = 0
        self.walls_area = 0
        self.windows = []
        self.doors = []
    
    def get_side_room(self, fun):
        s = fun()
        print(s)

    def __str__(self) -> str:
        return self.name

        
'''Класс Окно.
            h - высота окна.
            w - ширина окна
            с - (растояние от левой стены до окна, от пола до окна)'''
class WinOpening:
    def __init__(self, h: int, w: int, c: tuple) -> None:
        self.height_opening = h
        self.width_opening = w
        self.coord = c
        self.len_slopes = 0
        self.len_windowsill = 0
        self.area_win = 0


''' Класс дверь.
                с - растояние от левого угла стены до двери
                w - ширина двери
                h - высота двери'''
class DoorOpening:
    def __init__(self, c: int, w: int, h: int = 2100) -> None:
        self.height_opening = h
        self.width_opening = w
        self.coord = c
        self.area_door = 0
        self.len_platband = 0