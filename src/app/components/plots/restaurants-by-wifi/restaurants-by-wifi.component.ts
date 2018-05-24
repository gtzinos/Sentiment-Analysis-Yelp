import { ReviewPerYear } from './../../../shared/models/ReviewPerYear';
import { HttpClient } from '@angular/common/http';
import { Component, OnInit, ViewChild, ElementRef, AfterViewInit } from '@angular/core';
import { Chart } from 'chart.js';
import { environment } from '../../../../environments/environment';
import { RestaurantByWifi } from '../../../shared/models/RestaurantByWifi';

@Component({
  selector: 'app-restaurants-by-wifi',
  templateUrl: './restaurants-by-wifi.component.html',
  styleUrls: ['./restaurants-by-wifi.component.css']
})
export class RestaurantsByWifiComponent implements OnInit {

  @ViewChild("restaurantsCountChart") restaurantsCountChart: ElementRef<any>;
  @ViewChild("reviewCount") reviewCountChart: ElementRef<any>;
  @ViewChild("avgReviewCount") avgReviewCountChart: ElementRef<any>;
  @ViewChild("starsCount") starsCountChart: ElementRef<any>;
  @ViewChild("avgStarsCount") avgStarsCountChart: ElementRef<any>;

  constructor(public http: HttpClient) { }

  ngOnInit() {
    let restaurantsCountCanvas = this.restaurantsCountChart.nativeElement.getContext('2d');
    let reviewCountCanvas = this.reviewCountChart.nativeElement.getContext('2d');
    let avgReviewCountCanvas = this.avgReviewCountChart.nativeElement.getContext('2d');
    let starsCountCanvas = this.starsCountChart.nativeElement.getContext('2d');
    let avgStarsCountCanvas = this.avgStarsCountChart.nativeElement.getContext('2d');

    this.http.get(environment.api + "/restaurants-by-wifi").subscribe((restaurants: [RestaurantByWifi]) => {
      let labels = [];
      let restaurantsCount = [];

      let reviewCount = [];
      let avgReviewCount = [];

      let starsCount = [];
      let avgStarsCount = [];

      restaurants.forEach(restaurant => {
        restaurantsCount.push(restaurant.count);
        reviewCount.push(restaurant.review_count);
        avgReviewCount.push(restaurant.avg_review_count);
        starsCount.push(restaurant.stars);
        avgStarsCount.push(restaurant.avg_stars);
        labels.push(restaurant.id);
      });

      this.createChart(labels, restaurantsCount, "Number of Restaurants By Wifi", restaurantsCountCanvas, "bar");
      this.createChart(labels, reviewCount, "Review count of Restaurants By Wifi", reviewCountCanvas, "bar");
      this.createChart(labels, avgReviewCount, "AVG Review count of Restaurants By Wifi", avgReviewCountCanvas, "bar");
      this.createChart(labels, starsCount, "Restaurants stars By Wifi", starsCountCanvas, "bar");
      this.createChart(labels, avgStarsCount, "Restaurants avg stars By Wifi", avgStarsCountCanvas, "bar");
    })
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
