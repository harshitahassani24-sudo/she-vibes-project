import requests

# The API endpoint — a free public GitHub user lookup
url = "https://api.github.com/users/torvalds"

# Send the request
response = requests.get(url)

# Convert the response into a Python dictionary
data = response.json()

# Pull out the pieces we care about
name = data["name"]
location = data["location"]
company = data["company"]
followers = data["followers"]

# Print them
print(f"Name: {name}")
print(f"Location: {location}")
print(f"Company: {company}")
print(f"Followers: {followers}")