with open('myfile.txt', 'w') as file:
    file.write("Hello file world!")
with open('myfile.txt', 'a') as file:
    file.write("\nNew line added to the file.")