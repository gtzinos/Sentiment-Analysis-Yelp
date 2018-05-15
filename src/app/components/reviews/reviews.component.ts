import { Component, OnInit, ElementRef } from '@angular/core';

@Component({
  selector: 'app-reviews',
  templateUrl: './reviews.component.html',
  styleUrls: ['./reviews.component.css']
})
export class ReviewsComponent implements OnInit {

  public pieChartLabels:string[] 
  public pieChartData:number[] 
  public pieChartType:string = 'pie';
  
  constructor(private elementRef: ElementRef) { }

  ngOnInit() {

    console.log("ngOnInit")

    this.pieChartLabels= ['Download Sales', 'In-Store Sales', 'Mail Sales'];
    this.pieChartData = [300, 500, 100];
    this.pieChartType = 'pie';
  }

  // Pie
  
 
 
  // events
  public chartClicked(e:any):void {
    console.log(e);
  }
 
  public chartHovered(e:any):void {
    console.log(e);
  }
}
