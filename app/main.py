from fastapi import FastAPI, Depends, HTTPException
from .crud import create_submission, get_submissions, get_submission_by_id, update_submission, delete_submission
from .schemas import CalculatorSubmission
from .database import get_db
from uuid import UUID
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI()

@app.post("/calculator_submissions", response_model=CalculatorSubmission)
async def create_submission_route(submission: CalculatorSubmission, db: AsyncSession = Depends(get_db)):
    return await create_submission(db=db, submission=submission)

@app.get("/calculator_submissions", response_model=List[CalculatorSubmission])
async def get_submissions_route(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await get_submissions(db=db, skip=skip, limit=limit)

@app.get("/calculator_submissions/{submission_id}", response_model=CalculatorSubmission)
async def get_submission_route(submission_id: UUID, db: AsyncSession = Depends(get_db)):
    submission = await get_submission_by_id(db, submission_id)
    if not submission:
        raise HTTPException(status_code=404, detail="Submission not found")
    return submission

@app.put("/calculator_submissions/{submission_id}", response_model=CalculatorSubmission)
async def update_submission_route(submission_id: UUID, submission: CalculatorSubmission, db: AsyncSession = Depends(get_db)):
    return await update_submission(db=db, submission_id=submission_id, submission=submission)

@app.delete("/calculator_submissions/{submission_id}")
async def delete_submission_route(submission_id: UUID, db: AsyncSession = Depends(get_db)):
    return await delete_submission(db=db, submission_id=submission_id)

from sqlalchemy import text

@app.get("/ping-db")
async def ping_db(db: AsyncSession = Depends(get_db)):
    try:
        await db.execute(text("SELECT 1"))
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
