import requests
from pymongo import Connection

connection = Connection()
connection.drop_database('rutgers_hidden_courses')
database = connection['rutgers_hidden_courses']
course_list = database['course_list']

SUBJECTS_URL = 'http://sis.rutgers.edu/soc/subjects.json?semester=12015&campus=NB&level=U'

subjects_list = requests.get(SUBJECTS_URL).json()
subject_codes = []

for subject in subjects_list:
	subject_codes.append(int(subject['code']))

BASE_URL = 'http://sis.rutgers.edu/soc/courses.json?semester=12015&campus=NB&level=U&subject='

for subject in subject_codes:
    subject_courses = requests.get(BASE_URL + str(subject)).json()

    for course in subject_courses:
        sections = course['sections']
        for section in sections:
            if section['printed'] == 'N':
                time_place = []
                for meeting in section['meetingTimes']:
                    time_place.append({'start_time':meeting['startTime'],
                                       'end_time'  :meeting['endTime'],
                                       'pm_code'   :meeting['pmCode'],
                                       'campus'    :meeting['campusAbbrev'],
                                       'building'  :meeting['buildingCode'],
                                       'room'      :meeting['roomNumber'],
                                       'day'       :meeting['meetingDay']})

                course_list.insert({'index'     :section['index'],
                                    'section'   :section['number'],
                                    'title'     :course['title'],
                                    'subject'   :course['subject'],
                                    'number'    :course['courseNumber'],
                                    'time_place':time_place})

                print section['index'] + '  ' + course['title']
