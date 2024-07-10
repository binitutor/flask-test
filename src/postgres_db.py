import sqlalchemy
import config as cfg

class PostgresDb:
    def __init__(self):
        self.app = None
        self.driver = None

    def init_app(self, app):
        self.app = app
        self.connect()

    def connect(self):
        self.driver = sqlalchemy.create_engine(cfg.DB_URL, pool_size=30)
        return self.driver
    
    def get_db(self):
        if not self.driver:
            return self.connect()
        return self.driver