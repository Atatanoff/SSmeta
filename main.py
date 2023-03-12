from services.room import Room

question = ("Название комнаты",
            "Кол-во углов",
            "Введите сторону")

def main():
    name_room = input(question[0])
    quantity_angle = int(input(question[1]))
    for i in range(quantity_angle):
        pass
        
if __name__ == '__main__':
    main()
