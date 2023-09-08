# Import dataclass
from dataclasses import dataclass

@dataclass
class WeightEntry:
    # Define the fields on the class
    species: str
    body_mass: int
    flippper_length: int
    sex: str
        
    # Define a property that returns the body_mass / flipper_length
    @property
    def mass_to_flipper_length_ratio(WeightEntry):
        return WeightEntry.body_mass / WeightEntry.flippper_length
