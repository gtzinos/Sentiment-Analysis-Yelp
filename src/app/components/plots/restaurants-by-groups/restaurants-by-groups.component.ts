import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../../environments/environment';
import { RestaurantByGroups } from '../../../shared/models/RestaurantsByGroups';
import { Chart } from 'chart.js'
import { MatSelectChange } from '@angular/material';


@Component({
  selector: 'app-restaurants-by-groups',
  templateUrl: './restaurants-by-groups.component.html',
  styleUrls: ['./restaurants-by-groups.component.css']
})
export class RestaurantsByGroupsComponent implements OnInit {

  @ViewChild("restaurantsByArea") restaurantsByArea: ElementRef<any>;
  @ViewChild("restaurantsByMeals") restaurantsByMeals: ElementRef<any>;
  @ViewChild("restaurantsByAmbience") restaurantsByAmbience: ElementRef<any>;
  @ViewChild("restaurantsByMusic") restaurantsByMusic: ElementRef<any>;
  @ViewChild("restaurantsByDay") restaurantsByDay: ElementRef<any>;
  @ViewChild("restaurantsBySmoking") restaurantsBySmoking: ElementRef<any>;


  neighborhood =[
    {value: 'Southeast', viewValue: 'Southeast'},
    {value: 'Spring Valley', viewValue: 'Spring Valley'},
    {value: 'Westside', viewValue: 'Westside'},
    {value: 'Eastside', viewValue: 'Eastside'},
    {value: 'Anthem', viewValue: 'Anthem'},
    {value: 'Centennial', viewValue: 'Centennial'},
    {value: 'Northwest', viewValue: 'Northwestcos'},
    {value: 'The Strip', viewValue: 'The Strip'},
    {value: 'Downtown', viewValue: 'Downtown'},
    {value: 'University', viewValue: 'University'},
    {value: 'South Summerlin', viewValue: 'South Summerlin'},
    {value: 'Chinatown', viewValue: 'Chinatown'},
    {value: 'Southwest', viewValue: 'Southwest'},
    {value: 'Summerlin', viewValue: 'Summerlin'},
    {value: 'The Lakes', viewValue: 'The Lakes'}
  ];

  constructor(public http: HttpClient) { }
  restaurantsBySmokingCanvas;

  ngOnInit() {
    let restaurantsByAreaCanvas = this.restaurantsByArea.nativeElement.getContext('2d');
    let restaurantsByMealsCanvas = this.restaurantsByMeals.nativeElement.getContext('2d');
    let restaurantsByAmbienceCanvas = this.restaurantsByAmbience.nativeElement.getContext('2d');
    let restaurantsByMusicCanvas = this.restaurantsByMusic.nativeElement.getContext('2d');
    let restaurantsByDayCanvas = this.restaurantsByDay.nativeElement.getContext('2d');

    this.restaurantsBySmokingCanvas = this.restaurantsBySmoking.nativeElement.getContext('2d');

    this.http.get(environment.api + "/restaurants-by-groups").subscribe((restaurants: [RestaurantByGroups]) => {
      let labels = [];
      let restaurantsCount = [];

      restaurants.forEach(restaurant => {
        restaurantsCount.push(restaurant.count);
        labels.push(restaurant.neighborhood);
      });

      this.createChart(labels, restaurantsCount, "Number of Restaurants By Neighborhood", restaurantsByAreaCanvas, "bar");
    });

    this.http.get(environment.api + "/restaurants-by-meals").subscribe((restaurants: [RestaurantByGroups]) => {
      let labels = [];
      let restaurantsCount = [];

      restaurants.forEach(restaurant => {
        restaurantsCount.push(restaurant.count);
        labels.push(restaurant.meal);
      });

      this.createChart(labels, restaurantsCount, "Number of Restaurants By Meal Type", restaurantsByMealsCanvas, "bar");
    });

    this.http.get(environment.api + "/restaurants-by-ambience").subscribe((restaurants: [RestaurantByGroups]) => {
      let labels = [];
      let restaurantsCount = [];

      restaurants.forEach(restaurant => {
        restaurantsCount.push(restaurant.count);
        labels.push(restaurant.ambience);
      });

      this.createChart(labels, restaurantsCount, "Number of Restaurants By Ambience Type", restaurantsByAmbienceCanvas, "bar");
    });

    this.http.get(environment.api + "/restaurants-by-music").subscribe((restaurants: [RestaurantByGroups]) => {
      let labels = [];
      let restaurantsCount = [];

      restaurants.forEach(restaurant => {
        restaurantsCount.push(restaurant.count);
        labels.push(restaurant.music);
      });

      this.createChart(labels, restaurantsCount, "Number of Restaurants By Music Type", restaurantsByMusicCanvas, "bar");
    });

    this.http.get(environment.api + "/restaurants-by-day").subscribe((restaurants: [RestaurantByGroups]) => {
      let labels = [];
      let restaurantsCount = [];

      restaurants.forEach(restaurant => {
        restaurantsCount.push(restaurant.count);
        labels.push(restaurant.day);
      });

      this.createChart(labels, restaurantsCount, "Number of Restaurants by Best Nights", restaurantsByDayCanvas, "bar");
    });
    
    this.getSmokingStats(this.neighborhood[0].value);
  }

  
  getSmokingStats(which){
    this.http.get(environment.api + "/smoking-by-neighborhood?neighborhood="+which).subscribe((restaurants: [RestaurantByGroups]) => {
      let labels = [];
      let restaurantsCount = [];

      restaurants.forEach(restaurant => {
        restaurantsCount.push(restaurant.count);
        labels.push(restaurant.type);
      });

      this.createChart(labels, restaurantsCount, "Smoking Stats by Neighborhood", this.restaurantsBySmokingCanvas, "doughnut");
    });
  }

  createChart(labels, data, chartLabel, chartElement, type = "line") {
    var chartData = {
      labels: labels,
      datasets: [
        {
          "label": chartLabel,
          "data": data,
          "backgroundColor": [
            "#F08080",
            "#696969",
            "#1fc8f8",
            "#76a346"
          ]
        }]
    };

    var chart = new Chart(
      chartElement,
      {
        "type": type,
        "data": chartData,
        "options": {
          scales: {
            yAxes: [{
              stacked: true
            }]
          }
        }
      }
    );
  }
}
