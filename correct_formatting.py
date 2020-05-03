inputFile = open('embeddings.txt', 'r') 
exportFile = open('correct_embeddings.txt', 'w')
for line in inputFile:
   new_line = line.replace('  ', ' ')
   exportFile.write(new_line) 

inputFile.close()
exportFile.close()