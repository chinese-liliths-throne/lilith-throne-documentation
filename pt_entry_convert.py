import re
import json
import shutil
import os
import zipfile
import subprocess

from pathlib import Path
from urllib import request

PARATRANZ_API_BASE_URL = "https://paratranz.cn/api"
PARATRANZ_PROJECT_ID = "8683"
PARATRANZ_API_URL = PARATRANZ_API_BASE_URL + "/projects/" + PARATRANZ_PROJECT_ID

DOWNLOAD_DIR = "./downloads"
ROOT_DIR = "./"
DICT_DIR = "./dict"

LOCALE_DIR = "./docs/locale"
RESULT_DIR = "./dict"
TARGET_DIR = "./docs/locale/zh/LC_MESSAGES"

def fetch_latest_dict(paratranz_access_token: str) -> None:
	output_url = PARATRANZ_API_URL + "/artifacts"  # use post
	download_url = PARATRANZ_API_URL + "/artifacts/download"

	path = Path(DOWNLOAD_DIR)

	if not path.exists():
		path.mkdir()

	file_path = path / f"dict-latest.zip"
	if file_path.exists():
		os.remove(file_path)

	opener = request.build_opener()
	opener.addheaders = [('Authorization', paratranz_access_token)]
	request.install_opener(opener)

	request.urlretrieve(download_url, file_path)

def unzip_latest_dict() -> None:
	zip_path = Path(DOWNLOAD_DIR) / f"dict-latest.zip"
	extract_path = Path(ROOT_DIR)
	old_dict_dir = Path(DICT_DIR)

	with zipfile.ZipFile(zip_path, "r") as zip_ref:
		zip_ref.extractall(extract_path)

	if old_dict_dir.exists():
		shutil.rmtree(old_dict_dir)

	shutil.move(extract_path / "utf8", old_dict_dir)
	shutil.rmtree(extract_path / "raw", ignore_errors=True)

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
	dict_path = Path(DICT_DIR)
	target_path = Path(TARGET_DIR)

	pt_token = (
		""
		if os.environ.get("PARATRANZ_TOKEN") is None
		else os.environ.get("PARATRANZ_TOKEN")
	)

	if pt_token == "":
		pt_token = input(
			"请输入Paratranz的Acccess Token，\t或选择设置环境变量“PARATRANZ_TOKEN”/在main.py文件夹中修改--pt-token的default值："
		)
	fetch_latest_dict(pt_token)
	unzip_latest_dict()

	dic = {}

	for file in dict_path.iterdir():
		target_file = target_path / (file.with_suffix("").name + ".po")
		with open(file, mode="r", encoding="utf-8") as f:
			dic[target_file] = json.load(f)
	
	for file, content in dic.items():
		with open(file, mode="r", encoding="utf-8") as f:
			lines = f.readlines()
		
		idx = 0
		temp = []
		new_lines = []
		ori = False


		for line in lines:
			if "msgid" in line:
				ori = True
			elif "msgstr" in line:
				ori = False
				if len(temp) > 0 and "\n".join(temp) == content[idx]['original'].replace('\\n','\n'):
					if content[idx]['stage'] != 0:
						line = line.replace("\"\"", '"' + content[idx]['translation'].replace('\\n','') + '"')
					idx += 1
				temp = []
			if ori:
				matches = re.findall(r"\"(.*)\"", line)
				if len(matches) > 0:
					match = matches[0]
					if match != "":
						temp.append(match)
			new_lines.append(line)
		with open(file, mode="w", encoding="utf-8") as f:
			f.writelines(new_lines)

if __name__ == "__main__":
	# extract()
	apply()