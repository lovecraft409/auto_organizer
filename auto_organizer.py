from pathlib import Path
import shutil

folders = {
	".jpeg": "Images",
	".txt" : "Documents",
	".mp3" : "Music",
	".docx" : "Documents" 
}

def organize(folder_name):
	folder = Path(folder_name)

	for item in folder.iterdir():
		if not item.is_file():
			continue

		try:
			destination = folders[item.suffix]
		
		except KeyError:
			print(item.name, "Type of file is unknown bro --> Skipping")
		else:
			target = folder / destination
			target.mkdir(exist_ok=True)
			shutil.move(str(item), str(target / item.name))
			print(item.name, "Bro moved to", destination)

organize(Path.home() / "Downloads")