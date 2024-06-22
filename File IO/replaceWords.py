def find_and_replace(file, search, replace):
	with open(file) as page:
		data = page.read()
		new_text = data.split()
		for index, word in enumerate(new_text):
			if word == search:
				new_text.remove(word)
				new_text.insert(index, replace)
		realtext = " ".join(new_text)

	with open(file, "w") as finally44:
		finally44.write(realtext)


find_and_replace("story.txt", "runner", "WATERMELONNNN")