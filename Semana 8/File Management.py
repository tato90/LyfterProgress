#File Management

origin_file = 'my_songs.txt'
destination_file = 'new_file.txt'

with open(origin_file, 'r') as file:
    lines = file.readlines()
sorted_lines = sorted(line.strip() for line in lines)
with open(destination_file, 'w') as file:
    for line in sorted_lines:
        file.write(line + '\n')

print(f'Lines from {origin_file} have been sorted and saved to {destination_file}.')
for line in sorted_lines:
        print(line)
