import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    year_of_birth: str
    month_of_birth: str
    day_of_birth: str
    subject: str
    hobbie: str
    image: str
    address: str
    state: str
    city: str
