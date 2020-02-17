from collections import deque

queue = deque()

numbers = [int(x) for x in input().split()]

num_add_element, num_remove_element, search_elemnt = numbers

elements = [int(x) for x in input().split()]

[queue.append(elements[i]) for i in range(num_add_element)]
[queue.popleft() for _ in range(num_remove_element)]
if search_elemnt in queue:
    print(True)

else:
    if queue:
        print(min(elements))
    else:
        print(0)

