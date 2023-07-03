from http.server import BaseHTTPRequestHandler
from urllib import parse, request

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    path = self.path
    url_components = parse.urlsplit(path)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)
    
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    
    word = dic['word']
    url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"
    response = request.get(url + word)
    
    message = f'definition soon {response}'
    self.wfile.write(message.encode())
    return
  