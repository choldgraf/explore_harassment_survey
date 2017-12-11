from download import download
import pandas as pd
import string

# This is the URL of the survey results
url = "https://docs.google.com/spreadsheets/d/1S9KShDLvU7C-KkgEevYTHXr3F6InTenrBsS9yk-8C5M/export?format=csv"

# Download the data
path = download(url, './data/raw.csv', replace=True)

# Rename columns
data = pd.read_csv(path)
rename = {"(Optional) What Was The Name of the Institution(s)": "institution",
          "Your Field/Discipline": "field",
          "What Was Your Status When the Incident(s) Happened?": "position",
          "What Was the Status of the Perpetrator(s) (Particularly, relative to you)?": "position_perp",
          "What Type of Institution Was It?": "institution_type",
          "What Was the Gender of the Harasser?": "gender_harasser",
          "What Happened and When? (Feel free to include incidents that happened to you or to others close to you in your program/department/campus/lab/disciplinary group)": "description",
          "The Impact of the Harassment on Your Life Choices/Trajectory": "impact_trajectory",
          "The Impact of the Harassment on Your Mental Health": "impact_mental_health",
          "The Impact of the Harassment on Your Career": "impact_career",
          "Institutional Responses to the Harassment (If Any)": "institute_response",
          "Institutional/Career Consequences for the Harasser (If Any)": "consequences_harasser"
}
data = data.rename(columns=rename)
data = data[list(rename.values())]

# Clean up text
for col in data.columns:
    data[col] = data[col].str.lower().str.strip(string.punctuation + ' ')
data = data.replace('N/A', 'NaN')

data.to_csv('./data/clean.csv')