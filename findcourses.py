import requests
import pymongo

BASE_URL = 'http://sis.rutgers.edu/soc/courses.json?semester=92014&campus=NB&level=U&subject='



for subject in subject_codes:
    subject_courses = requests.get(BASE_URL + str(subject)).json()

    for course in subject_courses:
        sections = course['sections']
        for section in sections:
            if section['printed'] == 'N':
                print section['index'] + "  --  " + course['title']
