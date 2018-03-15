



function viewGeocode( geocode, zipcode ) {
	var scope = { address: zipcode, componentRestrictions: { postalCode: zipcode }, region: '021' }
	geocode.geocode( scope, function( geodata, feedback ) {
		if ( feedback === 'OK' ) {
			var coords = geodata[ 0 ].geometry.location.toJSON( )
			console.log( 'Geocode:', geodata[ 0 ] )
			drawMap( coords, zipcode )
		}
		else if ( window.location.pathname === '/' ) {
			return
		}
		else {
			console.error( 'There was a problem trying to geocode!  ' + feedback )
			window.location.pathname = ''
		}
	} )
}

function reverseGeocode( geocode, market ) {
	console.log( 'Location:', market )
	var id = { placeId: market.place_id }
	geocode.geocode( id, function( geodata, feedback ) {
		if ( feedback === 'OK' ) {
			console.log( 'Amalgam:', geodata )
			var zipcode = ''
			for ( var idx = geodata[ 0 ].address_components.length - 1; idx >= 0; idx-- ) {
				if ( geodata[ 0 ].address_components[ idx ].types[ 0 ] === 'postal_code' ) {
					zipcode = geodata[ 0 ].address_components[ idx ].short_name
				}
			}
			console.log( 'ZipCode: ' + zipcode )
			var amalgam = {
				address_components: geodata[ 0 ].address_components,
				formatted_address: market.formatted_address,
				location: [ market.geometry.location.toJSON( ), geodata[ 0 ].geometry.location.toJSON( ) ],
				id: market.id,
				name: market.name,
				zip_code: zipcode,
				place_id: market.place_id,
				reference: market.reference,
				types: [ market.types, geodata[ 0 ].types ]
			}
			exportJson( amalgam )
		}
		else {
			console.error( 'An error occurred while reverse geocoding!  ' + feedback )
		}
	} )
}


