import billboard
from datetime import datetime

def get_birthdate_number_one(birthdate_str: str):
try:
  birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
except ValueError:
  
