# Import tracer {
from runner import Runner
from tracers import Array
from tracers import Logger
from tracers import Tracer
from random import randint
from math import ceil

# }

# Setup the runner with the tracer {
OUTPUT_TO_FILE = 0

runner = Runner()
array_tracer = Array()
logger_tracer = Logger()
runner.register([array_tracer, logger_tracer])
max_elements = 6
# }

arr_of_numbers = [randint(0, 100) for n in range(max_elements)]

# Initialize array of numbers {
array_tracer.init(arr_of_numbers)
logger_tracer.print("Initialize array with {0} numbers with values from 0 to 100".format(max_elements))
Tracer.step(19)
logger_tracer.print("Original Array: {}".format(list(map(int, arr_of_numbers))))
array_tracer.select_range(0, max_elements - 1, "red")
Tracer.step(19)
array_tracer.unselect_range(0, max_elements - 1)


# }


class MergeSort():
    def __init__(self, array):
        self.arr_of_numbers = array

    def sort(self):
        self.merge_sort(0, len(self.arr_of_numbers))
        return arr_of_numbers

    def merge_sort(self, start, end):
        # O1: Base case
        if abs(end - start) <= 1:
            return []

        # O2: A mid point is defined
        middle = ceil((start + end) / 2)

        # O3: Left side is sorted
        self.merge_sort(start, middle)

        # O4: Right side is sorted
        self.merge_sort(middle, end)

        # Merge list {
        logger_tracer.print("Divide: Left[{},{}] and Right[{},{}]".format(start, middle - 1, middle, end - 1))
        # }

        # O0: Both part are sorted
        return self.merge(start, middle, end)

    def merge(self, start, middle, end):
        left_size = middle - start
        right_size = end - middle
        max_size = max(left_size, right_size)
        size = end - start
        left = []
        right = []

        index = 0
        while index < max_size:
            if index < left_size:
                left.append(self.arr_of_numbers[start + index])
                # Insert in to left {
                array_tracer.select(start + index, "blue")
                logger_tracer.print("Insert value {} into Left [{}]".format(self.arr_of_numbers[start + index], index))
                Tracer.step(70)
                # }

            if index < right_size:
                right.append(arr_of_numbers[middle + index])
                # Insert in to right {
                array_tracer.select(middle + index, "blue")
                logger_tracer.print(
                    "Insert value {} into Right [{}]".format(self.arr_of_numbers[middle + index], index))
                Tracer.step(78)
                # }

            index += 1

        # Merge list {
        logger_tracer.print("Left:{} and Right:{}".format(list(map(int, left)), list(map(int, right))))
        # }

        index = 0
        while index < size:
            # keep track of line executed
            line = 90
            if len(left) > 0 and len(right) > 0:
                if left[0] > right[0]:
                    self.arr_of_numbers[start + index] = right.pop(0)
                    # {
                    line = 106
                    logger_tracer.print("Replace Right[{}] with {}".format(index, self.arr_of_numbers[start + index]))
                    # }
                else:
                    self.arr_of_numbers[start + index] = left.pop(0)
                    # {
                    line = 120
                    logger_tracer.print("Replace Left[{}] with {}".format(index, self.arr_of_numbers[start + index]))
                    # }
            elif len(left) > 0:
                self.arr_of_numbers[start + index] = left.pop(0)
                # {
                line = 118
                logger_tracer.print("Replace Left[{}] with {}".format(index, self.arr_of_numbers[start + index]))
                # }
            else:
                arr_of_numbers[start + index] = right.pop(0)
                # {
                line = 124
                logger_tracer.print("Replace Right[{}] with {}".format(index, self.arr_of_numbers[start + index]))
                # }

            array_tracer.unselect(start + index)
            array_tracer.notice(start + index, self.arr_of_numbers[start + index], "red")
            Tracer.step(line)
            array_tracer.unnoticed(start + index)
            index += 1

        # Merged Array {
        partially_merged_array = []
        index2 = start
        while index2 < end:
            partially_merged_array.append(self.arr_of_numbers[index2])
            index2 += 1
        logger_tracer.print("Merged Array: {}".format(list(map(int, partially_merged_array))))
        # }


# Sort array of numbers
merge = MergeSort(arr_of_numbers)
sorted_list = merge.sort()

# { Sort array of 100 elements using merge sort
logger_tracer.print("Sorted Array: {}".format(list(map(int, sorted_list))))
array_tracer.select_range(0, max_elements - 1, "green")
Tracer.step(146)
# }


if OUTPUT_TO_FILE:
    jsonFile = open("output/merge_sort.json", "w")
    jsonFile.write(runner.export_events())
    jsonFile.close()
else:
    print(runner.export_events())
