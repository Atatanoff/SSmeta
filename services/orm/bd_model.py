from peewee import Model, CharField, DateField, SqliteDatabase, IntegerField,\
      ForeignKeyField, TextField, BigBitField, BooleanField, BigIntegerField
from dataclasses import dataclass


@dataclass
class DataBass:
    db: SqliteDatabase = SqliteDatabase('data/bd.db')


class BaseModel(Model):
    class Meta:
        database = DataBass.db


class User(BaseModel):
    class Meta:
        db_table = 'Users'

    id = BigIntegerField()
    pay = BooleanField(default=False)


class Estimate(BaseModel):
    class Meta:
        db_table = 'Estimates'

    name = CharField()
    date_create = DateField()
    user_id = ForeignKeyField(User)


class Room(BaseModel):
    class Meta:
        db_table = 'Rooms'

    count_corners = IntegerField()
    name_side = TextField()
    len_side = TextField()
    name_diagonals = TextField()
    len_diagonals = TextField()
    plan = BigBitField()
    height = IntegerField()
    perimeter = IntegerField()
    area = IntegerField()
    area_wall = IntegerField()


class WinOpening(BaseModel):

    room = ForeignKeyField(Room)
    height_opening = IntegerField()
    width_opening = IntegerField()
    coord = CharField()
    len_slopes = IntegerField()        #откосы
    len_windowsill = IntegerField()     #подоконник
    area_win = IntegerField()


class DoorOpening(BaseModel):
    
    room = ForeignKeyField(Room)
    height_opening = IntegerField()
    width_opening = IntegerField()
    coord = CharField()
    area_door = IntegerField() 
    len_platband = IntegerField()
    side_doborniki = IntegerField()


class BalconyDoor(BaseModel):

    room = ForeignKeyField(Room)
    count_corners = IntegerField()
    name_side = TextField()
    len_side = TextField()
    name_diagonals = TextField()
    len_diagonals = TextField()
    plan = BigBitField()
    area_door = IntegerField() 
    len_slopes = IntegerField()
    len_windowsill = IntegerField()
    side_doborniki = IntegerField()    


class Price(BaseModel):
    
    name = CharField()
    price = IntegerField()


class Estimate_works(BaseModel):

    room = ForeignKeyField(Room)
    name = ForeignKeyField(Price)
    cost = IntegerField()
    quantity = IntegerField()


def create_bd():
    db = DataBass.db
    db.connect()
    db.create_tables([Estimate, Room, User, WinOpening, DoorOpening, BalconyDoor, \
                      Price, Estimate_works])
    db.close()



def load_vd():
    pass

if __name__ == '__main__':
    create_bd()
