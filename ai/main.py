from decision import RobotDecision

from planner import PathPlanner



decision = RobotDecision()

planner = PathPlanner()



state = decision.decide(

    False,

    80

)


print(

    "Robot action:",

    state

)
