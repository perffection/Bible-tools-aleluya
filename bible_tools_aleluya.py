# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
#Thanks Jesus for bible-api.com
#{"reference":"John 3:16","verses":[{"book_id":"JHN","book_name":"John","chapter":3,"verse":16,"text":"\nFor God so loved the world, that he gave his one and only Son, that whoever believes in him should not perish, but have eternal life.\n\n"}],"text":"\nFor God so loved the world, that he gave his one and only Son, that whoever believes in him should not perish, but have eternal life.\n\n","translation_id":"web","translation_name":"World English Bible","translation_note":"Public Domain"}
import sublime, sublime_plugin
import json
import urllib.request
import urllib.parse
import time
import re
class BibleToolsAleluya:
  """Hallelujah, shared across all classes"""

  @staticmethod
  def debug_aleluya(str_aleluya):
    print("BibleToolsAleluya: " + time.ctime() + " - " + str_aleluya )

  @staticmethod
  def reftostr_aleluya(obj_aleluya):
    book_name_before_every_verse_aleluya = sublime.load_settings("BibleToolsAleluya.sublime-settings").get("book_name_before_every_verse_aleluya")

    strings_aleluya = "" if book_name_before_every_verse_aleluya else obj_aleluya["verses"][0]["book_name"]+" "
    strings_aleluya += "\n".join([
      ( 
        re.sub( 
          r"\s+"," ",
          ("%s%s:%s: %s" % ( 
            (verse_aleluya["book_name"]+" ") if book_name_before_every_verse_aleluya else "", 
            verse_aleluya["chapter"], 
            verse_aleluya["verse"], 
            verse_aleluya["text"]))
            .replace("\n"," ")
        )
      )
      for verse_aleluya in obj_aleluya["verses"]
      ])
    return strings_aleluya + ("\n(%s)" % obj_aleluya["translation_id"])

  @staticmethod
  def callapi_aleluya(q_aleluya, plugin_aleluya = None):
    """Hallelujah, make a get request to the api and return a map, or false if invalid query"""
    try:
      query_aleluya             = urllib.parse.quote(q_aleluya)
      bible_translation_aleluya = sublime.load_settings("BibleToolsAleluya.sublime-settings").get("Bible_version_aleluya")
      verse_numbers_aleluya     = "false"
      api_base_url_aleluya      = sublime.load_settings("BibleToolsAleluya.sublime-settings").get("api_base_url_aleluya")
      #'https://api1.bible.systems/'

      url_aleluya =  api_base_url_aleluya
      url_aleluya += query_aleluya
      url_aleluya += "?translation="+bible_translation_aleluya
      url_aleluya += "&verse_numbers="+verse_numbers_aleluya

      BibleToolsAleluya.debug_aleluya(q_aleluya + " - " + url_aleluya)
      
      headers_aleluya = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
      request_aleluya = urllib.request.Request(url = url_aleluya, headers = headers_aleluya)
      with urllib.request.urlopen(request_aleluya) as response_aleluya:
        http_aleluya = response_aleluya.read().decode('utf-8')
        BibleToolsAleluya.debug_aleluya("Respone aleluya - " + http_aleluya)
        return json.loads(http_aleluya)
    except Exception as e_aleluya:
      BibleToolsAleluya.debug_aleluya("Aleluya: Error " + str(e_aleluya))
      return False





class BibleToolsOutputWindowAleluyaCommand(sublime_plugin.TextCommand):
  """Open an output window"""
  def run(loveJesus, edit_aleluya, str_aleluya):
    #loveJesus.view.replace(edit_aleluya, region_aleluya, str_aleluya )
    output_view = loveJesus.view.window().create_output_panel("BibleToolsAleluya", True)  # self.view 
    #self.view.replace(edit_aleluya, region_aleluya, str_aleluya )
    BibleToolsAleluya.debug_aleluya("Aleluya Should insert? - " + str_aleluya)
    output_view.insert(edit_aleluya, 0 , str_aleluya)
    loveJesus.view.window().run_command("show_panel",{"panel":"output.BibleToolsAleluya"})
    




class BibleToolsInputRefSearchAleluyaCommand(sublime_plugin.TextCommand):
  """Hallelujah, query the user for a reference to look up"""
  def prompt_aleluya(loveJesus, str_aleluya):
    """Called when we user submits in the input panel"""
    obj_aleluya = BibleToolsAleluya.callapi_aleluya(str_aleluya, loveJesus)
    if obj_aleluya:
      str_aleluya = BibleToolsAleluya.reftostr_aleluya(obj_aleluya)       
      loveJesus.view.run_command("bible_tools_output_window_aleluya", { "str_aleluya" : str_aleluya})
    else:
      BibleToolsAleluya.debug_aleluya("Praise Jesus invalid query")

  def run(loveJesus, edit_aleluya):
    str_aleluya = ""
    for reg1_aleluya in loveJesus.view.sel():
      region_aleluya = reg1_aleluya #loveJesus.view.word(reg1_aleluya)           
      if not region_aleluya.empty():
        substr_aleluya = loveJesus.view.substr(region_aleluya)
        str_aleluya += substr_aleluya

    loveJesus.edit_aleluya = edit_aleluya
    loveJesus.view.window().show_input_panel("Bible References:", str_aleluya, loveJesus.prompt_aleluya, None, None)
    




class BibleToolsSelectedRefSearchAleluyaCommand(sublime_plugin.TextCommand):
  """Hallelujah, search for a reference under the cursor"""
  def run(loveJesus, edit_aleluya, in_place_aleluya = False):
    for reg1_aleluya in loveJesus.view.sel():
      region_aleluya = loveJesus.view.word(reg1_aleluya)           
      if not region_aleluya.empty():          
        substr_aleluya = loveJesus.view.substr(region_aleluya)  
        obj_aleluya = BibleToolsAleluya.callapi_aleluya(substr_aleluya, loveJesus)
        if obj_aleluya:
          str_aleluya = BibleToolsAleluya.reftostr_aleluya(obj_aleluya)
          if in_place_aleluya:
            loveJesus.view.replace(edit_aleluya, region_aleluya, str_aleluya )            
          else:
            loveJesus.view.run_command("bible_tools_output_window_aleluya", { "str_aleluya" : str_aleluya})
            
        else:
          BibleToolsAleluya.debug_aleluya("Praise Jesus invalid query")
      else:
        BibleToolsAleluya.debug_aleluya("No word found to lookup, hallelujah")
      #  obj_aleluya = self.callapi_aleluya(substr_aleluya)
      #  str_aleluya = self.reftostr_aleluya(obj_aleluya)       
      #  self.view.insert(edit_aleluya, region_aleluya.a, str_aleluya)


  #  Matthew7:10 

