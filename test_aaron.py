original_string = "aimar,library!Lord of the rings;2023-03-30:Harry Potter;2023-03-28"
name = "Lord of the rings"

# Find the index of the first occurrence of "ABC;" in the string
index = original_string.find(f"{name};")

# Find the index of the next colon (:) in the string, starting from the index of "ABC;"
next_colon_index = original_string.find(":", index)

# Remove the substring between the "ABC;" and the next colon (:)
new_string = original_string[:index] + original_string[next_colon_index+1:]

print(new_string) # "CBA!BCA;10,12,14"
with open("members.txt", "w") as file:
    file.write("aimar,library!\nrowan,library!\nben,library!\n")