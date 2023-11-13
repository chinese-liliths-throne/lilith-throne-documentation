import re
import json

from pathlib import Path

LOCALE_DIR = "./docs/locale"
RESULT_DIR = "./dict"

def extract():

	locale_path = Path(LOCALE_DIR)
	result_path = Path(RESULT_DIR)

	dic = {}

	for file in locale_path.glob("**/*.po"):
		with open(file, mode="r", encoding="utf-8") as f:
			lines = f.readlines()
			results = []
			results_dicts = []
			temp = []
			ori = False
			for line in lines:
				if "msgid" in line:
					ori = True
				elif "msgstr" in line:
					ori = False
					if len(temp) > 0:
						results.append("\n".join(temp))
					temp = []
				if ori:
					matches = re.findall(r"\"(.*)\"", line)
					if len(matches) > 0:
						match = matches[0]
					else:
						continue
					if match != "":
						temp.append(match)
			for i, original in enumerate(results):
				d = {
					"key" : str(i),
					"original" : original,
					"translation" : ""
				}
				results_dicts.append(d)
			
			if len(results) > 0:
				dic[file.with_suffix("").name] = results_dicts
	
	if not result_path.exists():
		result_path.mkdir(parents=True)
	
	for file, content in dic.items():
		with open(result_path/(file + ".json"), mode="w", encoding="utf-8") as f:
			json.dump(content, f)


def apply():
	pass


if __name__ == "__main__":
	extract()