from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField, SubmitField
from wtforms.validators import DataRequired, AnyOf, URL


class ShowForm(FlaskForm):
    artist_id = StringField('artist_id', validators = [DataRequired('please add an artist id')])
    venue_id = StringField('venue_id', validators = [DataRequired('please add a veneue id')])
    start_time = DateTimeField('start_time',validators=[DataRequired('please add a start time')],default=datetime.today())
    upcoming =BooleanField('seeking_talent')
class VenueForm(FlaskForm): 
    states=[
            ('AL', 'AL'),
            ('AK', 'AK'),
            ('AZ', 'AZ'),
            ('AR', 'AR'),
            ('CA', 'CA'),
            ('CO', 'CO'),
            ('CT', 'CT'),
            ('DE', 'DE'),
            ('DC', 'DC'),
            ('FL', 'FL'),
            ('GA', 'GA'),
            ('HI', 'HI'),
            ('ID', 'ID'),
            ('IL', 'IL'),
            ('IN', 'IN'),
            ('IA', 'IA'),
            ('KS', 'KS'),
            ('KY', 'KY'),
            ('LA', 'LA'),
            ('ME', 'ME'),
            ('MT', 'MT'),
            ('NE', 'NE'),
            ('NV', 'NV'),
            ('NH', 'NH'),
            ('NJ', 'NJ'),
            ('NM', 'NM'),
            ('NY', 'NY'),
            ('NC', 'NC'),
            ('ND', 'ND'),
            ('OH', 'OH'),
            ('OK', 'OK'),
            ('OR', 'OR'),
            ('MD', 'MD'),
            ('MA', 'MA'),
            ('MI', 'MI'),
            ('MN', 'MN'),
            ('MS', 'MS'),
            ('MO', 'MO'),
            ('PA', 'PA'),
            ('RI', 'RI'),
            ('SC', 'SC'),
            ('SD', 'SD'),
            ('TN', 'TN'),
            ('TX', 'TX'),
            ('UT', 'UT'),
            ('VT', 'VT'),
            ('VA', 'VA'),
            ('WA', 'WA'),
            ('WV', 'WV'),
            ('WI', 'WI'),
            ('WY', 'WY'),
        ]
    genre_choices=[
            ('Alternative', 'Alternative'),
            ('Blues', 'Blues'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Electronic', 'Electronic'),
            ('Folk', 'Folk'),
            ('Funk', 'Funk'),
            ('Hip-Hop', 'Hip-Hop'),
            ('Heavy-Metal', 'Heavy-Metal'),
            ('Instrumental', 'Instrumental'),
            ('Jazz', 'Jazz'),
            ('Musical-Theatre', 'Musical-Theatre'),
            ('Pop', 'Pop'),
            ('Punk', 'Punk'),
            ('R&B', 'R&B'),
            ('Reggae', 'Reggae'),
            ('Rock-n-Roll', 'Rock-n-Roll'),
            ('Soul', 'Soul'),
            ('Other', 'Other'),
        ]    
    name = StringField('name', validators=[DataRequired('please add a name')])
    city = StringField('city', validators = [DataRequired()])
    state = SelectField('state', choices=states, validators = [DataRequired('please select a state')])
    address = StringField('address', validators=[DataRequired('please add an address')])
    phone = StringField('phone', validators=[DataRequired('please add a phone number')])
    image_link = StringField('image_link', validators = [URL()])
    genres = SelectMultipleField('genres', validators=[DataRequired('please add at least one genre')], choices=genre_choices)
    facebook_link = StringField('facebook_link', validators=[URL()])
    website = StringField('website', validators=[URL()])
    seeking_talent = BooleanField('seeking_talent')
    seeking_description = StringField('seeking_description')
    submit = SubmitField('Submit')

#----------------------------------------------------------------------------

class ArtistForm(FlaskForm):
    states=[
        ('AL', 'AL'),
        ('AK', 'AK'),
        ('AZ', 'AZ'),
        ('AR', 'AR'),
        ('CA', 'CA'),
        ('CO', 'CO'),
        ('CT', 'CT'),
        ('DE', 'DE'),
        ('DC', 'DC'),
        ('FL', 'FL'),
        ('GA', 'GA'),
        ('HI', 'HI'),
        ('ID', 'ID'),
        ('IL', 'IL'),
        ('IN', 'IN'),
        ('IA', 'IA'),
        ('KS', 'KS'),
        ('KY', 'KY'),
        ('LA', 'LA'),
        ('ME', 'ME'),
        ('MT', 'MT'),
        ('NE', 'NE'),
        ('NV', 'NV'),
        ('NH', 'NH'),
        ('NJ', 'NJ'),
        ('NM', 'NM'),
        ('NY', 'NY'),
        ('NC', 'NC'),
        ('ND', 'ND'),
        ('OH', 'OH'),
        ('OK', 'OK'),
        ('OR', 'OR'),
        ('MD', 'MD'),
        ('MA', 'MA'),
        ('MI', 'MI'),
        ('MN', 'MN'),
        ('MS', 'MS'),
        ('MO', 'MO'),
        ('PA', 'PA'),
        ('RI', 'RI'),
        ('SC', 'SC'),
        ('SD', 'SD'),
        ('TN', 'TN'),
        ('TX', 'TX'),
        ('UT', 'UT'),
        ('VT', 'VT'),
        ('VA', 'VA'),
        ('WA', 'WA'),
        ('WV', 'WV'),
        ('WI', 'WI'),
        ('WY', 'WY'),
    ]
    genres_choices=[
        ('Alternative', 'Alternative'),
        ('Blues', 'Blues'),
        ('Classical', 'Classical'),
        ('Country', 'Country'),
        ('Electronic', 'Electronic'),
        ('Folk', 'Folk'),
        ('Funk', 'Funk'),
        ('Hip-Hop', 'Hip-Hop'),
        ('Heavy-Metal', 'Heavy-Metal'),
        ('Instrumental', 'Instrumental'),
        ('Jazz', 'Jazz'),
        ('Musical-Theatre', 'Musical-Theatre'),
        ('Pop', 'Pop'),
        ('Punk', 'Punk'),
        ('R&B', 'R&B'),
        ('Reggae', 'Reggae'),
        ('Rock-n-Roll', 'Rock-n-Roll'),
        ('Soul', 'Soul'),
        ('Other', 'Other'),
    ]
    name = StringField('name', validators = [DataRequired('please add a name')])
    city = StringField('city', validators = [DataRequired('please add a city')])
    state = SelectField('state', choices=states, validators = [DataRequired('please select a state')])
    phone = StringField('phone', validators = [DataRequired('please add a phone number')])    
    image_link = StringField('image_link', validators = [URL()])
    genres = SelectMultipleField('genres', choices=genres_choices, validators=[DataRequired('please select at least one genre')])
    facebook_link = StringField('facebook_link', validators = [URL()])
    website = StringField('website', validators = [URL()])
    seeking_venue = BooleanField('seeking_venue', default=True)
    seeking_description = StringField('seeking_description')
    submit = SubmitField('Submit')

# TODO IMPLEMENT NEW ARTIST FORM AND NEW SHOW FORM
