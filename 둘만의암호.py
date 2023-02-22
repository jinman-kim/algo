import string


def solution(s, skip, index):
    result = ''
    alpha_dict = dict.fromkeys(string.ascii_lowercase, 0)
    for i in skip:
        del alpha_dict[i]
    cnt = 1
    new_dict = {}
    for key, value in alpha_dict.items():
        alpha_dict[key] = cnt
        new_dict[cnt] = key
        cnt += 1
    for i in s:

        if (alpha_dict[i] + index) % len(alpha_dict) == 0:
            result += new_dict[len(alpha_dict)]
        else:
            result += new_dict[(alpha_dict[i] + index) % len(alpha_dict)]
    return result