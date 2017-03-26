import webapp2
from cgi import escape
from caesar import encrypt

form = '''
    <form method = "post" action = "">
    <label>ROT <input type = "number" min = "-26" max = "26" name = "r" value = %d></label><br>
    <textarea rows = "4" cols = "50" name = "t" placeholder = "Enter text to be encypered...">%s</textarea><br>
    <input type = "submit">
    </form>
'''

class MainHandler(webapp2.RequestHandler):
    def write_form(self, num = 0, txt = ""):
        txt = escape(txt)
        self.response.out.write(form %(num, txt))

    def get(self):
        self.write_form()

    def post(self):
        r = int(self.request.get("r"))
        t = str(self.request.get("t"))
        ctext = encrypt(t, r)
        self.write_form(r, ctext)

app = webapp2.WSGIApplication([('/', MainHandler)], debug = True)
