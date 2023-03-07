def solution(sequence):
    answer = 0
    p_pulse = [sequence[i]*(-1)**(i%2) for i in range(len(sequence))]
    m_pulse = [sequence[i]*(-1)**(i+1%2) for i in range(len(sequence))]
    tmp,max_tmp = 0,0
    for i in p_pulse:
        tmp += i
        if tmp < 0:
            tmp = 0
        max_tmp = max(tmp,max_tmp)
    tmp = 0
    for i in m_pulse:
        tmp += i
        if tmp < 0:
            tmp = 0
        max_tmp = max(tmp,max_tmp)
    return max_tmp