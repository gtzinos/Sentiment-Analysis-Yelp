import { Component, OnInit } from '@angular/core';
import { ViewChild } from '@angular/core';
import { } from '@types/googlemaps';

@Component({
  selector: 'app-maps',
  templateUrl: './maps.component.html',
  styleUrls: ['./maps.component.css']
})
export class MapsComponent implements OnInit {

<<<<<<< HEAD
  @ViewChild('gmap') gmapElement: any;
  map: google.maps.Map;


  latitude: any;
  longitude: any;

  iconBase = 'https://maps.google.com/mapfiles/kml/shapes/';

  markerTypes = [
    {
      text: "Parking", value: "parking_lot_maps.png"
    }
    // ,
    // {
    //   text: "Library", value: "library_maps.png"
    // },
    // {
    //   text: "Information", value: "info-i_maps.png"
    // }
  ];

  selectedMarkerType: string = "parking_lot_maps.png";
=======
  title: string = 'Some of Los Angeles Restaurants';

  lat: number = 34.0201613;
  lng: number = -118.6919205;

  title1="5 stars restaurants"
  title2="Has free WiFi"
  title3="Suitable for kids"
  title4="Accepts credid card for payment"
  title5="Noise level: quiet"
  title6="Restaurants with outdor seating"
  title7="Reastaurants with delivery suport"
  title8="Restaurants with free WiFi and TV"
  title9="Wheel chair accessible restaurants with outdor seating"
  title10="Restaurants which accepts reservation and credid card for payment"
  
  coordinates: any[] = [
    {
      "label":"test",
      "stars":4.7,
      "lat": 34.1201613,
      "lng": -118.0919205
    },
    {
      "label":"test",
      "stars":5,
      "lat": 33.9201613,
      "lng": -118.9919205
    },
    {
      "label":"test",
      "stars":4.5,
      "lat": 34.5201613,
      "lng": -117.6919205
    },
    {
      "label":"test",
      "stars":3.8,
      "lat": 34.5901613,
      "lng": -117.3519205
    }
  ]
>>>>>>> febfe52b6b84eb2b2290a78ee06e9945bb35a76c

  constructor() { }

  ngOnInit() {
    var mapProp = {
      center: new google.maps.LatLng(18.5793, 73.8143),
      zoom: 15,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    this.map = new google.maps.Map(this.gmapElement.nativeElement, mapProp);
  }

  setMapType(mapTypeId: string) {
    this.map.setMapTypeId(mapTypeId)
  }

  setCenter() {
    this.map.setCenter(new google.maps.LatLng(this.latitude, this.longitude));

    let location = new google.maps.LatLng(this.latitude, this.longitude);

    let marker = new google.maps.Marker({
      position: location,
      map: this.map,
      title: 'Got you!'
    });

    marker.addListener('click', this.simpleMarkerHandler);

    marker.addListener('click', () => {
      this.markerHandler(marker);
    });
  }

  simpleMarkerHandler() {
    alert('Simple Component\'s function...');
  }

  markerHandler(marker: google.maps.Marker) {
    alert('Marker\'s Title: ' + marker.getTitle());
  }

  showCustomMarker() {


    this.map.setCenter(new google.maps.LatLng(this.latitude, this.longitude));

    let location = new google.maps.LatLng(this.latitude, this.longitude);

    console.log(`selected marker: ${this.selectedMarkerType}`);
    
    let marker = new google.maps.Marker({
      position: location,
      map: this.map,
      icon: this.iconBase + this.selectedMarkerType,
      title: 'Got you!'
    });

  }
  
}
