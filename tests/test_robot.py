from core.autonomous_system import AutonomousSystem



def test_robot_system():


    system=AutonomousSystem()


    result=system.run_cycle(

        (5,5)

    )


    assert "decision" in result

    assert "navigation" in result
