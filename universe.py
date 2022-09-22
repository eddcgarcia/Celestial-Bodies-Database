from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from galaxy import Galaxy
from star import Star
from base import Base


engine = create_engine('postgresql://freecodecamp@localhost:5432/universe')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

galaxyA = Galaxy('galaxyA', 10, 10, 10, 'This is galaxyA', False, False)
starA = Star('starA', 10, 10, 10, 'This is starA', False, False, galaxyA)

session.add(galaxyA)
session.add(starA)

session.commit()
session.close()
