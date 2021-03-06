import sublime, sublime_plugin

import datetime

import os

class CreateDailyNoteCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        note_title = datetime.datetime.now().strftime("%Y-%m-%d") + '.note'

        # if os.path.isfile(note_title):
        #     return

        note_path = os.environ['HOME'] + '/Dropbox/Documents/notes/' + note_title
        note_path = os.environ['HOME'] + '/Dropbox/Documents/VSCO/' + note_title

        print("CreateDailyNoteCommand  " + str(note_path))
        self.view.window().open_file(note_path)
