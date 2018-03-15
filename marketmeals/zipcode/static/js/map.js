



function drawMap( coords, zipcode ) {
	if ( coords ) {
		console.log( 'ZipCode: ' + zipcode )
		console.log( 'Coords:', coords )
		var geo = { center: coords, zoom: 11 }
		var map = new google.maps.Map( document.getElementById( 'map' ), geo )
		browseMarkets( map, coords )
	}
}

function browseMarkets( map, coords ) {
	var codex = [ ]
	var views = [ ]
	var seeker = new google.maps.places.PlacesService( map )
	var zone = { location: coords, radius: '250', query: 'farmers market' }
	seeker.textSearch( zone, function( markets, feedback ) {
		if ( feedback == google.maps.places.PlacesServiceStatus.OK ) {
			console.log( 'Markets:', markets )
			for ( var idx = 0; idx < markets.length; idx++ ) {
				var view = createLocation( markets[ idx ], map )
				views.push( view )
				if ( idx + 1 === markets.length ) {
					console.log( 'Views:', views )
				}
			}
		}
	} )
}

function createLocation( market, map ) {
	ViewClass( )
	/* var location = new google.maps.Marker( {
		map: map,
		position: market.geometry.location.toJSON( ),
		title: market.name
	} ) */
	farmerMarket = new View( market.geometry.location, market )
	farmerMarket.setMap( map )
	return farmerMarket
}



