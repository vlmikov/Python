from collections import deque
n = int(input())
result = deque()

for i in range(n):
    command = [int(x) for x in input().split()]
    petrol, distance = command
    result.append([i, petrol, distance])
start_index= 0
gorivo = 0


while result:
    current_station_start = result.popleft()
    gorivo += current_station_start[1]
    distance = current_station_start[2]
    if gorivo < distance:
        print(f"{current_station_start[0]} is no start station")
        result.append(current_station_start)
    else:
        gorivo -= distance

        
        for i in range(len(result)):
            if gorivo < distance:
                print(f"{current_station_start[0]} is no start station")
                result.append(current_station_start)
