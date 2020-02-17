from collections import deque

alls = deque()

duration_green = int(input())
duration_free_window = int(input())

start = 0
count_car = 0
crash = False

while True:
    command = input()
    if command == "END":
        break
    else:
        alls.append(command)

for _ in range(len(alls)):
    current_car = alls[0]
    if current_car == "green":
        start = 0
        alls.popleft()
        #print("Svetna zeleno")
        continue
    else:
        current_time = len(current_car)
        if start >= duration_green:

            continue
        else:
            start += current_time
            alls.popleft()
            #print(f"{alls.popleft()} vliza v krustovishteto")
            if start > duration_green + duration_free_window:
                print("A crash happened!")
                crash = duration_green + duration_free_window - start
                print(f"{current_car} was hit at {current_car[crash]}.")
                crash = True

                break
            else:
                #print(f"{current_car} premina")
                count_car += 1


if not crash:
    print("Everyone is safe.")
    print(f"{count_car} total cars passed the crossroads.")






