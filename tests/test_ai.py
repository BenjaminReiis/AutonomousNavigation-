from ai.decision_engine import DecisionEngine



def test_decision():


    ai=DecisionEngine()


    result=ai.decide(

        [],

        False

    )


    assert result["action"]=="continue"
