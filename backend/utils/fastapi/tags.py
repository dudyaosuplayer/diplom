from enum import Enum


class Tags(str, Enum):
    projects = 'Projects'
    tasks = 'Tasks'
    users = 'Users'
    comments = 'Comments'
    authentication = 'Authentication'
