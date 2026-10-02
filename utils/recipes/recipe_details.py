from faker import Faker
from random import randint

fake = Faker('pt_BR')


def rand_ratio():
    return randint(840, 900), randint(473, 573)


# Function to generate a dictionary with recipe details
def make_recipe_details():

    height, width = rand_ratio()

    return {
        'id': fake.random_number(digits=2, fix_len=True),
        'title': fake.sentence(),
        'description': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'porções',
        'preparation_steps': fake.text(max_nb_chars=3000),
        'created_at': fake.date_time_this_year(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
            'url': f'https://picsum.photos/{width}/{height}'
        }
    }

if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe_details())