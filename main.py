import webapp2
from caesar import encrypt

form = '''
    <form method = "post" action = "cyphered">
        <label>ROT <input type = "text" name = "r"></label><br>
        <label>Text <input type = "text" name = "t"></label><br>
        <input type = "submit">
    </form>
'''

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)

class EncryptHandler(webapp2.RequestHandler):
    def post(self):
        r = int(self.request.get("r"))
        t = str(self.request.get("t"))
        self.response.out.write(encrypt(t, r))

app = webapp2.WSGIApplication([('/', MainHandler), ('/cyphered', EncryptHandler)], debug = True)
