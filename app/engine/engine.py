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

        new_state, percepts, thoughts, focused_thought = self.brain.step( self.state,
        self.event_queue,)

        self.state = new_state
        print(f"\n========== Tick {self.tick_count} ==========")

        for percept in percepts:
            print(
            f"[PERCEPT] {percept.type.value} "
            f"({percept.intensity:.2f}) "
             f"from {percept.source.value}"
        )

        for thought in thoughts:
            print(
        f"[THOUGHT] {thought.type.value} "
        f"({thought.priority:.2f})"
        )

        if focused_thought is not None:
            print(
            f"[FOCUS] {focused_thought.type.value} "
            f"({focused_thought.priority:.2f})"
            )
            
        print(
        f"Age: {self.state.age} | "
        f"Energy: {self.state.energy.level:.2f}"
        )  
        self.tick_count += 1