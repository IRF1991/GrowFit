"""
Session Data model for GrowFit application.

PURPOSE:
--------
This module defines the SessionData structure for HISTORICAL tracking of workout sessions.
This corresponds to the `session_data.csv` file that stores historical records for 
machine learning model training and Power BI analytics.

FUTURE RESPONSIBILITIES:
------------------------
1. Define the structure and data types of a workout session
2. Validate data integrity for session records
3. Normalize data format for consistent session tracking
4. Prepare clean data for CSV export (session_data.csv)
5. Ensure Power BI receives high-quality session analytics data

WORKFLOW:
---------
User starts workout → SessionData (validate/clean) → DataManager → session_data.csv → Power BI/ML

DATA USAGE:
-----------
This historical data will be used for:
- Tracking workout frequency and duration patterns
- Analyzing session completion rates
- Identifying user activity patterns (time of day, day of week)
- Training ML models for engagement predictions
- Calculating retention and adherence metrics

RELATIONSHIPS:
--------------
- One session can contain multiple routines (1:N with routines_data.csv)
- One session belongs to one device/user (N:1 with device_id)
- Sessions link exercises through session_id in exercise_data.csv

DOES NOT:
---------
- Store active session state (that's in-memory during workout)
- Calculate complex metrics (that's for Power BI/DAX)
- Contain recommendation logic (that's for ML models)
"""

from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class SessionData:
    """
    Historical record of a workout session.
    
    Attributes:
        session_id (str): Unique identifier for this session
        routine_id (str): Identifier of the routine executed in this session
        device_id (str): User's device identifier (us_xxx or te_xxx)
        session_type (str): Type of session (e.g., 'workout', 'practice', 'test')
        session_start_time (datetime): When the session started
        session_end_time (Optional[datetime]): When the session ended (None if incomplete)
    """
    
    # Required fields
    session_id: str
    routine_id: str
    device_id: str
    session_type: str
    session_start_time: datetime
    
    # Optional fields
    session_end_time: Optional[datetime] = None
