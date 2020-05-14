from collections import deque

def hot_potato(people, num):

    queue = deque()

    for person in people:
        queue.appendleft(person)

    while len(queue) > 1:
        for _ in range(num - 1):
            queue.appendleft(queue.pop())

        queue.pop()

    return queue.pop()


print(hot_potato(["Roy", "Jenn", "Ben", "Bill", "Josephus", "Kelly", "Lora"], 3))