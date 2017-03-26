import webapp2
from cgi import escape
from caesar import encrypt

form1 = '''<form method = "post" action = "cyphered">
<label>ROT <input type = "number" min = "-26" max = "26" name = "r" value = '''
form2 = '''></label><br>
<label>Text <textarea name = "t">'''
form3 = '''</textarea></label><br>
<input type = "submit">
    </form>
'''

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form1 + form2 + form3)

class EncryptHandler(webapp2.RequestHandler):
    def post(self):
        r = int(self.request.get("r"))
        t = str(self.request.get("t"))
        t = t
        ctext = encrypt(t, r)
        self.response.out.write(form1 + str(r) + form2 + escape(ctext) + form3)

app = webapp2.WSGIApplication([('/', MainHandler), ('/cyphered', EncryptHandler)], debug = True)
