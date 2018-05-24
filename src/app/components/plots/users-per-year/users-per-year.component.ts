import { GraphConfiguration } from './../../../shared/models/GraphConfiguration';
import { GraphsService } from './../../../shared/services/graphs.service';
import { ReviewPerYear } from './../../../shared/models/ReviewPerYear';
import { HttpClient } from '@angular/common/http';
import { Component, OnInit, ViewChild, ElementRef, AfterViewInit } from '@angular/core';
import { Chart } from 'chart.js';
import { environment } from '../../../../environments/environment';
import { RestaurantByWifi } from '../../../shared/models/RestaurantByWifi';
import { GraphDataConfiguration } from '../../../shared/models/GraphDataConfiguration';

@Component({
  selector: 'app-users-per-year',
  templateUrl: './users-per-year.component.html',
  styleUrls: ['./users-per-year.component.css']
})
export class UsersPerYearComponent implements OnInit {

  @ViewChild("usersCountChart") usersCountChart: ElementRef<any>;

  constructor(public http: HttpClient, public graphService: GraphsService) { }

  ngOnInit() {
    let usersCountCanvas = this.usersCountChart.nativeElement.getContext('2d');

    this.http.get(environment.api + "/users-per-year").subscribe((users: [RestaurantByWifi]) => {

      let graphConfiguration = new GraphConfiguration("Number of Restaurants By Wifi", usersCountCanvas, "bar", new GraphDataConfiguration("count", ["count"]));

      this.graphService.createChart(graphConfiguration, users);
    })
  }


}
