from pathlib import Path
from natsort import natsorted

def combine(diry):
	print("Combining %s..." % diry)

	Path('out').mkdir(exist_ok=True)
	with open("out/%s.txt" % diry, "w+") as f:
		pathlist = Path(diry).glob('*.txt')

		# This is all for making the entries be ordered by ID.
		filelist = []
		for path in pathlist:
			filelist.append(path.stem)
		filelist = natsorted(filelist, reverse=False)

		for file in filelist:
			f.write(file + "\n")
			with open("%s/%s.txt" % (diry, file), "r") as f2:
				f.write(f2.read().rstrip())
			f.write("\n-----\n")

def main():
	combine('object_help')
	combine('item_help')

if __name__ == "__main__":
	main()
