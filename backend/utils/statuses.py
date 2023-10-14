from enum import Enum

class ProjectStatus(str, Enum):
    Active = 'Active'
    Inactive = 'Inactive'
    
    
class TaskStatus(str, Enum):
    InWork = 'In Work'
    Complete = 'Complete'
    Postponed = 'Postponed'
