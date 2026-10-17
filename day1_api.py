import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

if response.status_code == 200:
    user = response.json()

    print("=" * 35)
    print("       USER INFORMATION")
    print("=" * 35)
    print(f"Name:    {user['name']}")
    print(f"Email:   {user['email']}")
    print(f"City:    {user['address']['city']}")
    print(f"Company: {user['company']['name']}")
    print("=" * 35)

else:
    print("Request failed. Status:", response.status_code)