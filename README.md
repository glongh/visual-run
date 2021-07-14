# visual-run

VisualRun: A Framework for creating visualizations from code execution

## Quick start

If you use any virtual env, activate it .

```bash
# Create virtual env (optional)
python -m venv env
# Activate virtual env (optional)
source env/bin/activate
```

and install the dependencies

```bash
(env) python -m pip install -r requirements.txt
```

## Algorithms

Algorithms are located on the algorithms folder.

#### Run Merge sort

```bash
# To generate the file with the traces of the algorithm, run the following command
(env) python merge_sort.py
```

## Server

The server provides endpoints to be used in the front end interface

```bash
# Start server:
(env) python server.py
```

#### Access the endpoints

##### Request the breakpoints for the visualization of an algorithm:

```bash
(env) curl  "http://127.0.0.1:8080/algorithm?id=merge_sort"
```

###### Response example:

```json
[{"id":"128a2aba-c1e9-4ffe-9f6c-8e2602a3e8ca","event":"init","parameters":[7,4,1,2,9,0,6,3,8,5],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Initialize array with 10 numbers with values from 0 to 100"],"label":""},{"id":"Tracer","event":"step","parameters":[20],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Original Array: [7, 4, 1, 2, 9, 0, 6, 3, 8, 5]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Sort array of 10 elements using merge sort"],"label":""},{"id":"128a2aba-c1e9-4ffe-9f6c-8e2602a3e8ca","event":"select","parameters":[[7,4,1,2,9,0,6,3,8,5]],"label":"red"},{"id":"Tracer","event":"step","parameters":[108],"label":""},{"id":"128a2aba-c1e9-4ffe-9f6c-8e2602a3e8ca","event":"unselect","parameters":[[7,4,1,2,9,0,6,3,8,5]],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Split Left side: [7, 4, 1, 2, 9]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Split Left side: [7, 4]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Split Left side: [7]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Split Right side: [4]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Merge: Left[7] and Right[4]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Sorting: select 4 from Right[4] -> [4]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Merged: [4]"],"label":""},{"id":"128a2aba-c1e9-4ffe-9f6c-8e2602a3e8ca","event":"select","parameters":[[4]],"label":"blue"},{"id":"Tracer","event":"step","parameters":[60],"label":""},{"id":"128a2aba-c1e9-4ffe-9f6c-8e2602a3e8ca","event":"unselect","parameters":[[4]],"label":""},{"id":"Tracer","event":"step","parameters":[60],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Split Right side: [1, 2, 9]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Split Left side: [1]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Split Right side: [2, 9]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Split Left side: [2]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Split Right side: [9]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Merge: Left[2] and Right[9]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Sorting: select 2 from Left[2] -> [2]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Merged: [2]"],"label":""},{"id":"128a2aba-c1e9-4ffe-9f6c-8e2602a3e8ca","event":"select","parameters":[[2]],"label":"blue"},{"id":"Tracer","event":"step","parameters":[60],"label":""},{"id":"128a2aba-c1e9-4ffe-9f6c-8e2602a3e8ca","event":"unselect","parameters":[[2]],"label":""},{"id":"Tracer","event":"step","parameters":[60],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Merge: Left[1] and Right[2, 9]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Sorting: select 1 from Left[1] -> [1]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Merged: [1]"],"label":""},{"id":"128a2aba-c1e9-4ffe-9f6c-8e2602a3e8ca","event":"select","parameters":[[1]],"label":"blue"},{"id":"Tracer","event":"step","parameters":[60],"label":""},{"id":"128a2aba-c1e9-4ffe-9f6c-8e2602a3e8ca","event":"unselect","parameters":[[1]],"label":""},{"id":"Tracer","event":"step","parameters":[60],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Merge: Left[4, 7] and Right[1, 2, 9]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Sorting: select 1 from Right[1, 2, 9] -> [1]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Sorting: select 2 from Right[1, 2, 9] -> [1, 2]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Sorting: select 4 from Left[4, 7] -> [1, 2, 4]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Sorting: select 7 from Left[4, 7] -> [1, 2, 4, 7]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Merged: [1, 2, 4, 7]"],"label":""},{"id":"128a2aba-c1e9-4ffe-9f6c-8e2602a3e8ca","event":"select","parameters":[[1,2,4,7]],"label":"blue"},{"id":"Tracer","event":"step","parameters":[60],"label":""},{"id":"128a2aba-c1e9-4ffe-9f6c-8e2602a3e8ca","event":"unselect","parameters":[[1,2,4,7]],"label":""},{"id":"Tracer","event":"step","parameters":[60],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Split Right side: [0, 6, 3, 8, 5]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Split Left side: [0, 6]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Split Left side: [0]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Split Right side: [6]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Merge: Left[0] and Right[6]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Sorting: select 0 from Left[0] -> [0]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Merged: [0]"],"label":""},{"id":"128a2aba-c1e9-4ffe-9f6c-8e2602a3e8ca","event":"select","parameters":[[0]],"label":"blue"},{"id":"Tracer","event":"step","parameters":[60],"label":""},{"id":"128a2aba-c1e9-4ffe-9f6c-8e2602a3e8ca","event":"unselect","parameters":[[0]],"label":""},{"id":"Tracer","event":"step","parameters":[60],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Split Right side: [3, 8, 5]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Split Left side: [3]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Split Right side: [8, 5]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Split Left side: [8]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Split Right side: [5]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Merge: Left[8] and Right[5]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Sorting: select 5 from Right[5] -> [5]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Merged: [5]"],"label":""},{"id":"128a2aba-c1e9-4ffe-9f6c-8e2602a3e8ca","event":"select","parameters":[[5]],"label":"blue"},{"id":"Tracer","event":"step","parameters":[60],"label":""},{"id":"128a2aba-c1e9-4ffe-9f6c-8e2602a3e8ca","event":"unselect","parameters":[[5]],"label":""},{"id":"Tracer","event":"step","parameters":[60],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Merge: Left[3] and Right[5, 8]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Sorting: select 3 from Left[3] -> [3]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Merged: [3]"],"label":""},{"id":"128a2aba-c1e9-4ffe-9f6c-8e2602a3e8ca","event":"select","parameters":[[3]],"label":"blue"},{"id":"Tracer","event":"step","parameters":[60],"label":""},{"id":"128a2aba-c1e9-4ffe-9f6c-8e2602a3e8ca","event":"unselect","parameters":[[3]],"label":""},{"id":"Tracer","event":"step","parameters":[60],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Merge: Left[0, 6] and Right[3, 5, 8]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Sorting: select 0 from Left[0, 6] -> [0]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Sorting: select 3 from Right[3, 5, 8] -> [0, 3]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Sorting: select 5 from Right[3, 5, 8] -> [0, 3, 5]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Sorting: select 6 from Left[0, 6] -> [0, 3, 5, 6]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Merged: [0, 3, 5, 6]"],"label":""},{"id":"128a2aba-c1e9-4ffe-9f6c-8e2602a3e8ca","event":"select","parameters":[[0,3,5,6]],"label":"blue"},{"id":"Tracer","event":"step","parameters":[60],"label":""},{"id":"128a2aba-c1e9-4ffe-9f6c-8e2602a3e8ca","event":"unselect","parameters":[[0,3,5,6]],"label":""},{"id":"Tracer","event":"step","parameters":[60],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Merge: Left[1, 2, 4, 7, 9] and Right[0, 3, 5, 6, 8]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Sorting: select 0 from Right[0, 3, 5, 6, 8] -> [0]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Sorting: select 1 from Left[1, 2, 4, 7, 9] -> [0, 1]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Sorting: select 2 from Left[1, 2, 4, 7, 9] -> [0, 1, 2]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Sorting: select 3 from Right[0, 3, 5, 6, 8] -> [0, 1, 2, 3]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Sorting: select 4 from Left[1, 2, 4, 7, 9] -> [0, 1, 2, 3, 4]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Sorting: select 5 from Right[0, 3, 5, 6, 8] -> [0, 1, 2, 3, 4, 5]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Sorting: select 6 from Right[0, 3, 5, 6, 8] -> [0, 1, 2, 3, 4, 5, 6]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Sorting: select 7 from Left[1, 2, 4, 7, 9] -> [0, 1, 2, 3, 4, 5, 6, 7]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Sorting: select 8 from Right[0, 3, 5, 6, 8] -> [0, 1, 2, 3, 4, 5, 6, 7, 8]"],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Merged: [0, 1, 2, 3, 4, 5, 6, 7, 8]"],"label":""},{"id":"128a2aba-c1e9-4ffe-9f6c-8e2602a3e8ca","event":"select","parameters":[[0,1,2,3,4,5,6,7,8]],"label":"blue"},{"id":"Tracer","event":"step","parameters":[60],"label":""},{"id":"128a2aba-c1e9-4ffe-9f6c-8e2602a3e8ca","event":"unselect","parameters":[[0,1,2,3,4,5,6,7,8]],"label":""},{"id":"Tracer","event":"step","parameters":[60],"label":""},{"id":"028115dd-3302-446e-895b-9b78cb139b01","event":"print","parameters":["Sorted Array: [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]"],"label":""},{"id":"128a2aba-c1e9-4ffe-9f6c-8e2602a3e8ca","event":"select_range","parameters":[0,10],"label":"green"},{"id":"Tracer","event":"step","parameters":[108],"label":""}]
```

##### Request the source file for the visualization of an algorithm:

```bash
(env) curl  "http://127.0.0.1:8080/file?id=merge_sort"
```

###### Response example:

```json
{
  "file": "# Import tracer {\nfrom runner import Runner\nfrom tracers import Array\nfrom tracers import Logger\nfrom tracers import Tracer\nfrom random import randint\nfrom math import ceil\n\n# }\n\n# Setup the runner with the tracer {\nOUTPUT_TO_FILE = 1\n\nrunner = Runner()\narray_tracer = Array()\nlogger_tracer = Logger()\nrunner.register([array_tracer, logger_tracer])\nmax_elements = 6\n# }\n\narr_of_numbers = [randint(0, 100) for n in range(max_elements)]\n\n# Initialize array of numbers {\narray_tracer.init(arr_of_numbers)\nlogger_tracer.print(\"Initialize array with {0} numbers with values from 0 to 100\".format(max_elements))\nTracer.step(19)\nlogger_tracer.print(\"Original Array: {}\".format(list(map(int, arr_of_numbers))))\narray_tracer.select_range(0, max_elements - 1, \"red\")\nTracer.step(19)\narray_tracer.unselect_range(0, max_elements - 1)\n\n\n# }\n\n\ndef merge_sort(start, end):\n    # O1: Base case\n    if abs(end - start) <= 1:\n        return []\n\n    # O2: A mid point is defined\n    middle = ceil((start + end) / 2)\n\n    # O3: Left side is sorted\n    merge_sort(start, middle)\n\n    # O4: Right side is sorted\n    merge_sort(middle, end)\n\n    # Merge list {\n    logger_tracer.print(\"Divide: Left[{},{}] and Right[{},{}]\".format(start, middle - 1, middle, end - 1))\n    # }\n\n    # O0: Both part are sorted\n    return merge(start, middle, end)\n\n\ndef merge(start, middle, end):\n    # global arr_of_numbers\n    left_size = middle - start\n    right_size = end - middle\n    max_size = max(left_size, right_size)\n    size = end - start\n    left = []\n    right = []\n\n    index = 0\n    while index < max_size:\n        if index < left_size:\n            left.append(arr_of_numbers[start + index])\n            # Insert in to left {\n            array_tracer.select(start + index, \"blue\")\n            logger_tracer.print(\"Insert value {} into Left [{}]\".format(arr_of_numbers[start + index], index))\n            Tracer.step(70)\n            # }\n\n        if index < right_size:\n            right.append(arr_of_numbers[middle + index])\n            # Insert in to right {\n            array_tracer.select(middle + index, \"blue\")\n            logger_tracer.print(\"Insert value {} into Right [{}]\".format(arr_of_numbers[middle + index], index))\n            Tracer.step(78)\n            # }\n\n        index += 1\n\n    # Merge list {\n    logger_tracer.print(\"Left:{} and Right:{}\".format(list(map(int, left)), list(map(int, right))))\n    # }\n\n    index = 0\n    while index < size:\n        # keep track of line executed\n        line = 90\n        if len(left) > 0 and len(right) > 0:\n            if left[0] > right[0]:\n                arr_of_numbers[start + index] = right.pop(0)\n                # {\n                line = 95\n                logger_tracer.print(\"Replace Right[{}] with {}\".format(index, arr_of_numbers[start + index]))\n                # }\n            else:\n                arr_of_numbers[start + index] = left.pop(0)\n                # {\n                line = 101\n                logger_tracer.print(\"Replace Left[{}] with {}\".format(index, arr_of_numbers[start + index]))\n                # }\n        elif len(left) > 0:\n            arr_of_numbers[start + index] = left.pop(0)\n            # {\n            line = 107\n            logger_tracer.print(\"Replace Left[{}] with {}\".format(index, arr_of_numbers[start + index]))\n            # }\n        else:\n            arr_of_numbers[start + index] = right.pop(0)\n            # {\n            line = 113\n            logger_tracer.print(\"Replace Right[{}] with {}\".format(index, arr_of_numbers[start + index]))\n            # }\n\n        array_tracer.unselect(start + index)\n        array_tracer.notice(start + index, arr_of_numbers[start + index], \"red\")\n        Tracer.step(line)\n        array_tracer.unnoticed(start + index)\n        index += 1\n\n    # Merged Array {\n    partially_merged_array = []\n    index2 = start\n    while index2 < end:\n        partially_merged_array.append(arr_of_numbers[index2])\n        index2 += 1\n    logger_tracer.print(\"Merged Array: {}\".format(list(map(int, partially_merged_array))))\n    # }\n\n\nmerge_sort(0, len(arr_of_numbers))\n\n# { Sort array of 100 elements using merge sort\nlogger_tracer.print(\"Sorted Array: {}\".format(list(map(int, arr_of_numbers))))\narray_tracer.select_range(0, max_elements - 1, \"green\")\nTracer.step(135)\n# }\n\n\nif OUTPUT_TO_FILE:\n    jsonFile = open(\"output/merge_sort.json\", \"w\")\n    jsonFile.write(runner.export_events())\n    jsonFile.close()\nelse:\n    print(runner.export_events())\n"
}
```

##### Request the tracing of an algorithm file:

```bash
(env) curl  "http://127.0.0.1:8080/trace?id=merge_sort"
```

###### Response example:

A new output file will be placed on the output folder.

```bash
200 OK
```

##### Request the tracing of all algorithms files:

```bash
(env) curl  "http://127.0.0.1:8080/trace_all"
```

###### Response example:

```json
{
   "results": [
      {"merge_sort": "ok"}, 
      {"quick_sort_class": "ok"}, 
      {"merge_sort_class": "ok"}, 
      {"example": "ok"}
  ]
}
```
