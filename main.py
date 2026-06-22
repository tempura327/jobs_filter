from fastapi import FastAPI

from src.job.router import router as jobs_router

app = FastAPI()

app.include_router(jobs_router, prefix='/jobs', tags=['Jobs'])
