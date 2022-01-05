
with open('mad_libs.txt', 'r') as ml:
    ml2 = open('mad_libs2.txt', 'a')
    content = ml.read()
    i = 0
    while i < (len(content)):
        chunk = content[i:i+4]
        if chunk.lower() == 'noun':
            noun = input("Enter a noun: ")
            ml2.write(noun)
            i += 4
            continue
        if chunk.lower() == 'verb':
            verb = input("Enter a verb: ")
            ml2.write(verb)
            i += 4
            continue
        chunk = content[i:i+9]
        if chunk.lower() == 'adjective':
            adjective = input("Enter an adjective: ")
            ml2.write(adjective)
            i += 9
            continue
        else:
            ml2.write(content[i])
            i += 1
    ml2.write('\n')
    ml2.close()
