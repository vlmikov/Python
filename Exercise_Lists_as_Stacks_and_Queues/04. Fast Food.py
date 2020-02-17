from collections import deque
sums = 0
queue = deque()
quantity = int(input())

order = [int(x) for x in input().split()]
[queue.append(order[x]) for x in range(len(order))]

print(max(queue))

for i in range(len(queue)):


    p = queue.popleft()
    if p<= quantity:
        quantity -= p

    else:
        sums = sum(queue)+ p
        print(f"Orders left: {p} ", end="")
        for _ in range(len(queue)):
            print(f"{queue.popleft()}", end=" ")
        break

if sums==0:
    print("Orders complete")

