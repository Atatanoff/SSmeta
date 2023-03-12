
class Rooms():

    def __init__(self):
        self.state = 0
        self.name = ''
        self.rooms = []
        self.type_state = {
            1: 'Введите название комнаты'
                  }
        self.room_name = ''
    
    def add_room(self, room):
        self.rooms.append(room)

    def __str__(self) -> str:
        return self.type_state[self.state]

rooms = Rooms()

if __name__ == '__main__':
    rooms.state = 1
    print(rooms)