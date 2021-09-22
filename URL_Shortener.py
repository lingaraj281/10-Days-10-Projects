# URL SHORTENER using Bit.ly
# Install pyshorteners module by using this pip3 install pyShorterners
from pyshorteners import Shortener

api_key1 = "058adfff52fa26eca420240ae10ecc386f64ae63"

shortner = Shortener(api_key=api_key1)

long_url = "https://in.pinterest.com/prior1390/pokemon-images/"

short_url = shortner.bitly.short(long_url)
Long_url = shortner.bitly.expand(short_url)
print(short_url)
print(Long_url)
