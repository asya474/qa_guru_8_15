import datetime

from tests_demo.users.users import User

Charles_Leclerc = User(
    first_name='Charles',
    last_name='Leclerc',
    email='CL16@test.com',
    gender='Male',
    number='7900900909',
    date_of_birth=datetime.date(day=16, month=10, year=1997),
    subject='Arts',
    hobbies='Sports',
    image='character.png',
    address='Monaco, Avenue de la Costa',
    state='Haryana',
    city='Panipat',
)