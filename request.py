import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'gre':322, 'toefl':110, 'university_rating':3, 'statement_of_purpose':3.5, 'letter_of_recommendation':2.5, 'cgpa':8.67, 'research':1})

print(r.json())
