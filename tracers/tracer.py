import uuid
import json


class Tracer:
    events = []
    count = 0

    def __init__(self):
        self.id = uuid.uuid4()

    @classmethod
    def trace(cls, id, event_name: str, parameters: [str]) -> None:
        event = {
            "id": str(id),
            "event": event_name,
            "parameters": json.loads(json.dumps(parameters))
        }
        cls.events.append(event)

    @classmethod
    def step(cls, line_number):
        cls.trace('Tracer', 'step', [line_number])

    @classmethod
    def get_all_events(cls):
        return cls.events
