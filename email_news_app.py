import sys
sys.stdout.reconfigure(encoding='utf-8')

from send_email import send_email
import requests

topic = "technology, business"
url = (
"https://newsdata.io/api/1/latest?"
"apikey=pub_ab9a3133cb864b98a711ca502e125633"
f"&q={topic}"
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
body = " "
for result in data["results"][0:10]:
    if result["title"] is not None:
        body = "subject: TODAYS BREAKING NEWS" + "\n" + body + result["title"] + "\n" \
            + result["description"] + "\n" \
            + result["link"] + 2*"\n"

body = body.encode('utf-8')
send_email(message=body)

