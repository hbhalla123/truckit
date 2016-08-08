$(function(){
$(".actions>ul li:nth-child(2) a").click( function(){
calcRoute();
$.ajax({
type:'GET',
url:'vehicle_info',
success: function(data){
var distanceInput = document.getElementById("distance");
console.log(distanceInput.innerHTML);



var money = document.getElementById("order_fare");
var id= document.getElementById("options").value;
console.log(data[id-1].fields.vehicle_price);
money.value =  data[id-1].fields.vehicle_price*distanceInput.innerHTML;
document.getElementById("start1a").innerHTML = "source" + " " + ":" + document.getElementById("source").value;
document.getElementById("end1a").innerHTML = "Destination" + " " + ":" + document.getElementById("destination").value;
document.getElementById("pickdate").innerHTML = "Pick up date" + " " + ":" + document.getElementById("delivery_date").value;
document.getElementById("picktime").innerHTML = "Pick up time" + " " + ":" + document.getElementById("delivery_type").value;
var e = document.getElementById("options");
var option = e.options[e.selectedIndex].text;
document.getElementById("trucktype").innerHTML = "vehicle" + " " + ":" + option;
},
error: function(){
alert(' error loading data ');

}
});
});
});


/*
$(function(){
$(".actions>ul li:nth-child(3) a").click( function(){
var money1=document.getElementById("order_fare").innerHTML;
$.ajax({
type:'POST',
url:'price',
data:{"truckorder":delivery_date,"money":money1,csrfmiddlewaretoken:'{{csrf_token}}'},
success: function(data){

console.log("hii");

		},
error: function(){
alert(' error loading data ');
}
	});
});
});

*/