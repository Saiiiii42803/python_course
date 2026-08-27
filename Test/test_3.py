info = {"alice":90, "fred":80, "mike": 100, "alex": 60, "doug": 70}
print("name and scores:", info)
total = 0
avv = 0
scores = info.values()
for i in info.values():
    total += i
print("class avverage:", total/5)
print("Best score:", max(scores))
print("worst score:", min(scores))



search = input("Look up a specific student:" )
print("Search results:", "Score -", info.get(search))