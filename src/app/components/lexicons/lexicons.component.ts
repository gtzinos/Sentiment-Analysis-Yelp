import { Component, OnInit, ViewChild, ElementRef, AfterViewInit } from '@angular/core';
import { Chart } from 'chart.js';

@Component({
  selector: 'app-lexicons',
  templateUrl: './lexicons.component.html',
  styleUrls: ['./lexicons.component.css']
})
export class LexiconsComponent implements AfterViewInit {

  @ViewChild("myChart") mychart: ElementRef<any>;

  public chartObj;
  public chartContext;
  public chartBody;

  // Somewhere under the class constructor we want to wait for our view
  // to initialize

  ngAfterViewInit(): void {
    let chartElement = this.mychart.nativeElement.getContext('2d');

    var data = {
      labels: [
        "Value A",
        "Value B"
      ],
      datasets: [
        {
          "data": [101342, 55342],   // Example data
          "backgroundColor": [
            "#1fc8f8",
            "#76a346"
          ]
        }]
    };

    var chart = new Chart(
      chartElement,
      {
        "type": 'doughnut',
        "data": data,
        "options": {
          "cutoutPercentage": 50,
        }
      }
    );


  }

}
