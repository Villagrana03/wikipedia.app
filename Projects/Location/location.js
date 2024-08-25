/*  JavaScript 6th Edition
    Chapter 10
    Hands-on Project 10-3

    Author: 
    Date:   

    Filename: script.js
*/


//here i set the variable of the map

let map;
let mapBtn = document.getElementById("mapBtn");
let mapRio;
let mapParis;
let mapBeijing;


//This function is called when the geolocation request is successful. It takes one parameter, position, which is an object containing the geographical position of the device. Inside the function:
//It extracts the latitude and longitude coordinates from the position object using position.coords.latitude and position.coords.longitude

const success = (position) => {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    initMap(latitude, longitude);
}


//This function is called when the geolocation request fails or the user denies permission. Inside the function: It sets the inner HTML of the map element to display a message indicating that the connection failed.
const fail = () => {
    map.innerHTML = 'Your connection failed';
}


// This function initiates the process of requesting the user's current location. Inside the function: It first checks if the navigator.geolocation object is available in the browser. If it exists, it means that geolocation services are supported. If geolocation is supported, it calls navigator.geolocation.getCurrentPosition() to initiate the process of obtaining the user's current position. It passes the success and fail functions as arguments to handle the success and failure scenarios, respectively.

const askForLocation = () => {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(success, fail);
    } else {
        map.innerHTML = "location was not able to get.";
    }
}

// The next 4 functions are a google API 

async function initMap(latitude, longitude) {
    const { Map } = await google.maps.importLibrary("maps");

    map = new Map(document.getElementById("map"), {
        center: { lat: latitude, lng: longitude },
        zoom: 8,
    });
}

async function initMapRio() {
    const { Map } = await google.maps.importLibrary("maps");

    mapRio = new Map(document.getElementById("map"), {
        center: { lat: 22.906, lng: 43.172 },
        zoom: 8,
    });
    caption.innerHTML = "Rio de Janeiro location"
}

async function initMapParis() {
    const { Map } = await google.maps.importLibrary("maps");

    mapParis = new Map(document.getElementById("map"), {
        center: { lat: 48.857, lng: 2.351},
        zoom: 8,
    });
    caption.innerHTML = "Paris location"
}

async function initMapBeijing() {
    const { Map } = await google.maps.importLibrary("maps");

    mapBeijing = new Map(document.getElementById("map"), {
        center: { lat: 39.904, lng: 116.407},
        zoom: 8,
    });
    caption.innerHTML = "Beijing location"
}



//getting the 3 cities
let beijing = document.getElementById("beijing");
let paris = document.getElementById("paris");
let rio = document.getElementById("rio");

//calling the citis once the button is being clicked
rio.addEventListener("click", initMapRio);
paris.addEventListener("click", initMapParis);
beijing.addEventListener("click", initMapBeijing);
mapBtn.addEventListener("click", askForLocation);








