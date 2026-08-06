class OccupancyMap:


    def __init__(self,width,height):

        self.width = width

        self.height = height


        # 0 = livre
        # 1 = obstáculo

        self.grid = [

            [0 for x in range(width)]

            for y in range(height)

        ]



    def update(
        self,
        x,
        y,
        obstacle=False
    ):


        if (

            0 <= x < self.width

            and

            0 <= y < self.height

        ):


            if obstacle:

                self.grid[y][x]=1

            else:

                self.grid[y][x]=0



    def get_map(self):

        return self.grid
