from fastapi import APIRouter

router = APIRouter(prefix="/robots", tags=["Robots"])


@router.get("/")
def list_robots():

    return {
        "robots": []
    }


@router.get("/{robot_id}")
def get_robot(robot_id: int):

    return {
        "robot": robot_id
    }
