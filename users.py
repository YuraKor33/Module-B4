import datetime

import sqlalchemy as sa 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()

class User(Base):
	__tablename__ = 'user'

	id = sa.Column(sa.Integer, primary_key=True)
	first_name = sa.Column(sa.Text)
	last_name = sa.Column(sa.Text)
	gender = sa.Column(sa.Text)
	email = sa.Column(sa.Text)
	birthdate = sa.Column(sa.Text)
	height = sa.Column(sa.Float)

def connect_db():
	# Устанавливает соединение с БД 
	engine = sa.create_engine(DB_PATH)
	Base.metadata.create_all(engine)
	session = sessionmaker(engine)
	return session()

def reqest_data():
	# Регистрация пользователя
	print("Привет! Я запишу твои данные!")
	first_name = input("Введите свое имя: ")
	last_name = input("А теперь фамилию: ")
	gender = input("Введите пол (варианты: Male, Female): ")
	email = input("Введите адрес твоей электронной почты: ")
	birthdate = input("Введите дату рождения в формате ГГГГ-ММ-ДД (пример: 2000-01-01): ")
	height = input("Введите рост в метрах (пример: 1.78): ")

	user = User(
		first_name = first_name,
		last_name = last_name,
		gender = gender,
		email = email,
		birthdate = birthdate,
		height = height
		)
	return user

def main():
	session = connect_db()
	user = reqest_data()
	session.add(user)
	session.commit()
	print("Данные сохранены")
if __name__ == "__main__":
	main()