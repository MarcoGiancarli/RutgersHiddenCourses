import requests

subjects = 'http://sis.rutgers.edu/soc/subjects.json?semester=92014&campus=NB&level=U'

subjects_list = requests.get(subjects).json()
subjectcodes = []

for subject in subjects_list:
	subjectcodes.append(int(subject['code']))

print subjectcodes
