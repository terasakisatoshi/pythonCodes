from janome.tokenizer import Tokenizer 

t=Tokenizer()
tokens=t.tokenize("Hello World きょうはいい天気ですね。")
for tok in tokens:
    print(tok)

print(tok.part_of_speach)