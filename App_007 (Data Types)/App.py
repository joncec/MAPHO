# Text Type = str (String).
# Numeric Types: int (Integer), float, complex.
# Sequence Types: list, tuple, range.
# Mapping Type: dict.
# Set Types: set, frozenset.
# Boolean Type: bool.
# Binary Types: bytes, bytearray, memoryview.

# Use "type()" to fet the variable's type.

floating_point_number = 4.6
print(type(floating_point_number))
# float

my_list = [1, 2, 3, 4, 5]
print(my_list)
print(type(my_list))
# list

triple = ( 'A', 'B', 'C')
print(triple)
type(triple)
# tuple

to_ten = range(10)
print(to_ten)
type(to_ten)
# range

# simple loop for example:
for i in to_ten:
    print(i)

dictionary = {
    "name" : "Jonas",
    "language" : "Python"
}
print(dictionary)
type(dictionary)
# dict

set_of_numbers = set([1, 2, 2,3, 1, 3, 4, 4])
print(set_of_numbers)
print(type(set_of_numbers))
# set doesn't allow repetition, evert entry must be unique.

correct = True
wrong = False
print(type(correct))