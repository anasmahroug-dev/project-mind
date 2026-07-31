from app.brain.brain import Brain
from app.state.mind_state import MindState
from app.events.base_event import Event
from app.defaults.initial_state import create_initial_mind_state
import time
class Engine:

    def __init__(self):

        self.brain = Brain()

        self.state = create_initial_mind_state()

        self.event_queue = []

        self.tick_count = 0

        self.running = False
        
    def run(self):

        self.running = True

        while self.running:

            self.step()

            time.sleep(1)
            
    def step(self):

        events = self.event_queue
        self.event_queue = []

        new_state, actions = self.brain.step(
            self.state,
            events,
        )

        self.state = new_state
        print(
        f"Tick {self.tick_count} | "
        f"Age: {self.state.age} | "
        f"Energy: {self.state.energy.level:.2f}"
        )
        self.tick_count += 1