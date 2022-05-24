from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker, mapper


class Places:
    """Empty class to populate with pre-existing data"""
    pass


engine = create_engine("sqlite:///places.sqlite")  # Access existing database

metadata = MetaData(engine)  # Link existing metadata
moz_urls = Table("moz_places", metadata, autoload=True)  # Capture desired table
mapper(Places, moz_urls)  # Map existing table data to empty class

Session = sessionmaker(bind=engine)
session = Session()

urls = session.query(Places).all()
for url in urls:
    print(url.url)
