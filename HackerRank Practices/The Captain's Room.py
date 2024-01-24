from collections import Counter

k,room_numbers = int(input()),input()
lst = room_numbers.split(' ')
counter = Counter(lst)

for key in counter:
    if counter[key] == 1:
        print(key)
