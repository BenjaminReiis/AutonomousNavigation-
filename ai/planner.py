import math


class PathPlanner:


    def calculate_distance(
        self,
        a,
        b
    ):

        return math.sqrt(

            (a[0]-b[0])**2 +

            (a[1]-b[1])**2

        )



    def choose_path(
        self,
        paths
    ):


        best = None

        distance = float("inf")


        for path in paths:


            value = 0


            for i in range(
                len(path)-1
            ):

                value += self.calculate_distance(

                    path[i],

                    path[i+1]

                )


            if value < distance:

                distance = value

                best = path


        return best
