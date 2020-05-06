def reconstruct_queue(people):
        
    queue = [[None, None]] * len(people)
    
    people.sort(reverse=True)
    
    while people:
        current = people.pop()
        h, k = current
        pos = 0
        i = 0
        while pos != k or queue[i][0] is not None:
            if queue[i][0] is None or queue[i][0] == h:
                pos += 1
            i += 1
        queue[i] = current
        
    return queue


def reconstruct_queue_better(people):

    queue = []

    people = sorted(people, key = lambda x: (-x[0], x[1]))

    for p in people:
        queue.insert(p[1], p)

    return queue
    