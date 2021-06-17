from .tracer import Tracer


class Array(Tracer):

    def __init__(self) -> None:
        super().__init__()

    def init(self, params):
        self.trace(self.id, 'init', params)

    def reset(self):
        self.trace(self.id, 'reset', [])

    def select(self, index):
        self.trace(self.id, 'select', [index])

    def unselect(self, index):
        self.trace(self.id, 'unselect', [index])

    def select_range(self, start, end):
        self.trace(self.id, 'select_range', [start, end])

    def unselect_range(self, start, end):
        self.trace(self.id, 'unselect_range', [start, end])
