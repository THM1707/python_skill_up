from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://minh:password@localhost:3306/python_learning", echo=True, future=True)
