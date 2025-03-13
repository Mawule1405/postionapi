import psycopg2
from psycopg2 import OperationalError
from contextlib import contextmanager
from ..config import settings
import logging

# Optional: Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseManager:
    @contextmanager
    def get_connection(self):
        config = settings.Config()
        try:
            conn = psycopg2.connect(
                dbname=config.DB_NAME,
                user=config.DB_USER,
                password=config.DB_PASSWORD,
                host=config.DB_HOST,
                port=config.DB_PORT
            )
            logger.info("Database connection established.")
            yield conn
        except OperationalError as e:
            logger.error(f"Error connecting to the database: {e}")
            raise
        finally:
            if conn:
                conn.close()
                logger.info("Database connection closed.")

    @contextmanager
    def get_cursor(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            try:
                yield cursor
                conn.commit()
            except Exception as e:
                logger.error(f"Error during database operation: {e}")
                conn.rollback()
                raise
            finally:
                cursor.close()
                logger.info("Cursor closed.")
