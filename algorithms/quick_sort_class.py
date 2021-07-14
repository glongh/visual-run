# Import tracer {
from runner import Runner
from tracers import Array
from tracers import Logger
from tracers import Tracer
from random import randint


# }

# Setup the runner with the tracer {
OUTPUT_TO_FILE = 1

runner = Runner()
array_tracer = Array()
logger_tracer = Logger()
runner.register([array_tracer, logger_tracer])
max_elements = 10
# }

arr_of_numbers = [randint(0, 100) for n in range(max_elements)]

# Initialize array of numbers {
array_tracer.init(arr_of_numbers)
logger_tracer.print(
    "Initialize array with {0} numbers with values from 0 to 100".format(max_elements))
Tracer.step(21)
logger_tracer.print("Original Array: {}".format(
    list(map(int, arr_of_numbers))))
array_tracer.select_range(0, max_elements - 1, "red")
Tracer.step(21)
array_tracer.unselect_range(0, max_elements - 1)

# }


class QuickSort():
    def __init__(self, array):
        self.arr_of_numbers = array

    def sort(self):
        self.quick_sort(self.arr_of_numbers, 0, len(self.arr_of_numbers) - 1)
        return self.arr_of_numbers

    def quick_sort(self, array, start, end):
        # O0: Inmediately solvable?
        if len(array) == 1:
            return array

        if start < end:
            # {
            array_tracer.select(start)
            Tracer.step(57)
            array_tracer.select(end)
            Tracer.step(57)
            array_tracer.unselect(start)
            array_tracer.unselect(end)
            # }

            # O1 (Partitioned): array[start] <= array[k] < array[end] for all start <= k <= end
            k = self.partition(array, start, end)

            # {
            logger_tracer.print(
                "Select the partition index: {}".format(k))
            # }

            # O2a (Left part sorted): array[start, k] is sorted
            self.quick_sort(array, start, k - 1)

            # {
            logger_tracer.print(
                "Call quicksort on the Left sublist[{},{}]".format(start, k - 1))
            # }

            # O2b (Right part sorted): array[k+1, end] is sorted
            self.quick_sort(array, k + 1, end)

            # {
            logger_tracer.print(
                "Call quicksort on the Right sublist[{},{}]".format(k + 1, end))
            # }

    def partition(self, array, start, end):
        pivot_index = start
        pivot = array[pivot_index]
        # {
        array_tracer.select(end)
        Tracer.step(86)
        array_tracer.unselect(end)
        logger_tracer.print(
            "Pivot selected {}".format(pivot))
        # }

        while start < end:
            # {
            logger_tracer.print(
                "Move the left bound to the right until it reaches a value greater than or equal to the pivot")
            Tracer.step(101)
            # }
            while start < len(array) and array[start] <= pivot:
                start += 1

            # {
            logger_tracer.print(
                "Move the right bound to the left until it crosses the left bound or finds a value less than the pivot")
            Tracer.step(101)
            # }
            while array[end] > pivot:
                end -= 1

            if(start < end):
                array[start], array[end] = array[end], array[start]
                # {
                logger_tracer.print(
                    "Swap selected values, start and end have not crossed each other [{}] <- [{}] and [{}] <- [{}]".format(start, end, end, start))
                array_tracer.notice(start, array[end], "red")
                array_tracer.notice(end, array[start], "red")
                Tracer.step(113)
                array_tracer.unnoticed(start)
                array_tracer.unnoticed(end)
                # }

        array[end], array[pivot_index] = array[pivot_index], array[end]
        # {
        logger_tracer.print(
            "Swap pivot selected value with end position [{}] <- [{}] and [{}] <- [{}]".format(end, pivot_index, pivot_index, end))
        array_tracer.notice(end, array[pivot_index], "red")
        array_tracer.notice(pivot_index, array[end], "red")
        Tracer.step(126)
        array_tracer.unnoticed(pivot_index)
        array_tracer.unnoticed(end)
        # }

        return end


if __name__ == "__main__":
    # Sort array of numbers
    print(arr_of_numbers)
    quick = QuickSort(arr_of_numbers)
    sorted_list = quick.sort()
    print(sorted_list)
    # { Sort array of 100 elements using quick sort
    logger_tracer.print("Sorted Array: {}".format(list(map(int, sorted_list))))
    array_tracer.select_range(0, max_elements - 1, "green")
    Tracer.step(141)
    # }

    if OUTPUT_TO_FILE:
        jsonFile = open("output/quick_sort.json", "w")
        jsonFile.write(runner.export_events())
        jsonFile.close()
    else:
        print(runner.export_events())
