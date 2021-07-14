from runner import Runner
from tracers import Array
from tracers import Logger
from tracers import Tracer

OUTPUT_TO_FILE = 1

runner = Runner()
array_tracer = Array()
logger_tracer = Logger()

arr_of_numbers = [n for n in range(100)]

runner.register([array_tracer, logger_tracer])

array_tracer.init(arr_of_numbers)
num_to_search = 10

logger_tracer.print(
    "Searching for number 10 in an array of 100 elements", "red")
array_tracer.select_range(0, 99, 'blue')
Tracer.step(15)
array_tracer.unselect_range(0, 99)

for key, number in enumerate(arr_of_numbers):
    array_tracer.select(key, "yellow")
    logger_tracer.print("Searching for {} in the array index {}".format(
        num_to_search, key), "black")
    Tracer.step(19)

    if num_to_search == number:
        logger_tracer.print(
            "Name {} found in the array at position {}".format(num_to_search, key))
        Tracer.step(22)
        break

    logger_tracer.print(
        "Number {} not found at position {}. Let's keep searching".format(num_to_search, key))
    Tracer.step(22)

if OUTPUT_TO_FILE:
    jsonFile = open("output/example.json", "w")
    jsonFile.write(runner.export_events())
    jsonFile.close()
else:
    print(runner.export_events())
    print(runner.print_stats())
