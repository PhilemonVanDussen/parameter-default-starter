# PJ VanDussen
# 11/18/2024
# Default Values for Parameters Practice

# 8-3 (T-Shirt)
def make_shirt(shirt_size, shirt_message):
    print(f'The t-shirt size is {shirt_size} and it says {shirt_message}')
make_shirt('medium', 'Hi, Im fine')
make_shirt(shirt_size= 'large', shirt_message= 'Greeting human')




# 8-4 (Large Shirts)
def make_shirt(shirt_message, shirt_size = 'large'):
    print(f'The t-shirt size is {shirt_size} and it says {shirt_message}')
make_shirt('I love Python')

def make_shirt(shirt_size, shirt_message = 'I love Python'):
    print(f'The t-shirt size is {shirt_size} and it says {shirt_message}')
make_shirt('large')
make_shirt('medium')
make_shirt('small')



# 8-5 (Cities)
def describe_city(city_name, country_name = 'United States'):
    print(f'The city of {city_name} is in {country_name}')
describe_city('New York')
describe_city('Denver')

def describe_city(country_name, city_name = 'London'):
    print(f'The city of {city_name} is in {country_name}')
describe_city('England')