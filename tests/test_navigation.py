from navigation.path_planner import AStarPlanner



def test_astar():


    grid=[

        [0,0,0],

        [1,1,0],

        [0,0,0]

    ]


    planner=AStarPlanner(grid)


    path=planner.search(
        (0,0),
        (2,2)
    )


    assert len(path)>0
