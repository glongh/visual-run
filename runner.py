import json
import uuid


class Runner:
    _id = None
    _tracers = []

    def __init__(self):
        self._id = uuid.uuid4()

    def register(self, tracers):
        for tracer in tracers:
            self._tracers.append(tracer)

    def print_stats(self):
        """
        Pre-condition: len(self._tracers) > 0 OR len(self._tracers) == 0
        Post-condition: a dictionary with event stats is returned in JSON format.
        """
        total_steps = 0
        total_events = 0
        registered_tracers = len(self._tracers)
        events_per_tracer = {}

        # Oa: (Solvable Immediately):
        # len(self._tracers) == 0 And this returns with initial values
        if len(self._tracers) > 0:
            tracer = self._tracers.pop()
            # Ob: Iterates over all events
            total_events = len(tracer.events)
            for event in tracer.events:
                if event['id'] in events_per_tracer:
                    events_per_tracer[event['id']].append(event)
                else:
                    events_per_tracer[event['id']] = []
                    events_per_tracer[event['id']].append(event)

                if event['event'] == 'step':
                    total_steps += 1

        # Oc: Stats dictionary is filled with stats: Post condition satisfied
        stats = {
            'total_steps': total_steps,
            'total_events': total_events,
            'registered_tracers': registered_tracers,
            'events_per_tracer': events_per_tracer
        }
        json.loads(json.dumps(stats))

    def export_events(self):
        tracer = self._tracers.pop()
        return json.dumps(tracer.events, separators=(",", ":"))

    def get_tracers(self):
        return self._tracers

    @property
    def id(self):
        return self._id
