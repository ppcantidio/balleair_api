from flask import Flask
from dotenv import load_dotenv
from webapi.config import DevelopmentConfig


load_dotenv('.env')

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

from webapi.routes.flights import flights_routes
app.register_blueprint(flights_routes, url_prefix='/api/v1/flight')

from webapi.routes.bookings import bookings_routes
app.register_blueprint(flights_routes, url_prefix='/api/v1/booking')
