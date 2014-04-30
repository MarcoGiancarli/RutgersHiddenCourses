from pymongo import Connection

connection = Connection()
database = connection['rutgers_hidden_courses']
course_list = database['course_list']
subject_number = ''
course_number = ''
answer = ''

print 'Enter a command to list hidden courses. Enter "help" for a list of commands.'

while True:
    answer = raw_input()
    params = answer.split(' ')

    if params[0] == 'help':
        print 'Commands:'
        print 'subject <subject_number> --> Sets the subject to the given parameter.'
        print 'number <course_number>   --> Sets the course number to the given parameter.'
        print 'find                     --> Returns all courses with the current subject and course number.'
        print 'clear                    --> Clears the set subject and course numbers.'
    elif params[0] == 'subject':
        if len(params) != 2:
            print 'Usage: subject <subject_number>'
            continue
        subject_number = params[1]

    elif params[0] == 'number':
        if len(params) != 2:
            print 'Usage: number <course_number>'
            continue
        course_number = params[1]

    elif params[0] == 'find':
        if len(params) != 1:
            print 'Usage: find'
            continue
        filters = {}
        if subject_number:
            filters.update({'subject':subject_number})
        if course_number:
            filters.update({'number':course_number})
        query = course_list.find(filters)
        for section in query:
            print section['index']+'  '+section['number']+'  '+section['section']+'  '+section['title']
            for meeting in section['time_place']:
                print '    '+meeting['day']+'  '+meeting['start_time']+'-'+meeting['end_time']+' '+meeting['pm_code']+'M  '+meeting['campus']+'  '+meeting['building']+'-'+meeting['room']

    elif params[0] == 'clear':
        if len(params) != 1:
            print 'Usage: clear'
            continue
        subject_number = ''
        course_number = ''
    else:
        if params[0] == 'quit':
            exit(0)
        print 'Invalid command. Enter "help" for a list of commands.'
