from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc
from puppies import engine, Shelter, Puppy
from datetime import date

DBSession = sessionmaker(bind = engine)
session = DBSession()

print session.query(Puppy).order_by(asc(Puppy.name)).all()
print session.query(Puppy).filter(Puppy.date_of_birth > (date.now() + timedelta(days = 180))).order_by(desc(Puppy.date_of_birth)).all()
