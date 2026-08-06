from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import ForeignKey

from backend.models.base import Base


class Telemetry(Base):

    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True)

    robot_id = Column(Integer, ForeignKey("robots.id"))

    battery = Column(Float)

    temperature = Column(Float)

    cpu = Column(Float)

    ram = Column(Float)

    speed = Column(Float)

    latitude = Column(Float)

    longitude = Column(Float)
