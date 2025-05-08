class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, orig_iata, dest_iata, dep_time, return_time):
        self.price = price
        self.orig_iata = orig_iata
        self.dest_data = dest_iata
        self.dep_time = dep_time
        self.return_time = return_time
        
    def cheapest_flight(flights):
        if flights is None or not data['data']:
            print("No flight data")
            return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")
        
        cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)
        
        for flight in flights["data"]:
            price = float(flight["price"]["grandTotal"])
            if price < lowest_price:
                lowest_price = price
                origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
                destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
                out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
                return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
                cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)
                print(f"Lowest price to {destination} is £{lowest_price}")

        return cheapest_flight