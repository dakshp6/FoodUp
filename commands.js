window.onload = function(){
    document.getElementById("button").addEventListener("click",random);
    getLocation();
}

function random(){
var ran =fetch('https://foodup-ugahacks.herokuapp.com/random');
    document.getElementById("par1").innerHTML= ran;
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
    alert("lat:" + lat + " lng:" + lng);
    codeLatLng(lat, lng);
    SendPar(lat,lng);
}



function geoError() {
    alert("Geocoder failed.");
}



function SendPar(lat,long){
    alert(lat+ " hi "+long);

    var xhr = new XMLHttpRequest();

    xhr.open('POST', 'https://foodup-ugahacks.herokuapp.com/filldb?radius=15000&lat='+lat.toString()+'&lng='+long.toString());

    xhr.send();

}

