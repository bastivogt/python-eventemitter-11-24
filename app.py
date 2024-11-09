from counter import Counter, CounterEvent


c = Counter()

def c_counter_started(e: CounterEvent) -> None:
    print(e.get_type(), e.get_sender().get_count())

def c_counter_changed(e: CounterEvent) -> None:
    print(e.get_type(), e.get_params())

def c_counter_finished(e: CounterEvent) -> None:
    print(f"type: {e.get_type()}, count: {e.get_params()['count']}")


c.get_event_emitter().on(CounterEvent.COUNTER_STARTED, c_counter_started)
c.get_event_emitter().on(CounterEvent.COUNTER_CHANGED, c_counter_changed)
c.get_event_emitter().on(CounterEvent.COUNTER_FINISHED, c_counter_finished)

#c.get_event_emitter().off(CounterEvent.COUNTER_CHANGED, c_counter_changed)


c.run()
print(c.get_event_emitter())
