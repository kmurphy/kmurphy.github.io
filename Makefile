message=default

default:
	osascript -e "tell application \"Firefox\" to activate"
	osascript -e 'tell application "System Events" to keystroke "r" using command down'

pub:
	cp -a /Users/kmurphy/mu_code/coderdojo_tramore/website_2/coderdojo_python/build/* . 
	git add .
	git status
	git commit -m "$(message)"
	git push origin master
	
view:
	open -a Firefox index.html
	
view-pub:
	open -a Firefox http://kmurphy.github.io/index.html
	
	
# session 3
#Hi Python coders, The plan for today's session (Saturday 25 Apr) is now online at kmurphy.github.io. Hope to see this this afternnon.