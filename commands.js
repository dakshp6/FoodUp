window.onload = function(){
    document.getElementById("button").addEventListener("click",random);

    
}

function random(){
    document.getElementById("par1").innerHTML="Hello";
getLocation();

}


function getLocation() {

    if(navigator.geolocation){
navigator.geolocation.getCurrentPosition(geoSuccess, geoError);
        } else {
            alert("Geolocation is not supported by this browser.");
        }
    }
    



function geoSuccess(position) {
    var lat = position.coords.latitude;
    var lng = position.coords.longitude;
    SendPar(lat,lng);
    alert("lat:" + lat + " lng:" + lng);
}



function geoError() {
    alert("Geocoder failed.");
}



function SendPar(lat,long){
    alert(lat+ " hi "+long);
const options = {
    method: 'POST' ,
    headers: {
    'Content-Type': 'application/json'
    }
    
};
fetch('https://foodup-ugahacks.herokuapp.com/filldb?radius=15000&lat='+ lat.toString() + "&lng="+ long.toString(), options);
 








/* var http = new XMLHttpRequest();
var url = 'https://foodup-ugahacks.herokuapp.com/filldb?raduis=15000&lat='+ lat.toString() + "&lng="+ long.toString();





http.open('POST', url, true);

http.send();

fetch('https://foodup-ugahacks.herokuapp.com/random').then(function (response) {
	// The API call was successful!
	alert('success!', response);
}).catch(function (err) {
	// There was an error
	alert('Something went wrong.', err);
});
 */
}


