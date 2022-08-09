import requests
from datetime import datetime

API_ID='1d591c4d'
API_KEY='1680767a0271442ec0eb1e518e1ab327'

s=input('Tell Me Which Exercise You Did: ')

end_point_url='https://trackapi.nutritionix.com/v2/natural/exercise'

query={
    'query':s,
    'gender':'male',
    'weight_kg':67.5,
    'height_cm':179,
    'age':22
}

HEADERS={
    'x-app-id':API_ID,
    'x-app-key':API_KEY
}

r=requests.post(end_point_url,headers=HEADERS,json=query)
res=r.json()
print(res)

sheet_end_point='https://api.sheety.co/b581f9da9351f0812c3fd26e34485634/workoutTracking/workouts'

today_date=datetime.now().strftime("%d/%m/%Y")
current_time=datetime.now().strftime('%X')


for exercise in res['exercises']:
    sheet_input={
        "workout":{
            'date':today_date,
            'time':current_time,
            'exercise':exercise['name'].title(),
            'duration':exercise['duration_min'],
            'calories':exercise['nf_calories']
        }
    }

    sheet_res=requests.post(sheet_end_point,json=sheet_input)
    print(sheet_res.text)
