from typing import Any

class FastApiUsersExceptions(Exception):
    pass

class InvalidId(FastApiUsersExceptions): 
    pass 

class UserAlreadyExists(FastApiUsersExceptions):
    pass 
