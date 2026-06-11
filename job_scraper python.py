import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)

print(response.status_code)


import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("div", class_="card-content")

titles = []
companies = []
locations = []
links = []

for job in jobs:

    title = job.find("h2", class_="title").text.strip()

    company = job.find("h3", class_="company").text.strip()

    location = job.find("p", class_="location").text.strip()

    link = job.find_all("a")[1]["href"]

    titles.append(title)

    companies.append(company)

    locations.append(location)

    links.append(link)

df = pd.DataFrame({
    "Job Title": titles,
    "Company": companies,
    "Location": locations,
    "Application Link": links
})

print(df)


df.to_excel("jobs_data_cleaned.xlsx", index=False)

print("Excel file created successfully")

print("Total Jobs Scraped:", len(df))
print("Unique Companies:", df["Company"].nunique())

print(df["Location"].value_counts().head(1))

df["Location"] = df["Location"].str.replace("\n", " ")

df["Location"] = df["Location"].str.strip()

print(df["Location"].head())

df["Remote"] = df["Location"].apply(
    lambda x: "Yes" if "Remote" in x else "No"
)


print(df[["Location", "Remote"]].head())
df["Job ID"] = range(1, len(df) + 1)

df = df[[
    "Job ID",
    "Job Title",
    "Company",
    "Location",
    "Remote",
    "Application Link"
]]


print(df.head())

top_companies = df["Company"].value_counts().head(10)

print(top_companies)

top_jobs = df["Job Title"].value_counts().head(10)

print(top_jobs)

remote_counts = df["Remote"].value_counts()

print(remote_counts)


summary = pd.DataFrame({
    "Metric": [
        "Total Jobs",
        "Unique Companies",
        "Remote Jobs"
    ],
    "Value": [
        len(df),
        df["Company"].nunique(),
        (df["Remote"] == "Yes").sum()
    ]
})

print(summary)

summary.to_excel("summary_metrics.xlsx", index=False)

