import webapp2
from cgi import escape
from caesar import encrypt

pageHTML = '''
    <!DOCTYPE HTML>
    <html>
    <head><title>Caesar Rotation Cypher</title></head>
    <body>
    <h1>Caesar Rotation Cypher</h1><br>
    <h2>Enter a number (-26 to 26) and some text to encypher using Caesar Rotation</h2><br>
    <form method = "post" action = "">
    <label>ROT <input type = "number" min = "-26" max = "26" name = "r" value = %d></label><br>
    <textarea rows = "4" cols = "50" name = "t" placeholder = "Enter text to be encypered...">%s</textarea><br>
    <input type = "submit">
    </form>
    <h6>git clone <a href = "https://github.com/bryandobberstein/web-caesar.git">https://github.com/bryandobberstein/web-caesar.git</a></h6>
    </body>
    </html>
'''

class MainHandler(webapp2.RequestHandler):
    def write_form(self, num = 0, txt = ""):
        txt = escape(txt, quote = True)
        self.response.write(pageHTML %(num, txt))

    def get(self):
        self.write_form()

    def post(self):
        r = int(self.request.get("r"))
        t = str(self.request.get("t"))
        ctext = encrypt(t, r)
        self.write_form(r, ctext)

app = webapp2.WSGIApplication([('/', MainHandler)], debug = True)
