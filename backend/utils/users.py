from enum import Enum

class ProjectRole(str, Enum):
    ProductManager = 'Product Manager'
    Developer = 'Developer'
    Tester = 'Tester'
    