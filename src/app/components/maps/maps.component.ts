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

  title1="test"
  title2="test"
  title3="test"
  title4="test"
  title5="test"
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
