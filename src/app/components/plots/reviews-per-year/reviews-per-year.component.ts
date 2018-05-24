import { ReviewPerYear } from './../../../shared/models/ReviewPerYear';
import { HttpClient } from '@angular/common/http';
import { Component, OnInit, ViewChild, ElementRef, AfterViewInit } from '@angular/core';
import { Chart } from 'chart.js';
import { environment } from '../../../../environments/environment';

@Component({
  selector: 'app-reviews-per-year',
  templateUrl: './reviews-per-year.component.html',
  styleUrls: ['./reviews-per-year.component.css']
})
export class ReviewsPerYearComponent implements OnInit {

  @ViewChild("reviewsPerYear") reviewsPerYearChart: ElementRef<any>;
  @ViewChild("usefulPerYear") usefulPerYearChart: ElementRef<any>;

  constructor(public http: HttpClient) { }

  ngOnInit() {
    let reviewsPerYearCanvas = this.reviewsPerYearChart.nativeElement.getContext('2d');
    let usefulPerYearCanvas = this.usefulPerYearChart.nativeElement.getContext('2d');

    this.http.get(environment.api + "/reviews-per-year").subscribe((reviews: [ReviewPerYear]) => {
      let labels = [];
      let reviewsPerYear: { x: number, y: number }[] = [];
      let usefulPerYear = [];

      reviews.forEach(review => {
        reviewsPerYear.push({ x: review.id, y: review.count });
        usefulPerYear.push({ x: review.id, y: review.useful });
        labels.push(review.id);
      });

      this.createChart(labels, reviewsPerYear, "Number of Reviews Per Year", reviewsPerYearCanvas);
      this.createChart(labels, usefulPerYear, "Useful Reviews Per Year", usefulPerYearCanvas);
    })
  }

  createChart(labels, data, chartLabel, chartElement) {
    var chartData = {
      labels: labels,
      datasets: [
        {
          "label": chartLabel,
          "data": data,
          "backgroundColor": [
            "#1fc8f8",
            "#76a346"
          ]
        }]
    };

    var chart = new Chart(
      chartElement,
      {
        "type": 'line',
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
