import webapp2
from caesar import encrypt

form = '''
    <form method = "post" action = "cyphered">
        <label>ROT <input type = "text" name = "r"></label><br>
        <label>Text <input type = "text" name = "t" value = "plain text"></label><br>
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
        newform2 = '<label>ROT <input type = "text" name = "r" value = ' 
        newform3 = '></label><br>'
        newform4 = '<label>Text <input type = "text" name = "t" value = '
        newform5 = '''></label><br>
        <input type = "submit">
            </form>
        '''
        self.response.out.write(newform1 + newform2 + str(r) + newform3 + newform4 + ctext + newform5)

app = webapp2.WSGIApplication([('/', MainHandler), ('/cyphered', EncryptHandler)], debug = True)
