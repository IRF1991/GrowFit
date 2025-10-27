from fastapi import FastAPI
from growfit.api.v1 import user_profile, utils, data

app = FastAPI()
app.include_router(user_profile.router, prefix="/api/v1/user_profile")
app.include_router(utils.router, prefix="/api/v1/utils")
app.include_router(data.router, prefix="/api/v1/data")
