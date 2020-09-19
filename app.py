#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
from flask_migrate import Migrate
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# TODO: connect to a local postgresql database ("done")

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'venues'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, default=True)
    seeking_description = db.Column(db.String(2000))
    genres = db.Column(db.String(120), nullable=False)
    shows = db.relationship('Show', backref='venues', lazy=True, cascade="all, delete-orphan")

        # TODO: implement any missing fields, as a database migration using Flask-Migrate




class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default=True)
    seeking_description = db.Column(db.String(2000))
    shows = db.relationship('Show', backref='artist', lazy=True, cascade="all, delete-orphan")
    genres = db.Column(db.String(120), nullable=False)


    def __repr__(self):
      return self.name
    # TODO: implement any missing fields, as a database migration using Flask-Migrate
class Show(db.Model):
  __tablename__='shows'
  id = db.Column(db.Integer, primary_key=True)
  artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
  venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)
  start_time = db.Column(db.String(100), default=False)
  upcoming = db.Column(db.Boolean, default=True)


  # TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format)

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  return render_template('pages/home.html')


#  Venues
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():
  # TODO: replace with real venues data.
  #       num_shows should be aggregated based on number of upcoming shows per venue.
  #("Done")
  venues = Venue.query.all()
  return render_template('pages/venues.html', venues=venues)

@app.route('/venues/search', methods=['POST'])
def search_venues():
  # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for Hop should return "The Musical Hop".
  # search for "Music" should return "The Musical Hop" and "Park Square Live Music & Coffee"
  #("Done")
  search_term = request.form['search_term']
  response = Venue.query.filter(Venue.name.ilike('%' + search_term + '%'))
  return render_template('pages/search_venues.html', results=response, search_term=search_term)

@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  # shows the venue page with the given venue_id
  # TODO: replace with real venue data from the venues table, using venue_id
  data = Venue.query.get(venue_id)
  data.genres = help(data.genres)  #changeing genres format
  upcoming_shows_count = Show.query.filter(Show.venue_id==venue_id, Show.upcoming==True).count()
  upcoming_shows = Show.query.filter(Show.venue_id==venue_id, Show.upcoming==True).all()

  past_shows_count = Show.query.filter(Show.venue_id==venue_id, Show.upcoming==False).count()
  past_shows= Show.query.filter(Show.venue_id==venue_id, Show.upcoming==False).all()

  return render_template('pages/show_venue.html', venue=data, upcoming_shows_count=upcoming_shows_count, past_shows_count=past_shows_count, past_shows=past_shows, upcoming_shows=upcoming_shows)

#  Create Venue
#  ----------------------------------------------------------------

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
  # TODO: insert form data as a new Venue record in the db, instead
  # TODO: modify data to be the data object returned from db insertion
  form = VenueForm()
  if form.validate_on_submit():
    try:
      new_venue = Venue(
        name=form.name.data,
        city=form.city.data,
        state=form.state.data,
        address=form.address.data, 
        phone=form.phone.data, 
        image_link=form.image_link.data, 
        genres=form.genres.data, 
        facebook_link=form.facebook_link.data,
        website=form.website.data,
        seeking_talent=form.seeking_talent.data,
        seeking_description=form.seeking_description.data,
      )
      db.session.add(new_venue)
      db.session.commit()
      flash('Venue successfully added')
      return redirect(url_for('venues'))
    except:
      db.session.rollback()
    finally:
      db.session.close()
  flash('Venue could not be listed')    
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/<venue_id>/delete', methods=['DELETE', 'POST'])
def delete_venue(venue_id):
  # TODO: Complete this endpoint for taking a venue_id, and using
  # SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.
  venue_to_delete = Venue.query.get(venue_id)
  try:
    db.session.delete(venue_to_delete)
    db.session.commit()
    flash("venue deleted successfully")
    return redirect(url_for('index'))
  except:
    db.session.rollback()
  finally:
    db.session.close()
  return redirect(url_for('show_venue', venue_id=venue_to_delete_id))
  # BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
  # clicking that button delete it from the db then redirect the user to the homepage

# ----------------------------------------------------------------
#   DELETE ARTIST
@app.route('/artist/<artist_id>/delete', methods=['DELETE', 'POST'])
def delete_artist(artist_id):
  artist_to_delete = Artist.query.get(artist_id)
  try:
    db.session.delete(artist_to_delete)
    db.session.commit()
    flash("artist deleted successfully")
    return redirect(url_for('index'))
  except:
    db.session.rollback()
  finally:
    db.session.close()
  return redirect(url_for('show_artist', artist_id=artist_to_delete.id))

#  Artists
#  ----------------------------------------------------------------
@app.route('/artists')
def artists():
  # TODO: replace with real data returned from querying the database ("done")
  data = Artist.query.all()
  return render_template('pages/artists.html', artists=data)

@app.route('/artists/search', methods=['POST'])
def search_artists():
  # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for "A" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band".
  # search for "band" should return "The Wild Sax Band". ("Done")

  search_term = request.form['search_term']
  response = Artist.query.filter(Artist.name.ilike('%' + search_term + '%'))
  
  return render_template('pages/search_artists.html', results=response, search_term=search_term)

#-------------------------------
#    CREATE A LIST OUT OF STRING. to change genres from this format {'genre1, genre2'}
#    to this format ['genre1', 'genre2']

def help(s):
  s = s.replace(s[0:1], '')
  s = s.replace(s[len(s)-1], '')
  
  for i in s:
    if i == ',':
      s = s.replace(i, ' ')
  s = s.split()

  return s
#----------------------------------

@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  # shows the venue page with the given venue_id
  # TODO: replace with real venue data from the venues table, using venue_id ("Done")
  upcoming_shows_count = Show.query.filter(Show.artist_id==artist_id, Show.upcoming==True).count()
  upcoming_shows = Show.query.filter(Show.artist_id==artist_id, Show.upcoming==True).all()

  past_shows_count = Show.query.filter(Show.artist_id==artist_id, Show.upcoming==False).count()
  past_shows= Show.query.filter(Show.artist_id==artist_id, Show.upcoming==False).all()
  data = Artist.query.get(artist_id)
  data.genres = help(data.genres) #changeing genres format

  return render_template('pages/show_artist.html',
   artist=data,
   upcoming_shows_count=upcoming_shows_count,
   upcoming_shows=upcoming_shows,
   past_shows_count=past_shows_count,
   past_shows=past_shows
    )

#  Update
#  ----------------------------------------------------------------
@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  artist = Artist.query.get(artist_id)
  form = ArtistForm(obj=artist)
  # TODO: populate form with fields from artist with ID <artist_id>
  return render_template('forms/edit_artist.html', form=form, artist=artist)

@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  artist = Artist.query.get(artist_id)
  form = ArtistForm()
  if form.validate_on_submit():
    try:
      artist.name = form.name.data
      artist.city = form.city.data
      artist.state = form.state.data
      artist.phone = form.phone.data
      artist.genres = form.genres.data
      artist.facebook_link = form.facebook_link.data
      artist.image_link = form.image_link.data
      artist.website = form.website.data
      artist.seeking_venue = form.seeking_venue.data
      artist.seeking_description = form.seeking_description.data
      db.session.commit()
      flash('Artist Updated successfully')
      return redirect(url_for('show_artist', artist_id=artist.id))
    except:
      db.session.rollback()
    finally:
      db.session.close()
  # TODO: take values from the form submitted, and update existing
  # artist record with ID <artist_id> using the new attributes
  flash("something went wrong, artist has not been updated")
  return render_template('forms/edit_artist.html', form=form, artist=artist)

@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  venue = Venue.query.get(venue_id)
  form = VenueForm(obj=venue)

  # TODO: populate form with values from venue with ID <venue_id>
  return render_template('forms/edit_venue.html', form=form, venue=venue)

@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  # TODO: take values from the form submitted, and update existing
  # venue record with ID <venue_id> using the new attributes
  venue = Venue.query.get(venue_id)
  form = VenueForm()
  if form.validate_on_submit():
    try:
      venue.name = form.name.data
      venue.city = form.city.data
      venue.state = form.state.data
      venue.address = form.address.data
      venue.phone = form.phone.data
      venue.image_link = form.image_link.data
      venue.genres = form.genres.data
      venue.facebook_link = form.facebook_link.data
      venue.website = form.website.data
      venue.seeking_talent = form.seeking_talent.data
      venue.seeking_description = form.seeking_description.data
      db.session.commit()
      flash("Venue Updated Successfully")
      return redirect(url_for('show_venue', venue_id=venue.id))
    except:
      db.session.rollback()
    finally:
      db.session.close()
  flash("something went wrong, venue has not been updated")
  print('check')
  return render_template('forms/edit_venue.html', form=form, venue=venue)

#  Create Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)


@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  form = ArtistForm()
  print(form.genres.data)
  if form.validate_on_submit():
    
    try:
      new_artist = Artist(
        name=form.name.data,
        city=form.city.data,
        state=form.state.data,
        phone=form.phone.data,
        genres=form.genres.data,
        facebook_link=form.facebook_link.data,
        image_link=form.image_link.data,
        website=form.website.data,
        seeking_venue=form.seeking_venue.data,
        seeking_description=form.seeking_description.data
        )
      db.session.add(new_artist)
      db.session.commit()
      flash('Artist added successfully')
      return redirect(url_for('artists'))
    except:
      db.session.rollback()
      
    finally:
      db.session.close()
  print("check6")
  flash('something wrong, Artist could not be listed')
  return render_template('forms/new_artist.html', form=form)
  # called upon submitting the new artist listing form
  # TODO: insert form data as a new Venue record in the db, instead
  # TODO: modify data to be the data object returned from db insertion
  
  # on successful db insert, flash success
  
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Artist ' + data.name + ' could not be listed.')


#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
  # displays list of shows at /shows
  # TODO: replace with real venues data.
  #       num_shows should be aggregated based on number of upcoming shows per venue.
  '''
  data=[{
    "venue_id": 1,
    "venue_name": "The Musical Hop",
    "artist_id": 4,
    "artist_name": "Guns N Petals",
    "artist_image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
    "start_time": "2019-05-21T21:30:00.000Z"
  }]
  '''
  data = Show.query.all()
  return render_template('pages/shows.html', shows=data)

@app.route('/shows/create',)
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  # called to create new shows in the db, upon submitting new show listing form
  # TODO: insert form data as a new Show record in the db, instead
  form = ShowForm()
  if form.validate_on_submit():
    # on successful db insert, flash success
    artist_id = form.artist_id.data
    venue_id = form.venue_id.data
    start_time = form.start_time.data
    upcoming = form.upcoming.data
    try:
      new_show = Show(artist_id=artist_id, venue_id=venue_id, start_time=start_time, upcoming=upcoming)
      db.session.add(new_show)
      db.session.commit()
    except:
      db.session.rollback()
    finally:
      db.session.close()
      flash("show added successfully")  
      return redirect(url_for('shows'))
        

  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Show could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  flash('An error occurred. Show could not be listed.')
  return render_template('forms/new_show.html', form=form)



#-----------------------------------------------------------------------------
#edit show form upcoming show to a past show


@app.route('/shows/<int:show_id>/edit', methods=['GET', 'POST'])
def edit_show(show_id):
  show = Show.query.get(show_id)
  form = ShowForm(obj=show)
  if form.validate_on_submit():
    try:
      show.upcoming = form.upcoming.data
      db.session.commit()
      flash('show updated successfully')
      return redirect(url_for('index'))
    except:
      db.session.rollback()
      flash('something went wrong')
    finally:
      db.session.close()
  return render_template('forms/edit_show.html', show=show, form=form)



#------------------------------------------------------------------------------
@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
