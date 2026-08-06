class Prediction:


    def estimate_position(

        self,

        position,

        velocity,

        time

    ):


        x = position[0] + velocity[0] * time


        y = position[1] + velocity[1] * time


        return (

            x,

            y

        )
