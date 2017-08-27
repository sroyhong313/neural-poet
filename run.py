from subprocess import check_output
output = []
while True:
    command = ['python3', 'sample.py', '-n', '4000']
    raw_text = check_output(command)
    text = raw_text.decode('unicode_escape')
    poem = text.split('\n\n\n\n')
    if (len(poem) >= 3):
        poem = poem[1]
        break

output.append({'text': poem})
print(output)