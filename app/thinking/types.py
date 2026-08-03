from enum import Enum


class ThoughtType(str, Enum):
    REST = "rest"

    WONDER = "wonder"

    RECALL_MEMORY = "recall_memory"

    FOCUS_ON_GOAL = "focus_on_goal"

    PLAN = "plan"

    OBSERVE_SELF = "observe_self"

    OBSERVE_USER = "observe_user"

    LEARN = "learn"

    EXPLORE = "explore"

    SPEAK = "speak"

    STAY_SILENT = "stay_silent"
