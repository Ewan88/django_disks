from .models import *

artist1 = Artist(name="Bilbo Baggins")
artist2 = Artist(name="Melinda MacIlroy")
artist1.save()
artist2.save()

album1 = Album(title="Bilbo's Ballads", year=1992, stock_level=10, artist=artist1)
album2 = Album(title="Melinda's Melodies", year=1940, stock_level=5, artist=artist2)
album1.save()
album2.save()