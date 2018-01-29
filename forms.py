# forms.py
from wtforms import Form, StringField, SelectField
 
class ClubSearchForm(Form):
    choices = [('Club Name', 'Keywords'), 
    			('Club Name', 'Club Name')
    		  ]
    select = SelectField('Search for clubs:', choices=choices)
    search = StringField('')