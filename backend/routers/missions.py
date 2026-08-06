from fastapi import APIRouter

router = APIRouter(prefix="/missions", tags=["Missions"])


@router.get("/")
def missions():

    return {
        "missions": []
    }


@router.post("/start")
def start():

    return {
        "status": "started"
    }


@router.post("/stop")
def stop():

    return {
        "status": "stopped"
    }
