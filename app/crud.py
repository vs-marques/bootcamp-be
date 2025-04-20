from sqlalchemy.ext.asyncio import AsyncSession
from .models import CalculatorSubmissionTable
from .schemas import CalculatorSubmission
from uuid import UUID
from sqlalchemy.future import select

async def create_submission(db: AsyncSession, submission: CalculatorSubmission):
    db_submission = CalculatorSubmissionTable(**submission.dict())
    db.add(db_submission)
    await db.commit()
    await db.refresh(db_submission)
    return db_submission

async def get_submissions(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(
        "SELECT * FROM calculator_submissions OFFSET :skip LIMIT :limit", 
        {"skip": skip, "limit": limit}
    )
    return result.scalars().all()

##async def get_submission_by_id(db: AsyncSession, submission_id: UUID):
##    result = await db.execute(
##        "SELECT * FROM calculator_submissions WHERE id = :id",
##        {"id": submission_id}
##    )
##    return result.scalar()

# Função para buscar uma submissão pelo ID
async def get_submission_by_id(db: AsyncSession, submission_id: UUID):
    # Usando a consulta SELECT com o filtro de ID
    query = select(CalculatorSubmissionTable).filter(CalculatorSubmissionTable.id == submission_id)
    result = await db.execute(query)  # Executa a consulta no banco
    submission = result.scalars().first()  # Retorna o primeiro resultado ou None
    return submission

async def update_submission(db: AsyncSession, submission_id: UUID, submission: CalculatorSubmission):
    db_submission = await get_submission_by_id(db, submission_id)
    if db_submission:
        for key, value in submission.dict(exclude_unset=True).items():
            setattr(db_submission, key, value)
        await db.commit()
        await db.refresh(db_submission)
        return db_submission
    return None

async def delete_submission(db: AsyncSession, submission_id: UUID):
    db_submission = await get_submission_by_id(db, submission_id)
    if db_submission:
        await db.delete(db_submission)
        await db.commit()
        return {"message": "Submission deleted successfully."}
    return {"message": "Submission not found."}