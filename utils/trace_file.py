from concurrent.futures import ThreadPoolExecutor
import os
from typing import List
from time import sleep
from random import randint


class TraceFile:
    def __init__(self, files_to_trace: List, workers=3) -> None:
        self.files = files_to_trace
        self.pool = ThreadPoolExecutor(max_workers=workers)
        self.tasks = []
        self.results = []

    def trace(self, file_name):
        status_result = 'ok'
        if os.system('python algorithms/{}'.format(file_name)) > 0:
            status_result = 'failed'
        return {file_name.replace('.py', ''): status_result}

    def trace_all(self):
        for file in self.files:
            task = self.pool.submit(self.trace, (file))
            self.tasks.append(task)

        while len(self.tasks) > 0:
            for task in self.tasks:
                if task.done():
                    self.results.append(task.result())
                    self.tasks.remove(task)

        return self.done()

    def done(self):
        result = self.results
        self.results = []
        self.tasks = []
        return result
