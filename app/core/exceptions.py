from typing import Any

class FastApiUsersExceptions(Exception):
    pass

class InvalidIdError(FastApiUsersExceptions): 
    pass 

class UserAlreadyExistsError(FastApiUsersExceptions):
    pass 

class ProfileDoesNotExistsError(FastApiUsersExceptions):
    pass

class InvalidCredentialsError(FastApiUsersExceptions):
    pass