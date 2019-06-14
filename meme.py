from google.appengine.ext import ndb

class Meme(ndb.Model):
    top_line = ndb.StringProperty(required=False)
    bottom_line = ndb.StringProperty(required=False)

    date_str = ndb.StringProperty(required=True)
    author = ndb.StringProperty(required=True)
    image_id = ndb.StringProperty(required=True)

    def get_meme_url(self):
        if( self.image_id == 'college-grad'):
            url = "https://vignette.wikia.nocookie.net/vocaloid/images/7/76/Rin_len_v4x_design.png/revision/latest/scale-to-width-down/530?cb=20190426200904" #your choice
        elif( self.image_id == 'thinking-ape'):
            url = 'https://upload.wikimedia.org/wikipedia/commons/f/ff/Deep_in_thought.jpg'
        elif( self.image_id == 'coding'):
            url = 'https://upload.wikimedia.org/wikipedia/commons/b/b9/Typing_computer_screen_reflection.jpg'
        elif ( self.image_id == 'old-class'):
            url = 'https://upload.wikimedia.org/wikipedia/commons/4/47/StateLibQld_1_100348.jpg'

        return url
