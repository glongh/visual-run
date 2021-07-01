# Import tracer {
from runner import Runner
from tracers import Array
from tracers import Logger
from tracers import Tracer
from random import shuffle
OUTPUT_TO_FILE = 1
# }

# Setup the runner with the tracer {
runner = Runner()
array_tracer = Array()
array_sorted_tracer = Array()
logger_tracer = Logger()
runner.register([array_tracer, logger_tracer])
max_elements = 10
# }

# arr_of_numbers = [randint(0, 100) for n in range(max_elements)]
arr_of_numbers = [n for n in range(max_elements)]

shuffle(arr_of_numbers)

# Initialize array with 100 numbers from 0 to 100 {
array_tracer.init(arr_of_numbers)
logger_tracer.print("Initialize array with {} numbers with values from 0 to 100".format(max_elements))
Tracer.step(20)
logger_tracer.print("Original Array: {}".format(list(map(int, arr_of_numbers))))


# }

def merge_sort(array: list) -> list:
    length = len(array)

    # O1: Base case
    if length == 1:
        return array

    # O2: A mid point is defined
    middle = length // 2

    # O3: Left side is sorted
    # Split Left side {
    logger_tracer.print("Split Left side: {}".format(list(map(int, array[:middle]))))
    # }
    left = merge_sort(array[:middle])

    # O4: Right side is sorted
    # Split Right side {
    logger_tracer.print("Split Right side: {}".format(list(map(int, array[middle:]))))
    # }
    right = merge_sort(array[middle:])

    # Merge list {
    logger_tracer.print("Merge: Left{} and Right{}".format(list(map(int, left)), list(map(int, right))))
    # }

    # O0: Both part are sorted
    merged_list = merge(left, right)
    return merged_list


def merge(left_array: list, right_array: list) -> list:
    index_left = 0
    index_right = 0
    sorted_array = []

    while index_left < len(left_array) and index_right < len(right_array):
        if left_array[index_left] < right_array[index_right]:
            sorted_array.append(left_array[index_left])
            # Append to list  {
            logger_tracer.print(
                "Sorting: select {} from Left{} -> {}".format(left_array[index_left], list(map(int, left_array)),
                                                              list(map(int, sorted_array))))
            # }
            index_left += 1
        else:
            sorted_array.append(right_array[index_right])
            # Append to list  {
            logger_tracer.print(
                "Sorting: select {} from Right{} -> {}".format(right_array[index_right], list(map(int, right_array)),
                                                               list(map(int, sorted_array))))
            # }
            index_right += 1

    # Split list {
    logger_tracer.print("Merged: {}".format(list(map(int, sorted_array))))
    array_tracer.select(list(map(int, sorted_array)), "blue")
    Tracer.step(60)
    array_tracer.unselect(list(map(int, sorted_array)))
    Tracer.step(60)
    # }
    sorted_array.extend(left_array[index_left:])
    sorted_array.extend(right_array[index_right:])
    return sorted_array


# { Sort array of 100 elements using merge sort
logger_tracer.print("Sort array of {} elements using merge sort".format(max_elements))
# array_tracer.select_range(0, max_elements, "red")
array_tracer.select(list(map(int, arr_of_numbers)), "red")
Tracer.step(108)
# array_tracer.unselect_range(0, max_elements)
array_tracer.unselect(list(map(int, arr_of_numbers)))
# }

sorted_array = merge_sort(arr_of_numbers)

# { Sort array of 100 elements using merge sort
logger_tracer.print("Sorted Array: [{}]".format(list(map(int, sorted_array))))
array_tracer.select_range(0, max_elements, "green")
Tracer.step(108)
# }

if OUTPUT_TO_FILE:
    jsonFile = open("output/merge_sort.json", "w")
    jsonFile.write(runner.export_events())
    jsonFile.close()
else:
    print(runner.export_events())
