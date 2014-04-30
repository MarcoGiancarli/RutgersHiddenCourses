import requests

CS_URL = 'view-source:sis.rutgers.edu/soc/courses.json?semester=92014&campus=NB&level=U&subject=198'

courses = requests.get(CS_URL).json()
