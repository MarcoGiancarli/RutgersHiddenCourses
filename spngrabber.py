import requests

SUBJECTS_URL = 'http://sis.rutgers.edu/soc/subjects.json?semester=92014&campus=NB&level=U'

subjects_list = requests.get(SUBJECTS_URL).json()
subject_codes = []

for subject in subjects_list:
	subject_codes.append(int(subject['code']))

BASE_URL = 'http://sis.rutgers.edu/soc/courses.json?semester=92014&campus=NB&level=U&subject='

for subject in subject_codes:
    subject_courses = requests.get(BASE_URL + str(subject)).json()

    for course in subject_courses:
        sections = course['sections']
        for section in sections:
            if section['specialPermissionAddCode'] is not None:
                print section['index'] + '  ' + course['courseNumber'] + '  ' + course['title'] + '  ' + section['specialPermissionAddCode']
