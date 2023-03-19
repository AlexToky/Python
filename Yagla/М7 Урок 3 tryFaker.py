from faker import Faker

fake = Faker()

newName = fake.address()

print(newName + " - Result")