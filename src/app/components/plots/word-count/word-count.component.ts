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
  selector: 'app-word-count',
  templateUrl: './word-count.component.html',
  styleUrls: ['./word-count.component.css']
})
export class WordCountComponent implements OnInit {

  public graphConfigurations = [];
  public users = [];

  constructor(public http: HttpClient, public graphService: GraphsService) { }

  ngOnInit() {
    this.http.get(environment.api + "/top-words").subscribe((users: [UsersByYear]) => {

      this.users = users;
    })
  }
}
