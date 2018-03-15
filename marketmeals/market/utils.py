



from marketmeals import db
from marketmeals.market.models import Market



path = '/market/static'
html = 'templates'
static = 'static'


def urlify( label, zipcode ):
	url = ''
	prev = ''
	for char in label:
		if prev == '-' and not char.isalnum( ):
			if char == '&':
				url += char
				prev = char
			else:
				pass
		elif char.isalnum( ):
			if char.isupper( ):
				url += char.lower( )
				prev = char.lower( )
			else:
				url += char
				prev = char
		elif char.isspace( ):
			url += '-'
			prev = '-'
	url = url + '-' + zipcode
	return url


def catalog( name, url, addresses ):
	street = ''
	city = ''
	state = ''
	zipcode = None
	for sub in addresses:
		for area in sub[ 'types' ]:
			if area == 'street_number':
				street = sub[ 'short_name' ] + ' '
			## Some markets don't have route strings provided
			elif area == 'route':
				street += sub[ 'short_name' ]
			elif area == 'locality' or area == 'sublocality' or area == 'neighborhood':
				city = sub[ 'short_name' ]
			elif area == 'administrative_area_level_1':
				state = sub[ 'short_name' ]
			elif area == 'postal_code':
				zipcode = sub[ 'short_name' ]
	market = Market( name = name, url = url, address_1 = street, city = city, state = state, zip_code = zipcode )
	return market



