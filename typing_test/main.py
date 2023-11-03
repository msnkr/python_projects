import keyboard
import faker

# Display a list of random words
# Get user input
# compare the two
# Find a way to calculate words per minute

fake = faker.Faker()
word_lst = " ".join([fake.word().lower() for _ in range(20)])

print(word_lst)