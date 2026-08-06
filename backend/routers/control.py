from fastapi import APIRouter

from backend.services.command_service import CommandService



router=APIRouter(

    prefix="/control",

    tags=["Control"]

)



service=CommandService()



@router.post("/command/{cmd}")
def command(cmd:str):


    return service.execute(
        cmd.upper()
    )
