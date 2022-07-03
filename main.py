number_of_floors = range(1, 11)
rooms_per_floor = range(1, 51)
even_numbered_rooms = 0

for floor in number_of_floors:
    for room in rooms_per_floor:
        if room % 2 == 0:
            even_numbered_rooms += 0
