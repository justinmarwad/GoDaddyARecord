from godaddypy import Client, Account
from dotenv import load_dotenv
import os 

def create_or_update_record(domain, record_value, name, record_type="A", new=True): 
    load_dotenv()

    client = Client(Account(api_key=os.getenv("PUBLIC_KEY"), api_secret=os.getenv("SECRET_KEY")))


    data = client.add_record(domain, {
        "data": record_value, 
        "name": name", 
        "ttl": 600, 
        "type": record_type
    })

    print(data)


if __name__ == "__main__":
    create_or_update_record("cyberchallenge.us", "10.0.10.10", "test") 