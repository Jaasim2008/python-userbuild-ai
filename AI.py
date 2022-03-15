import random

times_tried = 1
while True:
    my_number = 46
    random_number = random.randint(0, 100)
    if int(random_number) == my_number:
        print("Got Number")
        break
    times_tried = times_tried + 1
print(f'It Took {times_tried} Times to Find the Number')

# It Took 0 ~ 250 Tries To Find the Number