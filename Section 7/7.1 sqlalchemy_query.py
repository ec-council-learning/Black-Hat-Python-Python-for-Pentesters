from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_declarative import Base, Cars

engine = create_engine("sqlite:///sqlalchemy_example.db")

Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

# Query all entries in database
cars = session.query(Cars).all()
for car in cars:
    print(car.name)

# Return first entry in database
car = session.query(Cars).first()
print("\n" + car.name)

# Return the car with given price
priced_car = session.query(Cars).filter(Cars.price == 25000).one()
print("\n" + priced_car.name + "\n")

# Return all the cars with a given price
priced_cars = session.query(Cars).filter(Cars.price == 26000).all()
for car in priced_cars:
    print(car.name)
