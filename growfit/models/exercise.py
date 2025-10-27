"""
Exercise data model for GrowFit application.

PURPOSE:
--------
This module defines the Exercise data structure and will serve as a data validation
and cleaning layer BEFORE saving to CSV files. It will ensure that all exercise data
stored in CSV files (and later analyzed in Power BI) is clean, consistent, and valid.

FUTURE RESPONSIBILITIES:
------------------------
1. Define the structure and data types of an Exercise
2. Validate data integrity (ranges, required fields, logical consistency)
3. Normalize data format (text formatting, null handling, type conversions)
4. Prepare clean data for CSV export
5. Ensure Power BI receives high-quality, analysis-ready data

WORKFLOW:
---------
User Input → Exercise (validate/clean) → to_csv_row() → DataManager → CSV → Power BI

WILL NOT:
---------
- Calculate complex metrics (that's for Power BI/DAX)
- Interact with CSV files directly (that's DataManager's job)
- Contain business logic for recommendations (that's for ML models)

This will be a DATA GATEKEEPER: only clean, valid data passes through to storage.
"""

from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Exercise:
    """
    Exercise data model.
    
    Attributes:
        exercise_id (str): Unique identifier for the exercise
        exercise_name (str): Human-readable name of the exercise
        exercise_category (str): Category classification (e.g., 'strength', 'cardio')
        difficulty_level (int): Difficulty rating from 1-10
        body_part (str): Primary body part targeted
        sets (int): Number of sets to perform
        reps (int): Number of repetitions per set
        rest_between_sets_sec (int): Rest time between sets in seconds
        exercise_order (int): Order within the routine
        exercise_status (str): Current status ('active', 'completed', 'skipped')
        exercise_weight_kg (Optional[float]): Weight used for the exercise
        hold_seconds (Optional[int]): Hold time for isometric exercises
        exercise_updated (Optional[datetime]): Last modification timestamp
    """
    
    # Required fields
    exercise_id: str
    exercise_name: str
    exercise_category: str
    difficulty_level: int
    body_part: str
    sets: int
    reps: int
    rest_between_sets_sec: int
    exercise_order: int
    
    # Optional fields with defaults
    exercise_status: str = "active"
    exercise_weight_kg: Optional[float] = None
    hold_seconds: Optional[int] = None
    exercise_updated: Optional[datetime] = None