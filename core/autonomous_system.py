from sensors.sensor_manager import SensorManager

from navigation.navigation_engine import NavigationEngine

from ai.decision_engine import DecisionEngine

from slam.slam_engine import SLAMEngine

from core.robot import Robot

from core.telemetry_manager import TelemetryManager



class AutonomousSystem:



    def __init__(self):


        self.robot = Robot(

            "ANS-Robot-01"

        )


        self.sensors = SensorManager()


        grid=[

            [0]*20

            for i in range(20)

        ]


        self.navigation = NavigationEngine(

            grid

        )


        self.ai = DecisionEngine()


        self.slam = SLAMEngine()


        self.telemetry = TelemetryManager()




    def run_cycle(
        self,
        target
    ):


        data = self.sensors.collect_data()



        slam_result = self.slam.process(

            data["gps"],

            data["imu"],

            data["lidar"]["points"]

        )



        decision = self.ai.decide(

            [],

            False

        )



        if decision["action"]=="continue":


            navigation = self.navigation.navigate(

                (0,0),

                target,

                data["lidar"]["points"]

            )


        else:


            navigation={

                "status":"stopped"

            }



        self.robot.update_position(

            slam_result["position"]

        )


        self.robot.set_status(

            navigation["status"]

        )


        telemetry=self.telemetry.record(

            self.robot

        )



        return {


            "decision":decision,


            "navigation":navigation,


            "telemetry":telemetry


        }
