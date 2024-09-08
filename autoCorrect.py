class AutoCorrect:
    def __init__(self, words) -> None:
        self.words = words
        
    def search(self, input) -> list[str]:
        # print("words",words)
        s = [w for w in self.words if w.startswith(input)]
        if s:
            return s
        # for i in self.words:
        #     if (i.startswith(input)):
        #         return list[i]
        return list["Empty"]


words = ["apple", "app", "acid", "aerospace"]
autocorrect = AutoCorrect(words)
a = autocorrect.search("ap")
print("Final", a)