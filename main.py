import webapp2
from caesar import encrypt

form = '''
    <form method = "post" action = "cyphered">
        <label>ROT </label><input type  = "number" min ="-26" max = "26" name = "r"><br>
        <label>Text <textarea name = "t"></textarea></label><br>
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
        ctext = encrypt(t, r)
        newform1 = '<form method = "post" action = "cyphered">'
        newform2 = '<label>ROT <input type = "number" min = "-26" max = "26" name = "r" value = ' 
        newform3 = '></label><br>'
        newform4 = '<label>Text <textarea name = "t">'
        newform5 = '''</textarea></label><br>
        <input type = "submit">
            </form>
        '''
        self.response.out.write(newform1 + "\n" + newform2 + str(r) + newform3 + "\n" + newform4 + ctext + newform5)

app = webapp2.WSGIApplication([('/', MainHandler), ('/cyphered', EncryptHandler)], debug = True)
