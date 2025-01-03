from sqlalchemy import create_engine, Table, MetaData, select
from sqlalchemy.org import sessionmaker , declarative_base
from dotenv import load_dotenv
import os


class DataBeseMySQI:
    def __init__(self):
        load_dotenv()
        self.db_host = os.getenv('DB_HOST')
        self.db_user = os.getenv('DB_USER')
        self.db_password = os.getenv('DB_PASSWORD')
        self.db_name = os.getenv('DB_NAME')
        self.connect = f'mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_name}?charset=utf8mb4'
        self.engine = create_engine(self.connect)
        self.metadata = MetaData()
        self.Base = declarative_base()

        self.adminUser = Table('adminUser', self.metadata, autoload_with=self.engine)

        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def check_email(self, email):
        result = self.session.execute(select(self.adminUser).where(self.adminUser.c.email == email))
        return result.fetchone() is not None