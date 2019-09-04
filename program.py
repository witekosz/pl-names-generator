from generator import generate_people


print("Hello! Generate random polish names")

while 1==1:

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

print(str(input_number_names), input_gender)

print(f"Generating names: gender->{input_gender}, {number_names} times")

print(generate_people(number_names, input_gender))