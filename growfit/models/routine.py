"""
Routine Data model for GrowFit application.

PURPOSE:
--------
This module defines the RoutineData structure for HISTORICAL tracking of routine executions.
This corresponds to the `routines_data.csv` file that stores historical records for 
machine learning model training and Power BI analytics.

FUTURE RESPONSIBILITIES:
------------------------
1. Define the structure and data types of a completed routine execution
2. Validate data integrity for routine execution records
3. Normalize data format for consistent historical tracking
4. Prepare clean data for CSV export (routines_data.csv)
5. Ensure Power BI receives high-quality routine execution analytics data

WORKFLOW:
---------
User completes routine → RoutineData (validate/clean) → DataManager → routines_data.csv → Power BI/ML

DATA USAGE:
-----------
This historical data will be used for:
- Tracking routine completion rates
- Analyzing workout frequency patterns
- Measuring exercise counts per routine
- Training ML models for routine recommendations
- Calculating user engagement metrics

DOES NOT:
---------
- Manage active routine definitions (that's routines.csv)
- Calculate complex metrics (that's for Power BI/DAX)
- Contain recommendation logic (that's for ML models)
"""

from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class RoutineData:
    """
    Historical record of a routine execution.
    
    Attributes:
        session_id (str): Unique identifier linking to session_data.csv
        routine_id (str): Identifier of the routine that was executed
        routine_name (str): Human-readable name of the routine
        routine_type (str): Type classification (e.g., 'strength', 'cardio', 'mixed')
        routine_start_time (datetime): When the routine started
        routine_end_time (Optional[datetime]): When the routine finished (None if incomplete)
        exercise_count (int): Number of exercises in this routine execution
        all_exercises_completed (bool): Whether all exercises were completed
    """
    
    # Required fields
    session_id: str
    routine_id: str
    routine_name: str
    routine_type: str
    routine_start_time: datetime
    exercise_count: int
    all_exercises_completed: bool
    
    # Optional fields
    routine_end_time: Optional[datetime] = None
