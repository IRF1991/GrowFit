"""
App Lifecycle Data model for GrowFit application.

PURPOSE:
--------
This module defines the AppLifecycleData structure for HISTORICAL tracking of app usage events.
This corresponds to the `app_lifecycle_data.csv` file that stores historical records for 
machine learning model training and Power BI analytics.

FUTURE RESPONSIBILITIES:
------------------------
1. Define the structure and data types of app lifecycle events
2. Validate data integrity for event tracking
3. Normalize data format for consistent event logging
4. Prepare clean data for CSV export (app_lifecycle_data.csv)
5. Ensure Power BI receives high-quality user behavior analytics data

WORKFLOW:
---------
App event occurs → AppLifecycleData (validate/clean) → DataManager → app_lifecycle_data.csv → Power BI/ML

DATA USAGE:
-----------
This historical data will be used for:
- Tracking user retention and churn patterns
- Analyzing app usage frequency and session lengths
- Identifying feature adoption rates
- Measuring app stability (crashes, errors)
- Training ML models for user engagement predictions
- A/B testing and feature performance analysis

EVENT TYPES:
------------
Common event_type values:
- 'app_open': User opened the app
- 'app_close': User closed the app
- 'feature_used': User interacted with a specific feature
- 'error': An error occurred
- 'crash': App crashed
- 'screen_view': User navigated to a screen

DOES NOT:
---------
- Store user personal data (that's user_profile.csv)
- Calculate complex metrics (that's for Power BI/DAX)
- Contain recommendation logic (that's for ML models)
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class AppLifecycleData:
    """
    Historical record of an app lifecycle event.
    
    Attributes:
        event_id (str): Unique identifier for this event
        device_id (str): User's device identifier (us_xxx or te_xxx)
        event_type (str): Type of event (e.g., 'app_open', 'app_close', 'feature_used')
        event_timestamp (datetime): When the event occurred
        app_version (str): Version of the app when event occurred
    """
    
    # Required fields
    event_id: str
    device_id: str
    event_type: str
    event_timestamp: datetime
    app_version: str
