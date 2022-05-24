from sqlalchemy import Column, Integer, Float, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Cars(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True)
    manufacturer = Column(String(length=50), nullable=False)
    name = Column(String(length=250), nullable=False)
    type = Column(String(length=25), nullable=False)
    price = Column(Float, nullable=False)


engine = create_engine("sqlite:///sqlalchemy_example.db")

Base.metadata.create_all(engine)
