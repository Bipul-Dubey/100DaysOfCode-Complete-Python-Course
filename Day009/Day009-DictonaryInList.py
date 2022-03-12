travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
def add_new_country(country_visited,visits_num,cities_visited):
    new_country={}
    new_country["country"]=country_visited
    new_country["visits"]=visits_num
    new_country["cities_visited"]=cities_visited
    travel_log.append(new_country)
#to be added to the travel_log. 👇
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
