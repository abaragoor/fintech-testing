from faker import Faker
faker = Faker()

def create_user_data():
    return {
        "name": faker.name(),
        "email": faker.unique.email(),
        "accountType": "premium"
    }

def create_transaction_data(user_id=None, recipient_id=None, amount=100.50):
    return {
        "userId": user_id or faker.uuid4(),
        "amount": amount,
        "type": "transfer",
        "recipientId": recipient_id or faker.uuid4()
    }
