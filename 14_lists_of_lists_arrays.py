#TWO DIMENSIONAL ARRAYS
EMPTY = "-"
ROOK = "ROOK"
KNIGHT = "KNIGHT"
PAWN = "PAWN"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK
board[4][2] = KNIGHT
board[3][4] = PAWN
print(board)

#MULTIDIMENSIONAL ARRAYS

##example temperature, 24hours 31 days
temps = [[0.0 for h in range(24)] for d in range(31)] #h is for hour, d for day
print(temps)
#monthly average
total = 0.0
for day in temps:
    total += day[11]
average = total / 31
print("Average temperature at noon:", average)
#max temperature of month
highest = -100.0
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
print("The highest temperature was:", highest)
#
hot_days = 0

for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "days were hot.")

#THREE DIMENSIONAL ARRAY
#hotel:consisting of three buildings, 15 floors each. There are 20 rooms on each floor. For this, you need an array which can collect and process information on the occupied/free rooms.
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
rooms[1][9][13] = True
rooms[0][4][1] = False
vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
