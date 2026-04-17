import psycopg2
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD


def connect():
    try:
        return psycopg2.connect(
            dbname = DB_NAME,
            host = DB_HOST,
            user = DB_USER,
            password = DB_PASSWORD)
    except Exception as e:
        print("❌ Connection error:", e)
        return None