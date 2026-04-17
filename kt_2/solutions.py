# task 1
def create_profile(username, email, **rest):
    # print(username, email, rest, sep='\n')
    result = {
        "username": username,
        "email": email,
        **rest
    }
    return result

create_profile("admin", "admin@mail.com", role="superuser", is_active=True)

# task 2
get_status_text = lambda code: "Success" if code < 400 else "Error"

print(get_status_text(200)) # "Success"
print(get_status_text(201)) # "Success"
print(get_status_text(404)) # "Error"
print(get_status_text(500)) # "Error"

# if code < 400:
#     print()
# else:
#     print()

# task 3
def build_url(base, *route):
    # route = '/'.join(route)
    # return base + '/' + route
    return f"{base}/{'/'.join(route)}"

url_1 = build_url("https://mysite.com", "api", "v1", "users")
print(url_1) # "https://mysite.com/api/v1/users"

url_2 = build_url("http://localhost:8000", "media", "images", "logo.png")
print(url_2) # "http://localhost:8000/media/images/logo.png"

def validator(users):
    filtered = list(filter(lambda user: user['age'] >= 18 and user['is_active'], users))
    print(filtered)
    result = list(map(lambda user: f"User: {user['name']}, Age: {user['age']}", filtered))
    return result

users = [
    {'name': 'Artyom', 'age': 19, 'is_active': True},
    {'name': 'Polina', 'age': 17, 'is_active': True},
    {'name': 'Ivan', 'age': 22, 'is_active': False},
    {'name': 'Anna', 'age': 25, 'is_active': True}
]
print(validator(users))