def add_length(str_):
    return [word + " " + str(len(word)) for word in str_.split()]

print(add_length("apple ban"))

print(add_length("you will win"))


def get_size(w, h, d):
    surface_area = 2 * (w * h + h * d + w * d)
    volume = w * h * d
    return [surface_area, volume]

def swap_values(args):
    temp = args[0]
    args[0] = args[1]
    args[1] = temp

def merge_arrays(arr1, arr2):
    return sorted(set(arr1 + arr2))
