from fastapi import APIRouter, HTTPException
from growfit.core.data_manager import DataManager

router = APIRouter()
data_manager = DataManager()

"""
API REST endpoints for data access in GrowFit backend.
- Exposes user_profile, routines, session_data, and device_id as JSON endpoints.
- Only accessible via API REST (no direct access from frontend/UI).
"""

@router.get("/user_profile")
def get_user_profile():
    """Get user profile data as JSON (for API REST)."""
    try:
        df = data_manager.get_csv("user_profile")
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/routines")
def get_routines():
    """Get routines data as JSON (for API REST)."""
    try:
        df = data_manager.get_csv("routines")
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/session_data")
def get_session_data():
    """Get session data as JSON (for API REST)."""
    try:
        df = data_manager.get_csv("session_data")
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/device_id")
def get_device_id():
    """Get device_id as JSON (for API REST)."""
    try:
        return {"device_id": data_manager.get_device_id()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
