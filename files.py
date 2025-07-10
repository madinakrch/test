# with open('text.txt', 'r') as f:
#     for s in f:
#         print(s.strip())
#
#
# with open('text.txt', 'r') as f:
#     lines = f.readlines()
#     print(lines)
#
#
# with open('output.txt', 'w') as foo:
#     foo.write('Obi-Wan')
#
#
# with open('output.txt', 'a+') as foo:
#     foo.write('Viktor Osimhen')
#
# with open('text.txt', 'r') as input_file, open('output.txt', 'a+') as output_file:
#     inp = input_file.readlines()
#     for i in inp:
#         output_file.write(i.strip())


with open('text.txt', 'r') as input_file, open('output.txt', 'w+') as output_file:
    lines = input_file.readlines()
    lines.reverse()
    for l in lines:
        if ',' not in l:
            ind = lines.index(l)
            newLines = [*lines[len(lines): ind: -1],  l, '*' * 12 + '\n', *lines[:ind]]
            output_file.write(''.join(newLines))
            break
    else:
        output_file.write(''.join(lines) + '*' * 12 + '\n')

