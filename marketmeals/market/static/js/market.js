



window.addEventListener( 'load', fetchMarket )


function fetchMarket( ) {
	var url = window.location.pathname
	if ( url.substring( 0, 8 ) === '/market/' ) {
		console.log( 'Subroute: ' + url.substring( 0, 8 ) )
		var name = url.substring( 8 )
		console.log( 'Url: ' + name )
		var map = document.createElement( 'div' )
		map.style.display = 'none'
		var seeker = new google.maps.places.PlacesService( map )
		var query = { query: name }
		seeker.textSearch( query, function( markets, feedback ) {
			if ( feedback == google.maps.places.PlacesServiceStatus.OK ) {
				console.log( 'Markets:', markets )
				reverseGeocode( new google.maps.Geocoder( ), markets[ 0 ] )
			}
		} )
	}
}


