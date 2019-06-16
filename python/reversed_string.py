#T(n) S(1)

def swap(a, b, string):
    print(a, b)
    print(string)
    string[a], string[b] = string[b], string[a]

def reversed_string(string):
    length = len(string)
    string = list(string)
    prior = 0
    rear = 0
    tags = 0

    while rear < length-1:
        rear_element = string[rear]
        rear += 1
        tags += 1
        if rear_element == ' ':
            space_location = rear
            tags = tags // 2 + 1
            rear -= 1
            while prior != tags:
                swap(prior, rear, string)
                prior += 1
                rear -= 1
            rear = space_location + 1
            prior = space_location + 1
            
        else:
            continue

    return ''.join(string)


string = "I am allen or call me feng"
