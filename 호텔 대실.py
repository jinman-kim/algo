def solution(book_time):
    convert_time = []
    for i in book_time:
        a = i[0].split(':')
        b = i[1].split(':')
        c = int(a[0])*60 + int(a[1])
        d = int(b[0])*60 + int(b[1]) + 10
        convert_time.append([c,d])
    convert_time.sort(key=lambda x:x[1])
    room = 1
    q = convert_time.pop(0)
    convert_time.sort(key=lambda x:x[0])
    tmp = q[1]
    for i in convert_time[:]:
        if tmp <= i[0]:
            tmp = i[1]
            convert_time.remove(i)
    while convert_time:
        room += 1
        q = convert_time.pop(0)
        tmp = q[1]
        for i in convert_time[:]:
            if tmp <= i[0]:
                tmp = i[1]
                convert_time.remove(i)
    return room


book_time = [["15:00", "17:00"], ["17:10", "18:10"], ["14:20", "14:30"], ["14:10", "19:20"], ["18:20", "21:20"]]
print(solution(book_time))