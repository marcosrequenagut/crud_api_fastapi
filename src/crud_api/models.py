"""
This is the models module
"""

from pydantic import BaseModel, Field, field_validator

class Project(BaseModel):
    """
    This class models a project where the users can report their time spent.
    
    :param name: The name of the project.
    :param time: How much time has been spent on the project.
    """
    
    name: str
    time: int = Field(ge=0)

    @field_validator("time", model="before")
    def time_must_be_positive(cls, value):
        if isinstance(value, int):
            if value < 0:
                print("WARNING, the time of a project can't be negative, defaulting to zero")
                return 0 
            else:
                return value
        raise ValueError