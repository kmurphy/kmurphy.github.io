message=default

default:
	osascript -e "tell application \"Firefox\" to activate"
	osascript -e 'tell application "System Events" to keystroke "r" using command down'

pub:
	git add .
	git status
	git commit -m "$(message)"
	git push origin master
	
view:
	open -a Firefox index.html
	
view-pub:
	open -a Firefox http://kmurphy.github.io/index.html