from autoCorrect import AutoCorrect

autocorrect = AutoCorrect()

autocorrect.insert("apple")
autocorrect.insert("app")
autocorrect.insert("acid")
autocorrect.insert("aerospace")
autocorrect.insert("acceptance")

word = input("Enter a word: ")

a = autocorrect.search(word)

print(a)