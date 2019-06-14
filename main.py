import webapp2
import jinja2
import os
import meme


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


# the handler section
class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        welcome_template = the_jinja_env.get_template('templates/welcome.html')
        dd = {'greeting': 'hellloooo, konnichiwa',
        'adjective': 'lovely'}
        self.response.write(welcome_template.render(dd))


class ShowMemeHandler(webapp2.RequestHandler):
    def get(self):
        dd = { "img_url": "https://vignette.wikia.nocookie.net/vocaloid/images/3/3a/KAITO_V3.png/revision/latest/scale-to-width-down/350?cb=20180928095510",
        "line1": "test1",
        "line2": "test2"}
        results_template = the_jinja_env.get_template('templates/results.html')
        self.response.write(results_template.render(dd))  # the response

    def post(self):
        results_template = the_jinja_env.get_template('templates/results.html')
        meme_line1 = self.request.get("user-first-ln")
        meme_line2 = self.request.get("user-second-ln")
        meme_choice = self.request.get("meme-type")
        username = self.request.get("username")
        date = self.request.get("my_date")
        print(meme_line1, type(meme_line1) )
        print(meme_line2, type(meme_line2) )
        print(meme_choice, type(meme_choice) )

        my_meme = meme.Meme( top_line = meme_line1,
        bottom_line = meme_line2,
        date_str = date,
        author = username,
        image_id = meme_choice)

        user_info = { "line1" :  meme_line1,
        "line2": meme_line2,
        "img_url": my_meme.get_meme_url(),
        "username": username,
        "date_created": date
        }



        my_meme.put()

        self.response.write(results_template.render(user_info))  # the response

class ShowLibraryHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        library_template = the_jinja_env.get_template('templates/library.html')

        meme_query = meme.Meme.query()
        memes = meme_query.fetch()
        template_vars = {'memes': memes}

        self.response.write(library_template.render(template_vars))


app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/memeresult', ShowMemeHandler),
    ('/library', ShowLibraryHandler)
], debug=True)
