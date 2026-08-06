from navigation.path_planner import AStarPlanner

from navigation.obstacle_avoidance import ObstacleAvoidance

from navigation.controller import MotionController



class NavigationEngine:


    def __init__(self,grid):


        self.planner=AStarPlanner(
            grid
        )


        self.obstacle_system=ObstacleAvoidance()


        self.controller=MotionController()



    def navigate(self,start,target,lidar):


        obstacle=self.obstacle_system.check(
            lidar
        )


        if obstacle["blocked"]:


            return {


                "status":
                "obstacle_detected"


            }



        path=self.planner.search(
            start,
            target
        )


        return {


            "status":
            "moving",


            "path":
            path,


            "control":
            self.controller.move(
                path[0]
                if path else None
            )

        }
