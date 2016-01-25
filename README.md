#SublimeRSS
 Welcome to SublimeRSS! An RSS reader for Sublime! I created this because I really enjoy this feature in Emacs and found it to be non-existant in Sublime Text. Hope someone enjoys it as much as me!

##Dependencies:
This package requires the 'Clickable URLS' package. Get it through the package manager or from https://github.com/leonid-shevtsov/ClickableUrls_SublimeText

##Supported Systems
Seems to be working on everything so far.
Tested on Windows 10, Linux Mint 17, and Mac OSX 10.9.5 

##How-To:
First of all, make sure to add your own RSS feeds seperated by a comma. For example:
http://www.techcrunch.com/feed/,
http://rss.slashdot.org/Slashdot/slashdot,
http://www.reddit.com/r/funny/.rss

 You can access the `feedlist.txt` file via the command palette and typing rss and choosing SublimeRSS: Edit Feeds. Once you've added the feeds you can run SublimeRSS via the SublimeRSS: Run command, also found in the command palette. I've bound it to hotkey `'F8'` in my system by going to `Preferences>Key Bindings - User` and adding this code to the array:
```
"keys": ["f8"], 
"command": "rss" 
```
 For added convenience opening URLs 
 Add this to `Preferences>Package Settings>Clickable URLs>Key Bindings - User`
```
[
	{ 
		"keys": ["alt+;"], 
		"command": "open_url_under_cursor" 
	}
]
```
This will allow you, if your cursor is over the link, to open it by pressing `ALT+;` which for me is easier than the default binding of `CTRL+ALT+ENTER`

 And this to `Preferences>Package Settings>Clickable URLs>Mouse Bindings - User`
 ```
 [
	{ 
		"button": "button1", 
		"modifiers": ["option"], 
		"press_command": "open_url_under_cursor" 
	}
]
```
Additionally, this will allow you to open URLs by holding ALT (or Option) and left clicking the link which by default is not actually possible. (This hotkey binding came from user 'thespacedoctors' useful comment [here](https://github.com/leonid-shevtsov/ClickableUrls_SublimeText/issues/2))

##Donate

###Donate Bitcoin: 19Ve bRAu 8ZdT zf7A JnJv dCyh qSBZ qMon T

###Donate Dogecoin: DBGX4dwhD7SHhfcgzKjSZ2yJDhruAPgPUP

###Donate via Paypal: http://bit.ly/1klxN1M
