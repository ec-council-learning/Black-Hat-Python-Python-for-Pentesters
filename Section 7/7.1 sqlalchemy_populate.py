from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_declarative import Cars, Base

engine = create_engine("sqlite:///sqlalchemy_example.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

mustang = Cars(manufacturer="Ford", name="Mustang", type="Coupe", price=26000)
camaro = Cars(manufacturer="Chevy", name="Camaro", type="Coupe", price=25000)
jetta = Cars(manufacturer="Volkswagen", name="Jetta", type="Sedan", price=18000)
wrangler = Cars(manufacturer="Jeep", name="Wrangler", type="SUV", price=28000)
series_3 = Cars(manufacturer="BMW", name="320i", type="Sedan", price=35000)
renegade = Cars(manufacturer="Jeep", name="Renegade", type="SUV", price=26000)

items = (mustang, camaro, jetta, wrangler, series_3, renegade)

session.add_all(items)

session.commit()
