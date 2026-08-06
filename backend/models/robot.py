from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

from backend.models.base import Base


class Robot(Base):

    __tablename__ = "robots"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100))

    status = Column(String(30))

    battery = Column(Float)

    latitude = Column(Float)

    longitude = Column(Float)

    speed = Column(Float)

    heading = Column(Float)
