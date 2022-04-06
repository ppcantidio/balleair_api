from webapi.utils.database import Database

db = Database()

class FlightModel:

    def __init__(self, departure_airport, arrival_airport, flight_date, aircraft, pax_available, pax_booked):
        self.departure_airport = self.validate_airport(departure_airport)
        self.arrival_airport = self.validate_airport(arrival_airport)
        self.flight_date = self.validate_date(flight_date)
        self.aircraft = self.validate_aircraft(aircraft)
        self.pax_available = self.validate_integer(pax_available)
        self.pax_booked = self.validate_integer(pax_booked)

    def validate_airport(self, value):
        pass

    def validate_date(self, value):
        pass

    def validate_aircraft(self, value):
        pass

    def validate_integer(self, value):
        pass

    def create_flight(self):
        flight_number = ''

        flight_doc = {
            'flightNumber': flight_number, # Número do voo *Identificador único
            'departureAirport': self.departure_airport,  # Aeroporto de saída   -> Guarulhos
            'arrivalAirport': self.arrival_airport,    # Aeroporto de chegada -> Galeão
            'flightDate': self.flight_date,  # Data do Voo
            'aircraft': self.aircraft,        # Aeronave que será utilizada
            'pax': {                   # Objeto com dados referentes aos passageiros
                'available': self.pax_available,        # Quantidade máxima de passageiros para essa aeronave
                'booked': self.pax_booked            # Quantidade de assentos reservados até o momento
            },
        }

        db.insert_object(flight_doc, 'flights_api')

        return flight_doc