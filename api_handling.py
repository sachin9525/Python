import requests


# ==========================================
# 1. Basic GET Request
# ==========================================

print("1. Basic GET Request")

url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

response = requests.get(url)

print("Status Code:", response.status_code)


# ==========================================
# 2. Check Request Status
# ==========================================

print("\n2. Checking API Response")

if response.status_code == 200:
    print("API request successful")
else:
    print("API request failed")


# ==========================================
# 3. Convert Response to JSON
# ==========================================

print("\n3. JSON Response")

data = response.json()

print(data)


# ==========================================
# 4. Access Data from JSON
# ==========================================

print("\n4. Accessing JSON Data")

if response.status_code == 200:

    user = data.get("data", {})

    print("First Name:", user.get("name", {}).get("first"))
    print("Last Name:", user.get("name", {}).get("last"))
    print("Email:", user.get("email"))


# ==========================================
# 5. Create Reusable API Function
# ==========================================

print("\n5. API Function")


def fetch_random_user():

    api_url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

    try:

        api_response = requests.get(api_url, timeout=10)

        api_response.raise_for_status()

        result = api_response.json()

        return result

    except requests.exceptions.RequestException as error:

        print("Request Error:", error)

        return None


result = fetch_random_user()

if result:
    print("Data fetched successfully")


# ==========================================
# 6. GET API with Query Parameters
# ==========================================

print("\n6. API With Query Parameters")

url = "https://api.freeapi.app/api/v1/public/randomusers"

params = {
    "page": 1,
    "limit": 5
}

try:

    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    print("Status Code:", response.status_code)

except requests.exceptions.RequestException as error:

    print("Error:", error)


# ==========================================
# 7. Common HTTP Status Codes
# ==========================================

print("\n7. Common HTTP Status Codes")

status_codes = {
    200: "OK",
    201: "Created",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    500: "Internal Server Error"
}

for code, message in status_codes.items():
    print(code, "-", message)


# ==========================================
# 8. Error Handling
# ==========================================

print("\n8. Error Handling")

try:

    response = requests.get(
        "https://api.freeapi.app/api/v1/public/randomusers/user/random",
        timeout=10
    )

    response.raise_for_status()

    print("Request successful")

except requests.exceptions.Timeout:

    print("Request timed out")

except requests.exceptions.ConnectionError:

    print("Connection error")

except requests.exceptions.HTTPError as error:

    print("HTTP Error:", error)

except requests.exceptions.RequestException as error:

    print("Request Error:", error)


# ==========================================
# 9. Response Headers
# ==========================================

print("\n9. Response Headers")

try:

    response = requests.get(
        "https://api.freeapi.app/api/v1/public/randomusers/user/random",
        timeout=10
    )

    print("Content Type:", response.headers.get("Content-Type"))

except requests.exceptions.RequestException as error:

    print("Error:", error)


# ==========================================
# 10. Final Example
# ==========================================

print("\n10. Random User Details")


def get_random_user():

    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

    try:

        response = requests.get(url, timeout=10)

        response.raise_for_status()

        data = response.json()

        user = data.get("data", {})

        name = user.get("name", {})

        print(
            "Name:",
            name.get("first"),
            name.get("last")
        )

        print("Email:", user.get("email"))
        print("Gender:", user.get("gender"))

    except requests.exceptions.RequestException as error:

        print("API Error:", error)


get_random_user()


print("\n" + "=" * 45)
print("API HANDLING PRACTICE COMPLETED")
print("=" * 45)