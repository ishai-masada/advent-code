# Import data from the text file
with open("data.txt", 'r') as f:
    data = f.read().splitlines()

# Number of pairs that overlap in any way
overlaped_pairs = 0

for pair in data:
    elf_pair = pair.split(",")
    elf_1, elf_2 = elf_pair[0].split("-"), elf_pair[1].split("-")
    section_1 = int(elf_1[0])
    section_2 = int(elf_1[1])
    section_3 = int(elf_2[0])
    section_4 = int(elf_2[1])
    
    if ((section_1 < section_3) and (section_2 < section_3)) or ((section_1 > section_4) and (section_2 > section_4)):
        continue

    overlaped_pairs += 1

print(overlaped_pairs)
