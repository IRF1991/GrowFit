"""Exercise model for GrowFit application."""

from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Exercise:
    """
    Exercise data model representing individual exercises in routines.
    
    Attributes:
        exercise_id (str): Unique identifier for the exercise
        exercise_name (str): Human-readable name of the exercise
        exercise_category (str): Category classification (e.g., 'strength', 'cardio')
        difficulty_level (int): Difficulty rating from 1-10
        body_part (str): Primary body part targeted
        exercise_weight_kg (Optional[float]): Weight used for the exercise
        sets (int): Number of sets to perform
        reps (int): Number of repetitions per set
        hold_seconds (Optional[int]): Hold time for isometric exercises
        rest_between_sets_sec (int): Rest time between sets in seconds
        exercise_order (int): Order within the routine
        exercise_status (str): Current status ('active', 'completed', 'skipped')
        exercise_updated (Optional[datetime]): Last modification timestamp
    """
    
    exercise_id: str
    exercise_name: str
    exercise_category: str
    difficulty_level: int
    body_part: str
    sets: int
    reps: int
    rest_between_sets_sec: int
    exercise_order: int
    exercise_status: str = "active"
    exercise_weight_kg: Optional[float] = None
    hold_seconds: Optional[int] = None
    exercise_updated: Optional[datetime] = None
    
    def __post_init__(self):
        """Post-initialization validation."""
        if self.exercise_updated is None:
            self.exercise_updated = datetime.now()
    
    @property
    def is_weighted(self) -> bool:
        """Check if exercise uses weights."""
        return self.exercise_weight_kg is not None and self.exercise_weight_kg > 0
    
    @property
    def is_isometric(self) -> bool:
        """Check if exercise is isometric (timed hold)."""
        return self.hold_seconds is not None and self.hold_seconds > 0
    
    def get_total_volume(self) -> float:
        """Calculate total volume (sets × reps × weight)."""
        if not self.is_weighted:
            return 0.0
        return self.sets * self.reps * self.exercise_weight_kg
    
    def get_estimated_duration(self) -> int:
        """Estimate total exercise duration in seconds."""
        # Base time per rep (assumption: 2 seconds per rep)
        rep_time = self.reps * 2 if not self.is_isometric else self.hold_seconds
        
        # Total time including rest between sets
        total_time = (rep_time * self.sets) + (self.rest_between_sets_sec * (self.sets - 1))
        
        return total_time