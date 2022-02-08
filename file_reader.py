import json

from matplotlib.font_manager import json_dump

filename1 = 'pi_digits.txt'
with open(filename1, 'r') as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

numbers = [2,3,4,1,3,5,5,4,7,9]
game = "Shanghai Temple"
filename2 = 'numbers.json'
with open(filename2, 'w') as f_obj:
    json.dump(numbers, f_obj)
    json.dump(game, f_obj)
