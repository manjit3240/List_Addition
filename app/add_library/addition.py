from fastapi import HTTPException
from app.models.response import AdditionResponse
from app.views.addition_views import perform_addition
from datetime import datetime, timezone

def add_numbers(request):
    try:
        started_at = datetime.now(timezone.utc)
        result = perform_addition(request)
        completed_at = datetime.now(timezone.utc)
        return AdditionResponse(
            batchid=request.batchid,
            response=result,
            status="completed",
            started_at=started_at,
            completed_at=completed_at
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


