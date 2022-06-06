# 1 Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(a):
    for x in range(len(a)):
        if x > 0:
            a[x] = "big"
    return print(a)


biggie_size([-1, 3, 5, -5])

# 2 Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it


def count_positives(a):
    counter = 0
    for x in range(len(a)):
        # print(x)
        if a[x] > 0:
            # print(x)
            counter = counter+1
            a[-1] = counter
        # print( a[-1])
    return print(a)


count_positives([-1, 1, 1, 1])
count_positives([1, 6, -4, -2, -7, -2])
# 3 Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

# for number in a:


def sum_total(a):
    _sum = 0
    for x in range(0, len(a)):
        _sum = _sum+a[x]

    return _sum


sum_total([1, 2, 3, 4])
sum_total([6, 3, -2])
# 4 Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5


def average(a):
    _sum = 0
    _avg = 0
    for x in range(0, len(a)):
        _sum = _sum+a[x]
    avg = _sum/len(a)

    return avg


average([1, 2, 3, 4])
# 5 Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0


def length(a):
    return print(len(a))


length([37, 2, 1, -9])
length([])
# 6 Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False


def minimum(a):
    if len(a) == 0:
        return False
    else:
        return min(a)


minimum([37, 2, 1, -9])
minimum([])
# 7 Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False


def maximum(a):
    if len(a) == 0:
        return False
    else:
        return max(a)


maximum([37, 2, 1, -9])
maximum([])

# 8 Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }


def ultimate_analysis(a):
    print("dic")
    _max = maximum(a)
    _min = minimum(a)
    _sum = sum_total(a)
    _avg = average(a)
    _len = (len(a))
    _dictionary = {'sumTotal': _sum, 'average': _avg,
                   'minimum': _min, 'maximum': _max, 'length': _len}
    print(_dictionary)


print(ultimate_analysis([37, 2, 1, -9]))


# 9 Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(a):
    return a[::-1]


reverse_list([37, 2, 1, -9])
