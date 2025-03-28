def check_exam(arr1, arr2):
    score = 0
    for correct, answer in zip(arr1, arr2):
        if answer == correct:
            score += 1  
        elif answer == "":
            continue  
        else:
            score -= 0.5  
    return max(score, 0)  



def remove(s):
    return s.replace(" ", "")


def get_real_floor(n):
    if n > 0:
        return n - 1
    elif n == 0:
        return 0 
        return n
