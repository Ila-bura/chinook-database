from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Programmer" table
class Switzerland(base):
    __tablename__ = "Switzerland"
    id = Column(Integer, primary_key=True)
    city_name = Column(String)
    canton_name = Column(String)
    language = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our Progammer table
zurich = Switzerland(
    city_name="Zürich",
    canton_name="Zürich",
    language="German"
)

lausanne = Switzerland(
    city_name="Lausanne",
    canton_name="Vaud",
    language="French"
)

basel = Switzerland(
    city_name="Basel",
    canton_name="Basel-Stadt",
    language="German"
)

bellinzona = Switzerland(
    city_name="Bellinzona",
    canton_name="Tessin",
    language="Italian"
)

# add each instance of our programmers to our session
# session.add(zurich)
# session.add(lausanne)
session.add(basel)

# commit our session to the database
# session.commit()


# query the database to find all Programmers
programmers = session.query(Switzerland)
for programmer in programmers:
    print(
        programmer.id,
        programmer.city_name,
        programmer.canton_name,
        programmer.language,
        sep=" | "
    )
