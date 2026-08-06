import heapq


class Node:


    def __init__(self, position, parent=None):

        self.position = position

        self.parent = parent

        self.g = 0

        self.h = 0

        self.f = 0



    def __lt__(self, other):

        return self.f < other.f



class AStarPlanner:


    def __init__(self, grid):

        self.grid = grid



    def heuristic(self, a, b):

        return abs(a[0]-b[0]) + abs(a[1]-b[1])



    def neighbors(self, node):

        x,y = node.position


        moves = [

            (1,0),
            (-1,0),
            (0,1),
            (0,-1)

        ]


        result=[]


        for dx,dy in moves:

            nx=x+dx

            ny=y+dy


            if (

                0 <= nx < len(self.grid)

                and

                0 <= ny < len(self.grid[0])

                and

                self.grid[nx][ny] == 0

            ):

                result.append((nx,ny))


        return result



    def search(self,start,end):


        open_list=[]


        start_node=Node(start)

        end_node=Node(end)


        heapq.heappush(
            open_list,
            start_node
        )


        closed=set()



        while open_list:


            current=heapq.heappop(
                open_list
            )


            if current.position == end:


                path=[]


                while current:

                    path.append(
                        current.position
                    )

                    current=current.parent


                return path[::-1]



            closed.add(
                current.position
            )



            for pos in self.neighbors(current):


                if pos in closed:

                    continue



                child=Node(
                    pos,
                    current
                )


                child.g=current.g+1

                child.h=self.heuristic(
                    pos,
                    end
                )

                child.f=child.g+child.h



                heapq.heappush(
                    open_list,
                    child
                )



        return []
