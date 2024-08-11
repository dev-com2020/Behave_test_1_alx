import unittest
from unittest import mock
from event import Event


# class EventTest(unittest.TestCase):
#     def test_a_listener(self):
#         called = False
#
#         def listener():
#             nonlocal called
#             called = True
#
#         event = Event()
#         event.connect(listener)
#         event.fire()
#         self.assertTrue(called)

# class EventTest(unittest.TestCase):
#     def test_a_listener(self):
#         listener = Mock()
#         event = Event()
#         event.connect(listener)
#         event.fire()
#         self.assertTrue(listener.called)
#
#     def test_a_listener_with_params(self):
#         listener = Mock()
#         event = Event()
#         event.connect(listener)
#         event.fire(456, imie="Tomek")
#         self.assertEquals(((456,), {"imie": "Tomek"}), listener.params)

class EventTest(unittest.TestCase):
    def test_a_listener(self):
        listener = mock.Mock()
        event = Event()
        event.connect(listener)
        event.fire()
        self.assertTrue(listener.called)
