import requests
url = (
"https://newsdata.io/api/1/latest?"
"apikey=pub_ab9a3133cb864b98a711ca502e125633"
"&q=technology and business"
"&country=in,us"
"&language=en"
"&category=breaking,science,technology"
"&removeduplicate=1"
"&sort=relevancy"
)
response = requests.get(url)
data = response.json()
print(data["results"])

# Print titles and descriptions of the news articles
for result in data["results"]:
    print(result["title"])
    print(result["description"])

