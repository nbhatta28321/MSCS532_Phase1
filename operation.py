from autoCorrect import AutoCorrect

autocorrect = AutoCorrect()

with open('test.txt', 'r') as file:

    print('Initilizing ...')

    for line in file:
        autocorrect.insert(line.split()[0])

    print('Initilization Completed!')
    
word = input("Enter a word: ")

a = autocorrect.search(word)

print(a)
