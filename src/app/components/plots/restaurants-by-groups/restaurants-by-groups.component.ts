import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../../environments/environment';
import { RestaurantByGroups } from '../../../shared/models/RestaurantsByGroups';
import {Chart} from 'chart.js'

@Component({
  selector: 'app-restaurants-by-groups',
  templateUrl: './restaurants-by-groups.component.html',
  styleUrls: ['./restaurants-by-groups.component.css']
})
export class RestaurantsByGroupsComponent implements OnInit {

  @ViewChild("restaurantsByArea") restaurantsByArea: ElementRef<any>;

  constructor(public http: HttpClient) { }

  ngOnInit() {
    let restaurantsByAreaCanvas = this.restaurantsByArea.nativeElement.getContext('2d');

    this.http.get(environment.api + "/restaurants-by-groups").subscribe((restaurants: [RestaurantByGroups]) => {
        let labels = [];
        let restaurantsCount = [];

        restaurants.forEach(restaurant => {
          restaurantsCount.push(restaurant.count);
          labels.push(restaurant.neighborhood);
        });


        this.createChart(labels, restaurantsCount, "Number of Restaurants By Neighborhood", restaurantsByAreaCanvas, "bar");
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
