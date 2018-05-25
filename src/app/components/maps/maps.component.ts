import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-maps',
  templateUrl: './maps.component.html',
  styleUrls: ['./maps.component.css']
})
export class MapsComponent implements OnInit {

  title: string = 'Los Angeles Restaurants';

  lat: number = 34.0201613;
  lng: number = -118.6919205;

  coordinates: any[] = [
    {
      "label":"test",
      "lat": 34.1201613,
      "lng": -118.0919205
    },
    {
      "label":"test",
      "lat": 33.9201613,
      "lng": -118.9919205
    },
    {
      "label":"test",
      "lat": 34.5201613,
      "lng": -117.6919205
    }
  ]

  constructor() { }

  ngOnInit() {
  }

}
