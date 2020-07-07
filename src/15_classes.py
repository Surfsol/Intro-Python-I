# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    #method
    def fullname(self):
        return '{} {}'.format(self.lat, self.lon)

cali = LatLon(20, 30)

cali.fullname()
LatLon.fullname(cali)
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

#https://www.educative.io/edpresso/what-is-super-in-python#:~:text=The%20super()%20function%20in,super%20(parent)%20class%20explicitly.
# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        self.name = name
        super().__init__(lat, lon)
    def __str__(self):
        return(f"{self.name}, {self.lat}, {self.lon}")

waypoint = Waypoint("Catacombs", 41.70505, -121.51521)

print(waypoint)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
# waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
# # Without changing the following line, how can you make it print into something
# # more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
#geocache = Geocache("Newberry Views", 1.5, size 2, 44.052137, -121.41556)
# YOUR CODE HERE

# Print it--also make this print more nicely
#print(geocache)
