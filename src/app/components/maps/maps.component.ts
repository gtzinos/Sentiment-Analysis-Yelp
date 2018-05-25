import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-maps',
  templateUrl: './maps.component.html',
  styleUrls: ['./maps.component.css']
})
export class MapsComponent implements OnInit {

  title: string = 'Los Angeles Restaurants';

  lat: number = 51.678418;
  lng: number = 7.809007;

  coordinates: any[] = [
    {
      "lat": 51.678418,
      "lng": 7.809007
    },
    {
      "lat": 51.178418,
      "lng": 8.809007
    },
    {
      "lat": 53.678418,
      "lng": 7.009007
    }
  ]

  constructor() { }

  ngOnInit() {
  }

}
