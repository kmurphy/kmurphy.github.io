message="default"

pib:
	git add .
	git status
	git commit -m $(message)
	git push origin master