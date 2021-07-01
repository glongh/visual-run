from .tracer import Tracer


class Array(Tracer):

    def __init__(self) -> None:
        super().__init__()

    def init(self, params):
        self.trace(self.id, 'init', params)

    def reset(self):
        self.trace(self.id, 'reset', [])

    def select(self, index, label=''):
        self.trace(self.id, 'select', [index], label)

    def unselect(self, index, label=''):
        self.trace(self.id, 'unselect', [index], label)

    def notice(self, index, new_value, label=''):
        self.trace(self.id, 'notice', [index, new_value], label)

    def unnoticed(self, index, label=''):
        self.trace(self.id, 'unnoticed', [index], label)

    def select_range(self, start, end, label=''):
        self.trace(self.id, 'select_range', [start, end], label)

    def unselect_range(self, start, end, label=''):
        self.trace(self.id, 'unselect_range', [start, end], label)
