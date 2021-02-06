message=default

default:
	osascript -e "tell application \"Firefox\" to activate"
	osascript -e 'tell application "System Events" to keystroke "r" using command down'


pub:
	#make -C /Users/kmurphy/mu_code/coderdojo_tramore/website_2 pub
	cp -a /Users/kmurphy/mu_code/coderdojo_tramore/website_2/public/* . 
	git add .
	git status
	git commit -m "$(message)"
	git push origin master
	
view:
	open -a Firefox index.html
	
view-pub:
	open -a Firefox http://kmurphy.github.io/index.html
	

# set -gx FLASK_APP coderdojo_python/app.py
# set -gx FLASK_ENV development
# flask run

# session 3
#Hi Python coders, The plan for today's session (Saturday 25 Apr) is now online at kmurphy.github.io. Hope to see this this afternnon.