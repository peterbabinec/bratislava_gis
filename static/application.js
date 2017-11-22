var lat, lon;

function searchGym() {
  var request = new XMLHttpRequest();
  request.open('GET', '/api/v1.0/fitness', true);
  
  request.onload = function () {
    if (request.status >= 200 && request.status < 400) {
      var gymData = JSON.parse(request.responseText);
      console.log(gymData);
      var myLayer = L.mapbox.featureLayer().addTo(map);
      myLayer.setGeoJSON(gymData);
    } else {
      alert("Load Error");
    }
  };
  
  request.onerror = function () {
    alert("Connection Error");
  };
  
  request.send();
}