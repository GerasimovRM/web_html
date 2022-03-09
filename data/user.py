from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relation

from data.db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String, nullable=False)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    position = Column(String, nullable=True)
    speciality = Column(String, nullable=True)
    address = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=True)
    modified_date = Column(DateTime, nullable=True)

    jobs_list = relation("Jobs", back_populates='team_leader_instance')

    def __repr__(self):
        return f"<Colonist> {self.id} {self.surname} {self.name}"
