from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from backend.models.base import Base


class Mission(Base):

    __tablename__ = "missions"

    id = Column(Integer, primary_key=True)

    robot_id = Column(Integer, ForeignKey("robots.id"))

    origin = Column(String)

    destination = Column(String)

    status = Column(String)
