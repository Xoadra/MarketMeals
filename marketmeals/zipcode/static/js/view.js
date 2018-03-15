



function ViewClass( ) {
	
	// View class constructor for new custom views
	View = function( coords, market ) {
		this.coords = coords
		var element = document.createElement( 'div' )
		element.classList.add( 'view' )
		var title = document.createElement( 'h6' )
		element.appendChild( title )
		title.innerText = market.name
		var offset = document.createElement( 'div' )
		offset.classList.add( 'spike' )
		offset.appendChild( element )
		this.anchor = document.createElement( 'div' )
		this.anchor.classList.add( 'anchor' )
		this.anchor.appendChild( offset )
		this.stopEventPropagation( )
		this.buildElements( market, element, offset )
	}
	
	
	// Use api's OverlayView for using custom markers
	View.prototype = Object.create( google.maps.OverlayView.prototype )
	
	
	// Add the view on the map to display markets
	View.prototype.onAdd = function( ) {
		this.getPanes( ).floatPane.appendChild( this.anchor )
	}
	
	// Remove view from the map when finished
	View.prototype.onRemove = function( ) {
		if ( this.anchor.parentElement ) {
			this.anchor.parentElement.removeChild( this.anchor )
		}
	}
	
	// Calculate necessary view positional specifications
	View.prototype.draw = function( ) {
		var position = this.getProjection( ).fromLatLngToDivPixel( this.coords )
		var display = Math.abs( position.x ) < 4000 && Math.abs( position.y ) < 4000 ? 'block' : 'none'
		if ( display === 'block' ) {
			this.anchor.style.left = position.x + 'px'
			this.anchor.style.top = position.y + 'px'
		}
		if ( this.anchor.style.display !== display ) {
			this.anchor.style.display = display
		}
	}
	
	// Stops user behavior from interfering with the map
	View.prototype.stopEventPropagation = function( ) {
		var anchor = this.anchor
		anchor.style.cursor = 'auto'
		var events = [
			'click',
			'dblclick',
			'contextmenu',
			'mousedown',
			'touchstart',
			'pointerdown'
		]
		events.forEach( function( event ) {
			anchor.addEventListener( event, function( reaction ) {
				reaction.stopPropagation( )
			} )
		} )
	}
	
	// Insert enlarged view frames into the html document
	View.prototype.buildElements = function( market, view, offset ) {
		var extra = document.createElement( 'form' )
		extra.classList.add( 'extra' )
		extra.setAttribute( 'method', 'POST' )
		var head = document.createElement( 'div' )
		extra.appendChild( head )
		var title = document.createElement( 'h3' )
		head.appendChild( title )
		title.innerText = market.name
		var retract = document.createElement( 'button' )
		head.appendChild( retract )
		retract.classList.add( 'retract' )
		retract.innerText = 'X'
		var address = document.createElement( 'p' )
		extra.appendChild( address )
		address.innerText = market.formatted_address
		var visit = document.createElement( 'button' )
		extra.appendChild( visit )
		visit.classList.add( 'visit' )
		visit.innerText = 'View This Market'
		visit.setAttribute( 'type', 'submit' )
		// Fetch reverse geocode market data before rerouting
		/* visit.addEventListener( 'click', function( ) {
			reverseGeocode( new google.maps.Geocoder( ), market )
		} ) */
		this.expandView( market, extra, retract, view, offset )
	}
	
	// Open larger view frame to share additional info
	View.prototype.expandView = function( market, extra, retract, view, offset ) {
		this.offset = offset
		this.view = view
		view.addEventListener( 'click', function( ) {
			var open = document.getElementsByClassName( 'extra' )[ 0 ]
			if ( open ) {
				open.parentElement.firstChild.style.display = 'block'
				open.parentElement.removeChild( open )
			}
			reverseGeocode( new google.maps.Geocoder( ), market )
			view.style.display = 'none'
			offset.appendChild( extra )
		} )
		retract.addEventListener( 'click', function( ) {
			view.style.display = 'block'
			offset.removeChild( extra )
			offset.appendChild( view )
		} )
	}
	
}



