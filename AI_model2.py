import random

# Model 2 -> Filter Out Already Tried Numbers

def random_number_func():
        random_number = random.randint(0, 100)
        return random_number

tried_numebrs = []
times_tried = 1
while True:
    my_number = 46
    random_number = random_number_func()
    # random_number = random.randint(0, 100)
    if len(tried_numebrs) == 0:
        tried_numebrs.append(random_number)
    else:
        for x in tried_numebrs:
            if x == random_number:
                random_number = random_number_func()
                tried_numebrs.append(random_number)
    if int(random_number) == my_number:
        print("Got Number")
        break
    times_tried = times_tried + 1

print(f'It Took {times_tried} Times to Find the Number')
print(f'Array => {tried_numebrs}')

# It Took 0 ~ 150 Tries To Find the Number