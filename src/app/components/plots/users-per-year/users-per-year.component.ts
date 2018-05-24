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
  selector: 'app-users-per-year',
  templateUrl: './users-per-year.component.html',
  styleUrls: ['./users-per-year.component.css']
})
export class UsersPerYearComponent implements OnInit {

  public graphConfigurations = [];
  public users = [];

  constructor(public http: HttpClient, public graphService: GraphsService) { }

  ngOnInit() {
    this.http.get(environment.api + "/users-per-year").subscribe((users: [UsersByYear]) => {

      this.graphConfigurations.push(new GraphConfiguration("Users By Year", "bar", new GraphDataConfiguration("count")));
      this.graphConfigurations.push(new GraphConfiguration("Average Stars By Year", "bar", new GraphDataConfiguration("average_stars")));
      this.graphConfigurations.push(new GraphConfiguration("Average compliment By Year", "bar", new GraphDataConfiguration("avg_compliment_cool")));
      this.graphConfigurations.push(new GraphConfiguration("Average compliment cute By Year", "bar", new GraphDataConfiguration("avg_compliment_cute")));
      this.graphConfigurations.push(new GraphConfiguration("Average compliment funny By Year", "bar", new GraphDataConfiguration("avg_compliment_funny")));
      this.graphConfigurations.push(new GraphConfiguration("Average compliment hot By Year", "bar", new GraphDataConfiguration("avg_compliment_hot")));
      this.graphConfigurations.push(new GraphConfiguration("Average compliment list By Year", "bar", new GraphDataConfiguration("avg_compliment_list")));
      this.graphConfigurations.push(new GraphConfiguration("Average compliment more By Year", "bar", new GraphDataConfiguration("avg_compliment_more")));
      this.graphConfigurations.push(new GraphConfiguration("Average compliment photos By Year", "bar", new GraphDataConfiguration("avg_compliment_photos")));
      this.graphConfigurations.push(new GraphConfiguration("Average compliment plain By Year", "bar", new GraphDataConfiguration("avg_compliment_plain")));
      this.graphConfigurations.push(new GraphConfiguration("Average compliment profile By Year", "bar", new GraphDataConfiguration("avg_compliment_profile")));
      this.graphConfigurations.push(new GraphConfiguration("Average compliment writer By Year", "bar", new GraphDataConfiguration("avg_compliment_writer")));
      this.graphConfigurations.push(new GraphConfiguration("Average cool By Year", "bar", new GraphDataConfiguration("avg_cool")));
      this.graphConfigurations.push(new GraphConfiguration("Average fans By Year", "bar", new GraphDataConfiguration("avg_fans")));
      this.graphConfigurations.push(new GraphConfiguration("Average funny By Year", "bar", new GraphDataConfiguration("avg_funny")));
      this.graphConfigurations.push(new GraphConfiguration("Average review count By Year", "bar", new GraphDataConfiguration("avg_review_count")));
      this.graphConfigurations.push(new GraphConfiguration("Average useful By Year", "bar", new GraphDataConfiguration("avg_useful")));
      this.graphConfigurations.push(new GraphConfiguration("Average cool By Year", "bar", new GraphDataConfiguration("compliment_cool")));
      this.graphConfigurations.push(new GraphConfiguration("Compliment cute By Year", "bar", new GraphDataConfiguration("compliment_cute")));
      this.graphConfigurations.push(new GraphConfiguration("Compliment funny By Year", "bar", new GraphDataConfiguration("compliment_funny")));
      this.graphConfigurations.push(new GraphConfiguration("Compliment hot By Year", "bar", new GraphDataConfiguration("compliment_hot")));
      this.graphConfigurations.push(new GraphConfiguration("Compliment list By Year", "bar", new GraphDataConfiguration("compliment_list")));
      this.graphConfigurations.push(new GraphConfiguration("Compliment more By Year", "bar", new GraphDataConfiguration("compliment_more")));
      this.graphConfigurations.push(new GraphConfiguration("Compliment note By Year", "bar", new GraphDataConfiguration("compliment_note")));
      this.graphConfigurations.push(new GraphConfiguration("Compliment photos By Year", "bar", new GraphDataConfiguration("compliment_photos")));
      this.graphConfigurations.push(new GraphConfiguration("Compliment plain By Year", "bar", new GraphDataConfiguration("compliment_plain")));
      this.graphConfigurations.push(new GraphConfiguration("Compliment profile By Year", "bar", new GraphDataConfiguration("compliment_profile")));
      this.graphConfigurations.push(new GraphConfiguration("Compliment writer By Year", "bar", new GraphDataConfiguration("compliment_writer")));
      this.graphConfigurations.push(new GraphConfiguration("Cool By Year", "bar", new GraphDataConfiguration("cool")));
      this.graphConfigurations.push(new GraphConfiguration("Count By Year", "bar", new GraphDataConfiguration("count")));
      this.graphConfigurations.push(new GraphConfiguration("Fans By Year", "bar", new GraphDataConfiguration("fans")));
      this.graphConfigurations.push(new GraphConfiguration("Funny By Year", "bar", new GraphDataConfiguration("funny")));
      this.graphConfigurations.push(new GraphConfiguration("Review Count By Year", "bar", new GraphDataConfiguration("review_count")));
      this.graphConfigurations.push(new GraphConfiguration("Useful By Year", "bar", new GraphDataConfiguration("useful")));

      this.users = users;
    })
  }
}
