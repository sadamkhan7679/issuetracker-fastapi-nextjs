from fastapi import   APIRouter, HTTPException          


router = APIRouter(prefix="/api/v1/issues", tags=["issues"])

@router.get("/")
def get_issues():
    return []

