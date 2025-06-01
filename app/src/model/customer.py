from sqlalchemy import Column , String , Integer
from src.core.base import Base


class Customer(Base):
    __tablename__ = "customers"

    id =  Column(Integer , primary_key=True)
    username = Column(String , nullable=False)
    password = Column(String , nullable=False)
    