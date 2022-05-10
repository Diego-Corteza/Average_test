def find_average(values) -> float:
    result = 0
    for v in values:
        result += v
    return result / len(values)


print("Oi m8, your average is: ", find_average([5, 6, 7, 8]))
print("hey dude,this code looks weird")
