from sevo.events import Event, EventEmitter


class CounterEvent(Event):

    COUNTER_STARTED = "COUNTER_STARTED"
    COUNTER_CHANGED = "COUNTER_CHANGED"
    COUNTER_FINISHED = "COUNTER_FINISHED"


    def __init__(self, type: str, sender: object, params: dict = {}) -> None:
        super().__init__(type, sender, params)

    


class Counter:
    _start: int
    _stop: int
    _step: int
    _count: int
    _event_emitter: EventEmitter

    def __init__(self, start: int = 0, stop: int = 10, step: int = 1) -> None:
        self._event_emitter = EventEmitter()
        self.reset(start, stop, step)

    def reset(self, start: int = 0, stop: int = 10, step: int = 1) -> None:
        self._start = start
        self._stop = stop
        self._step = step
        self._count = self._start

    def run(self) -> None:
        self._count = self._start
        # print("START", self._count)
        self._event_emitter.emit(CounterEvent(CounterEvent.COUNTER_STARTED, self, {"count": self._count}))
        for self._count in range(self._start, self._stop, self._step):
            # print("CHANGE", self._count)
            self._event_emitter.emit(CounterEvent(CounterEvent.COUNTER_CHANGED, self, {"count": self._count}))
        #print("FINISH", self._count)
        self._event_emitter.emit(CounterEvent(CounterEvent.COUNTER_FINISHED, self, {"count": self._count}))

    
    def get_count(self) -> int:
        return self._count
    
    def get_event_emitter(self) -> EventEmitter:
        return self._event_emitter
