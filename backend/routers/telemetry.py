from fastapi import APIRouter

router = APIRouter(prefix="/telemetry", tags=["Telemetry"])


@router.get("/")
def telemetry():

    return {
        "telemetry": []
    }
