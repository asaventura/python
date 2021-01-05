with open('lessons.txt') as lessons:
    schedule = {}
    for line in lessons.readlines():
        lesson = line.split(':')
        sum_time = 0
        it = iter(lesson[1].split())
        for time in lesson[1].split():
            if time.split('(')[0] == '-':
                next(it)
            else:
                sum_time += int(time.split('(')[0])
        schedule.update({lesson[0]: sum_time})
    print(schedule)
