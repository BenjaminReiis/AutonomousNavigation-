from backend.services.command_service import CommandService



def test_command():


    service=CommandService()


    result=service.execute(
        "START"
    )


    assert result["status"]=="running"
