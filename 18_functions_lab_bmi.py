#LAB
def bmi(weight, height):
    return weight / height ** 2


print(bmi(52.5, 1.65))

#backslash symbol will continue code in next line
def bmi2(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi2(352.5, 1.65))