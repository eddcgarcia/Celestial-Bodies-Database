from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from galaxy import Galaxy
from star import Star
from planet import Planet
from moon import Moon
from asteroid import Asteroid
from base import Base

from random import seed, uniform, randrange

engine = create_engine('postgresql://freecodecamp@localhost:5432/universe')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

seed(42)

for g in range(6):
    g_name = f'galaxy_g{g}'
    galaxy = Galaxy(g_name, randrange(1000), randrange(1000), randrange(10000), \
        f'This is {g_name}', False, False)
    session.add(galaxy) 
    for a in range(6):
        a_name = f'asteroid_g{g}_a{a}'
        asteroid = Asteroid(a_name, randrange(1000), randrange(1000), randrange(10000), \
            f'This is {a_name}', False, False, galaxy)  
        session.add(asteroid)
    for s in range(6):
        s_name = f'star_g{g}_s{s}'
        star = Star(s_name, randrange(1000), randrange(1000), randrange(10000), \
            f'This is {s_name}', False, False, galaxy)  
        session.add(star)
        for p in range(12):
            p_name = f'planet_g{g}_s{s}_p{p}'
            planet = Planet(p_name, randrange(1000), randrange(1000), randrange(10000), \
                f'This is {p_name}', False, False, star)  
            session.add(planet)
            for m in range(20):
                m_name = f'moon_g{g}_s{s}_p{p}_m{m}'
                moon = Moon(m_name, randrange(1000), randrange(1000), randrange(10000), \
                    f'This is {m_name}', False, False, planet)  
                session.add(moon)

session.commit()
session.close()
