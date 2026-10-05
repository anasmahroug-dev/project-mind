from app.goal_manager.goal_manager import GoalManager
from app.state.mind_state import MindState
from app.events.base_event import Event
from app.actions.action_manager import ActionManager
from app.actions.action import Action
from app.thinking.thought import Thought
from app.perception.percept import Percept
from app.state.goal import Goal
from app.perception.perception import Perception
from app.brain.state_updater import StateUpdater
from app.thinking.thinking import Thinking
from app.brain.decision import Decision
from app.attention.attention import Attention
from app.mood.mood_manager import MoodManager
from app.brain.appraisal import Appraisal



class Brain:
    def __init__(self):
        
        self.perception = Perception()

        self.state_updater = StateUpdater()

        self.thinking = Thinking()

        self.attention = Attention()
        
        self.goal_manager = GoalManager()
        
        self.decision = Decision()
        
        self.action_manager = ActionManager()
        
        self.mood_manager = MoodManager()
        
        self.appraisal = Appraisal()
        
    def step(
        self,
        state: MindState,
        events: list[Event]
    ) -> tuple[MindState, list[Percept], list[Thought], Thought | None, Goal | None, Action | None]:
        
        new_state = state.model_copy(deep=True)
        
        
        self.state_updater.process(new_state)
        self.mood_manager.process(new_state)
        self.appraisal.process(new_state, events)
        
        percepts = self.perception.process(new_state, events) 
        thoughts = self.thinking.process(new_state, percepts)
        focused_thought = self.attention.focus(thoughts, new_state)
        
        goal = new_state.current_goal
        action = None
 
        if new_state.current_action is not None:
            
            if self.action_manager.should_interrupt(
                new_state.current_action,
                events,
                new_state):
                self.action_manager.interrupt_current_action(new_state)
                
            else:
                action = self.action_manager.process_current_action(new_state)
                
                return (
                    new_state,
                    percepts,
                    thoughts,
                    focused_thought,
                    goal,
                    action
                )
                
        goal = self.goal_manager.process(focused_thought,
                                         new_state)
        new_state.current_goal = goal
      
        action = self.action_manager.process(goal, new_state)
        
        new_state.current_action = action

        return new_state, percepts, thoughts, focused_thought, goal, action