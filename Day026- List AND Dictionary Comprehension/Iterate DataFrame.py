student_dict={
    "student":["James","john","lily"],
    "score":[56,76,67]
}

# loop through dictionaries
# for (key,value) in student_dict.items():
#     print(key,value)

import pandas
student_data_frame=pandas.DataFrame(student_dict)
# print(student_data_frame)

# loop through DataFrame
# for (key,value) in student_data_frame.items():
#     print(value)

# loop through rows of a DataFrame
for (index,row) in student_data_frame.iterrows():
    # print(row.student)
    if row.student=='lily':
        print(row.score)