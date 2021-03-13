from pathlib import Path

def split(file, diry):
	print("Splitting %s..." % diry)

	Path(diry).mkdir(exist_ok=True)

	text = file.read()
	text = text.split("\n-----\n")
	for entry in text:
		if entry == '': break

		entry = entry.split("\n", 1)
		print("Splitting entry for \"%s\"..." % entry[0].split(':')[1])

		with open("%s/%s:%s.txt" % (diry, entry[0].split(':')[0], entry[0].split(':')[1]), "w+") as f:
			if len(entry) == 2:
				f.write(entry[1])
			else:
				print("Ooops, entry \"%s\" doesn't have any text! (This is fine.)" % entry[0].split(':')[1])

def main():
	with open("object_help.txt", "r") as f:
		split(f, 'object_help')

	with open("item_help.txt", "r") as f:
		split(f, 'item_help')

if __name__ == "__main__":
	main()