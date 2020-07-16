from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/restapi"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,echo=True
# )

engine = create_engine("mysql+mysqlconnector://root@localhost:3306/restapi",echo = True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()