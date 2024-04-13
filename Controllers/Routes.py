from ConfigDatabase.Database import MySQLDatabase
from fastapi import APIRouter

db = MySQLDatabase()
router = APIRouter()


@router.get('/')
async def read_root():
    return {
        'Message': 'Welcome to the MySQL API',
        'Endpoints': {
            '[GET] Database info': 'http://localhost:8000/db_info'
        }
    }


@router.get('/db_info')
async def get_bd_info():
    return {
        'Database info': {
            'Database': db.get_database_name(),
            'Number of tables': len(db.get_database_tables())
        }

    }

