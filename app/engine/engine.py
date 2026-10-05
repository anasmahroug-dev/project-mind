from app.brain.brain import Brain
from app.state.mind_state import MindState
from app.events.base_event import Event
from app.events.event_types import EventType
from app.defaults.initial_state import create_initial_mind_state
from app.personality.modulation import reply_urge
import time
import queue

class Engine:

    def __init__(self, preset: str = "neutre", verbose: bool = True):

        self.brain = Brain()

        self.state = create_initial_mind_state(preset)

        self.inbox: queue.Queue[Event] = queue.Queue()

        self.tick_count = 0

        self.running = False
        
        self.verbose = verbose
    
    def submit(self, event: Event) -> None:
        self.inbox.put(event)
        
    def _drain_inbox(self) -> list[Event]:
        events = []
        while True:
            try:
                events.append(self.inbox.get_nowait())
            except queue.Empty:
                return events
        
    def run(self):

        self.running = True

        while self.running:

            self.step()

            time.sleep(1)
            
    def step(self):

        events = self._drain_inbox()

        new_state, percepts, thoughts, focused_thought, goal, action = self.brain.step(self.state,
        events)

        self.state = new_state
        if self.verbose:
            print(f"\n========== Tick {self.tick_count} ==========")
            if events:
                for event in events:
                    print(
                        f"[EVENT] {event.type.value} "
                        f"({event.content})"
                        )
                    if event.tone is not None:
                        print(
                            f"Tone: {event.tone.valence:.2f}, {event.tone.directed}"
                        )
            
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
                
            if goal is not None:
                print(
                f"[GOAL] {goal.type.value}"
                )
            
            if action is not None:
                print(
            f"[ACTION] {action.type.value} "
            f"(duration={action.duration}, remaining={action.remaining_ticks})"
        )
            print(
            f"Age: {self.state.age} | "
            f"Energy: {self.state.energy.level:.2f} | "
            f"Mood: {self.state.mood.dominant.value} ({self.state.mood.levels[self.state.mood.dominant]:.2f}) | "
            f"User Relationship: {self.state.relationship.affinity}"
            )  
        
        else:
            self._log_compact(events, action)
        self.tick_count += 1
        
            
    def _log_compact(self, events: list[Event], action) -> None:
        for event in events:
            tone = ""
            if event.tone is not None:
                kind = "adressé" if event.tone.directed else "non adressé"
                tone = f" (ton {event.tone.valence:+.2f}, {kind})"
            print(f"[MESSAGE] {event.content}{tone}")
        if events:
            relationship = self.state.relationship
            print(f"[RELATION] affinité {relationship.affinity:+.2f} | besoin {relationship.contact_need:.2f}"
                f" | envie de répondre {reply_urge(self.state.personality, relationship):.2f}")
        if action is not None and action.remaining_ticks == action.duration:
            print(f"[ACTION] {action.type.value}")