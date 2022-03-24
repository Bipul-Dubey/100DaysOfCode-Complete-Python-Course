# new_dict={new_key:new_value for item in list} # create dict using list values
# new_dict={new_key:new_value for (key,value) in dict.item()} # create dict using dict

# conditional dict comprehension

# new_dict={new_key:new_value for (key,value) in dict.items() if test}

import random
names=['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
dict={student:random.randint(10,20) for student in names}
stud={'Alex': 11, 'Beth': 19, 'Caroline': 13, 'Dave': 17, 'Eleanor': 17, 'Freddie': 17}
passed_student={student:score for (student,score) in stud.items() if score>15}
print(passed_student)
