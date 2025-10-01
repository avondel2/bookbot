def get_num_words(msg):
    return len(msg.split())

def get_num_characters(msg):
    temp = {}
    for i in msg.lower():
        if i in temp:
            temp[i] += 1
        else:
            temp[i] = 1
    return temp