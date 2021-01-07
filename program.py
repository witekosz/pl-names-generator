from time import sleep

from src.generator import generate_people


print("Generating random names")

while True:
    input_number_names = input("Type number of names to generate: ")

    if input_number_names.isdigit() and int(input_number_names) > 0:
        number_names = int(input_number_names)
    else:
        print("Provide correct number!")
        break

    input_gender = input("Type gender(M for maskuline, F for feminine): ")

    if input_gender == 'M' or input_gender == 'F':
        gender_names = input_gender
    else:
        print("Provide correct gender")
        break

    break

print(f"Generating names: gender-> {input_gender}, {number_names} times")

sleep(1.5)

for e in (generate_people(number_names, input_gender)):
    print(e)
    sleep(0.1)
