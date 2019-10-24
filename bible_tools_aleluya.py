# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
#Thanks Jesus for bible-api.com
#{"reference":"John 3:16","verses":[{"book_id":"JHN","book_name":"John","chapter":3,"verse":16,"text":"\nFor God so loved the world, that he gave his one and only Son, that whoever believes in him should not perish, but have eternal life.\n\n"}],"text":"\nFor God so loved the world, that he gave his one and only Son, that whoever believes in him should not perish, but have eternal life.\n\n","translation_id":"web","translation_name":"World English Bible","translation_note":"Public Domain"}
import sublime, sublime_plugin
import json
import urllib.request
import urllib.parse

class BibleToolsAleluyaCommand(sublime_plugin.TextCommand):
  """Hallelujah, tools to work with the Bible, particularly references at this point"""

  def callapi_aleluya(self, q_aleluya):
    """Hallelujah, make a get request to the api and return a map, or false if invalid query"""
    try:
      query_aleluya = urllib.parse.quote(q_aleluya)
      url_aleluya = 'https://api1.bible.systems/' + query_aleluya
      print("q_aleluya " + q_aleluya + " - " + url_aleluya)
      headers_aleluya = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
      request_aleluya = urllib.request.Request(url=url_aleluya, headers=headers_aleluya)
      with urllib.request.urlopen(request_aleluya) as response_aleluya:
        print("Aleluya");
        http_aleluya = response_aleluya.read().decode('utf-8')
        print("Aleluya - " + http_aleluya)
        return json.loads(http_aleluya)
    except Exception as e_aleluya:
      print("ALeluya: Error " + str(e_aleluya))
      return False

  def reftostr_aleluya(self, obj_aleluya):
    return obj_aleluya["reference"] +": " + obj_aleluya["text"][1:-1] + " -" + obj_aleluya["translation_id"]

  def run(self, edit_aleluya):
    for reg1_aleluya in self.view.sel():
      region_aleluya = self.view.word(reg1_aleluya)              
      if not region_aleluya.empty():          
        substr_aleluya = self.view.substr(region_aleluya)  
        obj_aleluya = self.callapi_aleluya(substr_aleluya)
        if obj_aleluya:
          str_aleluya = self.reftostr_aleluya(obj_aleluya)       
          self.view.replace(edit_aleluya, region_aleluya, str_aleluya )
        else:
          print("Praise Jesus invalid query")
      else:
        print("No word found to lookup, hallelujah")
      #  obj_aleluya = self.callapi_aleluya(substr_aleluya)
      #  str_aleluya = self.reftostr_aleluya(obj_aleluya)       
      #  self.view.insert(edit_aleluya, region_aleluya.a, str_aleluya)


  #  Matthew7:10 

