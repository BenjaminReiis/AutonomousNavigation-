from slam.slam_engine import SLAMEngine



def test_slam():


    slam=SLAMEngine()


    result=slam.process(

        {
            "latitude":10,

            "longitude":20
        },


        {
            "yaw":90
        },


        [
            1,
            10,
            20
        ]

    )


    assert "position" in result
