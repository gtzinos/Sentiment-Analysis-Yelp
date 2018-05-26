import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-maps',
  templateUrl: './maps.component.html',
  styleUrls: ['./maps.component.css']
})
export class MapsComponent implements OnInit {

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

  constructor() { }

  ngOnInit() {
  }

}
