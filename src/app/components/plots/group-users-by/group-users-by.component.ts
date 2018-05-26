import { GraphConfiguration } from './../../../shared/models/GraphConfiguration';
import { GraphsService } from './../../../shared/services/graphs.service';
import { ReviewPerYear } from './../../../shared/models/ReviewPerYear';
import { HttpClient } from '@angular/common/http';
import { Component, OnInit, ViewChild, ElementRef, AfterViewInit } from '@angular/core';
import { Chart } from 'chart.js';
import { environment } from '../../../../environments/environment';
import { RestaurantByWifi } from '../../../shared/models/RestaurantByWifi';
import { GraphDataConfiguration } from '../../../shared/models/GraphDataConfiguration';
import { UsersByYear } from '../../../shared/models/UsersByYear';

@Component({
  selector: 'app-group-users-by',
  templateUrl: './group-users-by.component.html',
  styleUrls: ['./group-users-by.component.css']
})
export class GroupUsersByComponent implements OnInit {
  public selectedGroup = "compliment_profile";
  public groups = [{
    id: "compliment_profile",
    text: "Compliment Profile"
  }, {
    id: "funny",
    text: "Funny"
  }, {
    id: "fans",
    text: "Fans"
  }, {
    id: "cool",
    text: "Cool"
  }]
  public graphConfigurations = [];
  public users = [];

  constructor(public http: HttpClient, public graphService: GraphsService) { }

  ngOnInit() {
    this.updatePlots();
  }

  updatePlots() {
    this.graphConfigurations = [];
    this.users = [];
    this.http.post(environment.api + "/group-users-by", {fieldName: this.selectedGroup}).subscribe((users: [UsersByYear]) => {

      this.graphConfigurations.push(new GraphConfiguration("Users By Year", "pie", new GraphDataConfiguration("count")));

      this.users = users;
    })
  }
}
