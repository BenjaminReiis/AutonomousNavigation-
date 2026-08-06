class Detection:

    def __init__(
        self,
        name,
        confidence
    ):

        self.name = name

        self.confidence = confidence



class Obstacle:

    def __init__(
        self,
        detected
    ):

        self.detected = detected
