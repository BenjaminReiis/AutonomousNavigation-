from fastapi import APIRouter
from fastapi import WebSocket

from backend.websocket.manager import ConnectionManager



router = APIRouter(
    tags=["WebSocket"]
)


manager = ConnectionManager()



@router.websocket("/ws")
async def websocket_endpoint(
    websocket:WebSocket
):


    await manager.connect(
        websocket
    )


    try:


        while True:


            data = await websocket.receive_json()



            await manager.broadcast(

                {

                    "received":data

                }

            )


    except Exception:


        manager.disconnect(
            websocket
        )
