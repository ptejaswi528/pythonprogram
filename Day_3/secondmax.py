def secondmax(li):
    if len(li) < 2:
        return None
    first = second = float('-inf')
    for num in li:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else None


li=[3,4,5,6,72,56]
print("second largest number",secondmax(li))

