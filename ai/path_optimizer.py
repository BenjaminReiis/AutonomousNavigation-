class PathOptimizer:


    def optimize(

        self,

        path

    ):


        result=[]


        for point in path:


            if point not in result:

                result.append(point)



        return result
