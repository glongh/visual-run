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
[
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "init",
    "parameters": [34, 70, 64, 34, 74, 84],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Initialize array with 6 numbers with values from 0 to 100"],
    "label": ""
  },
  { "id": "Tracer", "event": "step", "parameters": [19], "label": "" },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Original Array: [34, 70, 64, 34, 74, 84]"],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "select_range",
    "parameters": [0, 5],
    "label": "red"
  },
  { "id": "Tracer", "event": "step", "parameters": [19], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unselect_range",
    "parameters": [0, 5],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Divide: Left[0,0] and Right[1,1]"],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "select",
    "parameters": [0],
    "label": "blue"
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Insert value 34 into Left [0]"],
    "label": ""
  },
  { "id": "Tracer", "event": "step", "parameters": [70], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "select",
    "parameters": [1],
    "label": "blue"
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Insert value 70 into Right [0]"],
    "label": ""
  },
  { "id": "Tracer", "event": "step", "parameters": [78], "label": "" },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Left:[34] and Right:[70]"],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Replace Left[0] with 34"],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unselect",
    "parameters": [0],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "notice",
    "parameters": [0, 34],
    "label": "red"
  },
  { "id": "Tracer", "event": "step", "parameters": [101], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unnoticed",
    "parameters": [0],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Replace Right[1] with 70"],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unselect",
    "parameters": [1],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "notice",
    "parameters": [1, 70],
    "label": "red"
  },
  { "id": "Tracer", "event": "step", "parameters": [113], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unnoticed",
    "parameters": [1],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Merged Array: [34, 70]"],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Divide: Left[0,1] and Right[2,2]"],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "select",
    "parameters": [0],
    "label": "blue"
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Insert value 34 into Left [0]"],
    "label": ""
  },
  { "id": "Tracer", "event": "step", "parameters": [70], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "select",
    "parameters": [2],
    "label": "blue"
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Insert value 64 into Right [0]"],
    "label": ""
  },
  { "id": "Tracer", "event": "step", "parameters": [78], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "select",
    "parameters": [1],
    "label": "blue"
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Insert value 70 into Left [1]"],
    "label": ""
  },
  { "id": "Tracer", "event": "step", "parameters": [70], "label": "" },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Left:[34, 70] and Right:[64]"],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Replace Left[0] with 34"],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unselect",
    "parameters": [0],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "notice",
    "parameters": [0, 34],
    "label": "red"
  },
  { "id": "Tracer", "event": "step", "parameters": [101], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unnoticed",
    "parameters": [0],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Replace Right[1] with 64"],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unselect",
    "parameters": [1],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "notice",
    "parameters": [1, 64],
    "label": "red"
  },
  { "id": "Tracer", "event": "step", "parameters": [95], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unnoticed",
    "parameters": [1],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Replace Left[2] with 70"],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unselect",
    "parameters": [2],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "notice",
    "parameters": [2, 70],
    "label": "red"
  },
  { "id": "Tracer", "event": "step", "parameters": [107], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unnoticed",
    "parameters": [2],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Merged Array: [34, 64, 70]"],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Divide: Left[3,3] and Right[4,4]"],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "select",
    "parameters": [3],
    "label": "blue"
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Insert value 34 into Left [0]"],
    "label": ""
  },
  { "id": "Tracer", "event": "step", "parameters": [70], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "select",
    "parameters": [4],
    "label": "blue"
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Insert value 74 into Right [0]"],
    "label": ""
  },
  { "id": "Tracer", "event": "step", "parameters": [78], "label": "" },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Left:[34] and Right:[74]"],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Replace Left[0] with 34"],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unselect",
    "parameters": [3],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "notice",
    "parameters": [3, 34],
    "label": "red"
  },
  { "id": "Tracer", "event": "step", "parameters": [101], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unnoticed",
    "parameters": [3],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Replace Right[1] with 74"],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unselect",
    "parameters": [4],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "notice",
    "parameters": [4, 74],
    "label": "red"
  },
  { "id": "Tracer", "event": "step", "parameters": [113], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unnoticed",
    "parameters": [4],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Merged Array: [34, 74]"],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Divide: Left[3,4] and Right[5,5]"],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "select",
    "parameters": [3],
    "label": "blue"
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Insert value 34 into Left [0]"],
    "label": ""
  },
  { "id": "Tracer", "event": "step", "parameters": [70], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "select",
    "parameters": [5],
    "label": "blue"
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Insert value 84 into Right [0]"],
    "label": ""
  },
  { "id": "Tracer", "event": "step", "parameters": [78], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "select",
    "parameters": [4],
    "label": "blue"
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Insert value 74 into Left [1]"],
    "label": ""
  },
  { "id": "Tracer", "event": "step", "parameters": [70], "label": "" },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Left:[34, 74] and Right:[84]"],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Replace Left[0] with 34"],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unselect",
    "parameters": [3],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "notice",
    "parameters": [3, 34],
    "label": "red"
  },
  { "id": "Tracer", "event": "step", "parameters": [101], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unnoticed",
    "parameters": [3],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Replace Left[1] with 74"],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unselect",
    "parameters": [4],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "notice",
    "parameters": [4, 74],
    "label": "red"
  },
  { "id": "Tracer", "event": "step", "parameters": [101], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unnoticed",
    "parameters": [4],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Replace Right[2] with 84"],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unselect",
    "parameters": [5],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "notice",
    "parameters": [5, 84],
    "label": "red"
  },
  { "id": "Tracer", "event": "step", "parameters": [113], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unnoticed",
    "parameters": [5],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Merged Array: [34, 74, 84]"],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Divide: Left[0,2] and Right[3,5]"],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "select",
    "parameters": [0],
    "label": "blue"
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Insert value 34 into Left [0]"],
    "label": ""
  },
  { "id": "Tracer", "event": "step", "parameters": [70], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "select",
    "parameters": [3],
    "label": "blue"
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Insert value 34 into Right [0]"],
    "label": ""
  },
  { "id": "Tracer", "event": "step", "parameters": [78], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "select",
    "parameters": [1],
    "label": "blue"
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Insert value 64 into Left [1]"],
    "label": ""
  },
  { "id": "Tracer", "event": "step", "parameters": [70], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "select",
    "parameters": [4],
    "label": "blue"
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Insert value 74 into Right [1]"],
    "label": ""
  },
  { "id": "Tracer", "event": "step", "parameters": [78], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "select",
    "parameters": [2],
    "label": "blue"
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Insert value 70 into Left [2]"],
    "label": ""
  },
  { "id": "Tracer", "event": "step", "parameters": [70], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "select",
    "parameters": [5],
    "label": "blue"
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Insert value 84 into Right [2]"],
    "label": ""
  },
  { "id": "Tracer", "event": "step", "parameters": [78], "label": "" },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Left:[34, 64, 70] and Right:[34, 74, 84]"],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Replace Left[0] with 34"],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unselect",
    "parameters": [0],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "notice",
    "parameters": [0, 34],
    "label": "red"
  },
  { "id": "Tracer", "event": "step", "parameters": [101], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unnoticed",
    "parameters": [0],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Replace Right[1] with 34"],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unselect",
    "parameters": [1],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "notice",
    "parameters": [1, 34],
    "label": "red"
  },
  { "id": "Tracer", "event": "step", "parameters": [95], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unnoticed",
    "parameters": [1],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Replace Left[2] with 64"],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unselect",
    "parameters": [2],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "notice",
    "parameters": [2, 64],
    "label": "red"
  },
  { "id": "Tracer", "event": "step", "parameters": [101], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unnoticed",
    "parameters": [2],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Replace Left[3] with 70"],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unselect",
    "parameters": [3],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "notice",
    "parameters": [3, 70],
    "label": "red"
  },
  { "id": "Tracer", "event": "step", "parameters": [101], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unnoticed",
    "parameters": [3],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Replace Right[4] with 74"],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unselect",
    "parameters": [4],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "notice",
    "parameters": [4, 74],
    "label": "red"
  },
  { "id": "Tracer", "event": "step", "parameters": [113], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unnoticed",
    "parameters": [4],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Replace Right[5] with 84"],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unselect",
    "parameters": [5],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "notice",
    "parameters": [5, 84],
    "label": "red"
  },
  { "id": "Tracer", "event": "step", "parameters": [113], "label": "" },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "unnoticed",
    "parameters": [5],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Merged Array: [34, 34, 64, 70, 74, 84]"],
    "label": ""
  },
  {
    "id": "f2aa7ffe-7b54-4bc1-8418-d88de2991d3e",
    "event": "print",
    "parameters": ["Sorted Array: [34, 34, 64, 70, 74, 84]"],
    "label": ""
  },
  {
    "id": "299992fe-ea78-492f-a1a4-2da4269015b9",
    "event": "select_range",
    "parameters": [0, 5],
    "label": "green"
  },
  { "id": "Tracer", "event": "step", "parameters": [135], "label": "" }
]
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
