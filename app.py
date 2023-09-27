# import requests
# from flask import Flask

# app = Flask(__name__)

# export FLASK_APP=app.py


# API_KEY = "71f325c630ec40aa86d7faae7ab1c982"
# METHOD = "foods.search"

# response = requests.get(
#     "https://platform.fatsecret.com/rest/server.api",
#     params={"method": METHOD, 
#             "search_expression": "cake"},
#     headers={"Authorization": f"Bearer {API_KEY}"},
# )

# # Parse the JSON response
# json_data = response.json()

# # Print the JSON data
# print(json_data)

from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def route():
    # Define your API key (should not be hard-coded in production)
    API_KEY = "1af83c33908b455da0ea7b26007d7b86"

    # Specify the API method you want to use
    METHOD = "foods.search"

    # Set your search expression
    search_expression = "cake"

    # Set other optional parameters
    page_number = 0  # Zero-based offset into the results
    max_results = 20  # Maximum number of results to return (cannot be greater than 50)
    format_type = "json"  # The desired response format ("xml" or "json")

    # Make a request to the FatSecret API to search for food items
    response = requests.get(
        "https://platform.fatsecret.com/rest/server.api",
        params={
            "method": METHOD,
            "search_expression": search_expression,
            "page_number": page_number,
            "max_results": max_results,
            "format": format_type,
        },
        headers={"Authorization": f'Bearer {API_KEY}'}
        
    )
    

    # 'scope' : 'basic'
    # Check if the request was successful
    if response.status_code == 200:
        if format_type == "json":
            # Parse the JSON response
            json_data = response.json()
            return jsonify(json_data)
        else:
            return f"Request failed with status code: {response.status_code}"
    else:
        return f"Request failed with status code: {response.status_code}"

if __name__ == "__main__":
    app.run(debug=True)








