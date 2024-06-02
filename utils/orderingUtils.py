import re;

__MININDEX: int = 1;

__numberOnlyRegex:   re.Pattern = re.compile(r"\D");
__inputCleanerRegex: re.Pattern = re.compile(r"[^0-9\-,]");

# 2-5,9,12-16

def isGoodRange(MAXINDEX: int, selection: str) -> bool:
	numOnly:   str = re.sub(__numberOnlyRegex, ' ', selection);
	strNumSet: set = set(numOnly.split(' '));

	strNumSet.discard(' ');			# rid of any leftover spaces
	strNumSet.discard('');

	intNumSet: set = set(map(int, strNumSet));

	if (__MININDEX > min(intNumSet)):
		print("The minimum value entered is below the minimum index (1)");
		return False;

	if (max(intNumSet) > MAXINDEX):
		print(f"The maximum value entered is more than the number of videos ({MAXINDEX}) in the playlist");
		return False;

	return True;


def getSelectedIndices(selection: str) -> set:
	if (selection == ''):
		return None;

	# > 2-6,9,12-16 and may not be necessarilly ordered'''
	cleanedSl: str = re.sub(__inputCleanerRegex, '', selection);
	ranges: list = cleanedSl.split(',');

	indices: set = set();

	for part in ranges:
		if ('-' in part):  # it is a range statement
			start, end = map(int, part.split('-'));
			indices.update(range(start, end + 1));
		else:
			indices.add(int(part));

	return indices;