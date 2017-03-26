import webapp2
from cgi import escape
from caesar import encrypt

form1 = '''<form method = "post" action = "">
<label>ROT <input type = "number" min = "-26" max = "26" name = "r" value = '''
form2 = '''></label><br>
<textarea rows = "4" cols = "50" name = "t" placeholder = "Enter text to be encypered...">'''
form3 = '''</textarea><br>
<input type = "submit">
    </form>
'''

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form1 + form2 + form3)

    def post(self):
        r = int(self.request.get("r"))
        t = str(self.request.get("t"))
        t = t
        ctext = encrypt(t, r)
        self.response.out.write(form1 + str(r) + form2 + escape(ctext) + form3)

app = webapp2.WSGIApplication([('/', MainHandler)], debug = True)
