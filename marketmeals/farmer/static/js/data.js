



var http = new XMLHttpRequest( )


window.addEventListener( 'load', queryData )


function queryData( ) {
	if ( document.getElementById( 'query' ) ) {
		document.getElementById( 'query' ).onclick = function( ) {
			observeData( )
		}
	}
}

function observeData( ) {
	http.onreadystatechange = function( ) {
		if ( http.readyState === XMLHttpRequest.DONE && http.status === 200 ) {
			console.log( 'Farmers:', JSON.parse( http.response ) )
		}
	}
	http.open( 'GET', '/data' )
	http.send( )
}


