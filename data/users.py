import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    month_of_brith: str
    year_of_brith: str
    day_of_brith: str
    subject: str
    hobby: str
    picture: str
    current_address: str
    state: str
    city: str