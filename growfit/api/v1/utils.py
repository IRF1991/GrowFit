from fastapi import APIRouter
from pydantic import BaseModel
from growfit.core import utils

router = APIRouter()

"""
API REST endpoints for utility functions in GrowFit backend.
- Exposes increment_counter, reduce_counter, and count_down as JSON endpoints.
- Only accessible via API REST (no direct access from frontend/UI).
"""

class CounterRequest(BaseModel):
    counter: int

@router.post("/increment_counter")
def increment_counter(req: CounterRequest):
    """Increment counter (API REST endpoint)."""
    result = utils.increment_counter(req.counter)
    return {"result": result}

@router.post("/reduce_counter")
def reduce_counter(req: CounterRequest):
    """Reduce counter (API REST endpoint)."""
    result = utils.reduce_counter(req.counter)
    return {"result": result}

@router.post("/count_down")
def count_down(req: CounterRequest):
    """Count down to zero (API REST endpoint)."""
    result = utils.count_down(req.counter)
    return {"result": result}
