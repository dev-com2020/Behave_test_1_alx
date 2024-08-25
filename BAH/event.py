class Event:
    """
    Klasa makiety która obsługuje signal/slot
    """

    def __init__(self):
        self.listeners = []

    def connect(self, listener):
        self.listeners.append(listener)

    def fire(self, *args, **kwargs):
        for listener in self.listeners:
            listener(*args, **kwargs)


def handle_event(num):
    print("Złapałem numer {0}".format(num))

def handle_event2(num):
    print(f"Złapałem numer: {num}")

# event = Event()
# event.connect(handle_event)
# event.connect(handle_event2)
# event.fire(3)
# event.fire(10)