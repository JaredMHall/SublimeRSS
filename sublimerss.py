import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__))+"/feedparser")
import sublime, sublime_plugin
import feedparser 
import datetime

class RssCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.getFeed(edit)

    def parseFeedList(self):
        feedList = []
        filestream = open(os.path.abspath(os.path.dirname(__file__)) + "/feedlist.txt", "r")
        feedList = filestream.read().split(',') 
        feedList = (j.strip(' ') for j in feedList)
        feedList = (j.strip('\n') for j in feedList)
        return feedList

    def getFeed(self,edit):
        window = sublime.active_window()
        entries = {}
        feed = self.parseFeedList()
        posts = []

        for x, link in enumerate(feed):
            parsedFeed = feedparser.parse(link)
            for post in parsedFeed.entries:
                posts.append(post.link)
                posts.append(post.title)

        now = datetime.datetime.now()
        newFile = window.new_file()
        newFile.set_name("SRSSfeeds.srss")
        newFile.set_syntax_file("Packages/" + os.path.basename(os.path.dirname(__file__)) + "/SublimeRSS.tmLanguage")
        newFile.set_scratch(True)

        for x, entry in enumerate(posts):
            if (x%2==0):
                newFile.insert(edit, 0, str(entry))
                newFile.insert(edit, 0, "\n")
            else:
                newFile.insert(edit, 0, str("# " + entry))
                newFile.insert(edit, 0, "\n")

        asciiLogo = """
   _____       _     _ _                _____   _____ _____ 
  / ____|     | |   | (_)              |  __ \ / ____/ ____|
 | (___  _   _| |__ | |_ _ __ ___   ___| |__) | (___| (___  
  \___ \| | | | '_ \| | | '_ ` _ \ / _ \  _  / \___ \\\\___ \ 
  ____) | |_| | |_) | | | | | | | |  __/ | \ \ ____) |___) |
 |_____/ \__,_|_.__/|_|_|_| |_| |_|\___|_|  \_\_____/_____/ 
        """
        newFile.insert(edit, 0, "\n")
        newFile.insert(edit, 0, str(now.strftime("%Y-%m-%d %H:%M")))
        newFile.insert(edit, 0, "\n")
        newFile.insert(edit, 0, asciiLogo)


class EditFeedsCommand(sublime_plugin.TextCommand):
    window = sublime.active_window()

    def run(self, edit):
        self.openFeedList()

    def openFeedList(self):
        self.window.open_file(os.path.abspath(os.path.dirname(__file__)) + "/feedlist.txt",)
