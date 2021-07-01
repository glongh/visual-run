from .tracer import Tracer


class Logger(Tracer):

    def __init__(self) -> None:
        super().__init__()

    def print(self, log, label = ''):
        self.trace(self.id, 'print', [log], label)
