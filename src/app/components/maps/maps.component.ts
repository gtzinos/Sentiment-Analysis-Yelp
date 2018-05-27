import { Component, OnInit, Attribute } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';

@Component({
  selector: 'app-maps',
  templateUrl: './maps.component.html',
  styleUrls: ['./maps.component.css']
})
export class MapsComponent implements OnInit {

  numOfPins = [
    {value: '100', viewValue: '100'},
    {value: '200', viewValue: '200'},
    {value: '0', viewValue: 'All'}
  ];
  selectedPins='100';

  numOfStars=[
    {value: '1', viewValue: 'Up to 1 Star'},
    {value: '2', viewValue: 'Up to 2 Stars'},
    {value: '3', viewValue: 'Up to 3 Stars'},
    {value: '4', viewValue: 'Up to 4 Stars'},
    {value: '5', viewValue: 'All'}
  ];
  
  selectedStars='5';

  title: string = 'Some of Las Vegas Restaurants';
  subtitle:string="Results are limited to 200 restaurants"
  public mapData:any;
  lat: number = 36.175585;
  lng: number = -115.199071;
  zoom:number = 11;

  constructor(public http: HttpClient) { }

  ngOnInit() {
    this.getAllRestaurants()
  }


  getAllRestaurants(){
    this.http.get(environment.api+"/maps?limit="+this.selectedPins).subscribe(data=>{
      this.mapData=data;
    })
  }

  getFiveStarsRestaurants(){
    this.http.get(environment.api+"/maps/5stars").subscribe(data=>{
      this.mapData=data;
    })
  }

  getWifi(){
    this.http.get(environment.api+"/maps/wifi?stars="+this.selectedStars+'&limit='+this.selectedPins).subscribe(data=>{
      this.mapData=data;
    })
  }

  getWifiAndTv(){
    this.http.get(environment.api+"/maps/wifi_tv?stars="+this.selectedStars+'&limit='+this.selectedPins).subscribe(data=>{
      this.mapData=data;
    })
  }

  getGfkAndHhAndOs(){
    this.http.get(environment.api+"/maps/gfk_hh_os?stars="+this.selectedStars+'&limit='+this.selectedPins).subscribe(data=>{
      this.mapData=data;
    })
  }

  getCreditCardAndReservations(){
    this.http.get(environment.api+"/maps/credit_and_reservations").subscribe(data=>{
      this.mapData=data;
    })
  }

}
