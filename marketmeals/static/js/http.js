



var http = new XMLHttpRequest( )


window.addEventListener( 'load', getZipCode )


function getZipCode( ) {
	if ( document.getElementById( 'map' ) ) {
		http.onreadystatechange = function( ) {
			if ( http.readyState === XMLHttpRequest.DONE && http.status === 200 ) {
				viewGeocode( new google.maps.Geocoder( ), http.responseText )
			}
		}
		http.open( 'GET', '/location' )
		http.send( )
	}
}

function exportJson( amalgam ) {
	http.onreadystatechange = function( ) {
		if ( http.readyState === XMLHttpRequest.DONE && http.status === 200 ) {
			var json = JSON.parse( http.response )
			console.log( 'Response: ', json )
			if ( document.getElementById( 'map' ) ) {
				var extra = document.getElementsByClassName( 'extra' )[ 0 ]
				extra.setAttribute( 'action', '/market/' + json.url )
				var visit = document.getElementsByClassName( 'visit' )[ 0 ]
				console.log( extra )
				console.log( visit )
				var url = document.createElement( 'input' )
				url.setAttribute( 'type', 'hidden' )
				url.setAttribute( 'name', 'url' )
				url.setAttribute( 'value', json.url )
				extra.insertBefore( url, visit )
			}
			else {
				var title = document.getElementById( 'title' ).innerText
				console.log( 'HTML Title: ' + title )
				console.log( 'JSON Title: ' + json.title )
				if ( title !== json.title ) {
					window.location.reload( )
				}
			}
		}
	}
	http.open( 'POST', '/url' )
	http.setRequestHeader( 'Content-Type', 'application/json' )
	http.send( JSON.stringify( amalgam ) )
}


