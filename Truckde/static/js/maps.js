
var directionDisplay;
var map;

function initialize() {
    directionsDisplay = new google.maps.DirectionsRenderer();
    <!-- DirectionsRenderer() function draws the directions -->
    var tcc = new google.maps.LatLng(30.813187, 75.96298);
    var myOptions = {
        zoom:7,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
     <!-- for driving distance we will use ROADMAP as maptype -->
        center: tcc
     <!-- the center of the map should be tcc -->
    }
<!-- following lines initializes map object that would show in div id map_canvas-->
    map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
    directionsDisplay.setMap(map);
}

<!-- Maps initialization javascript code ends -->

<!-- Now we will calculate the distance between two points -->


var directionsService = new google.maps.DirectionsService();

function calcRoute() {
    var start = document.getElementById("start").value;
    var end = document.getElementById("end").value;

    var request = {
        origin:start,
        destination:end,
        travelMode: google.maps.DirectionsTravelMode.DRIVING
    };
    <!-- calling google maps API function route to show (highlight) the route from one place to another --> 
    directionsService.route(request, function(response, status) {
        if (status == google.maps.DirectionsStatus.OK) {
            directionsDisplay.setDirections(response);
<!-- This calculates the distance between two points-->
var distanceInput = document.getElementById("distance");
distanceInput.value = response.routes[0].legs[0].distance.value / 1000;
        
        }
    });
}

