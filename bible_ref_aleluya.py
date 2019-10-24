# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
import sublime, sublime_plugin

import urllib.request
import urllib.parse

class BibleRefAleluyaCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    print("Hallelujah")
    with urllib.request.urlopen('https://api1.bible.systems/John+3:16') as response_aleluya:
      html_aleluya = response_aleluya.read().decode('utf-8')
      self.view.insert(edit, 0, html_aleluya)
