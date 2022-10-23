pets = ['pes', 'kočka', 'křeček', 'had', 'morče', 'králík', 'andulka']

list_of_pairs = []
for animal in pets:
    pair = (animal[1:], animal)
    list_of_pairs.append(pair)
list_of_pairs.sort()

final_list = []
for k, h in list_of_pairs:
    final_list.append(h)
print(final_list)
