import { Component, OnInit, ViewChild } from '@angular/core';
import { MatTableDataSource, MatSort, MatPaginator } from '@angular/material';
import { environment } from '../../../../environments/environment';
import { RestaurantByGroups } from '../../../shared/models/RestaurantsByGroups';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-neighborhood',
  templateUrl: './neighborhood.component.html',
  styleUrls: ['./neighborhood.component.css']
})

export class NeighborhoodComponent implements OnInit {
  displayedColumns = ['neighborhood', 'restaurant', 'review_count', 'stars'];
  dataSource: MatTableDataSource<RestaurantByGroups>;

  displayedColumns2 = ['neighborhood', 'name', 'address', 'noise_level', 'stars', 'review_count'];
  dataSource2: MatTableDataSource<RestaurantByGroups>;

  constructor(public http: HttpClient) { }

  ngOnInit() {
    this.http.get(environment.api + "/best-restaurant-by-neighborhood").subscribe((restaurants: [RestaurantByGroups]) => {
      this.dataSource = new MatTableDataSource(restaurants);
    });

    this.http.get(environment.api + "/top10-quiet-restaurants").subscribe((restaurants: [RestaurantByGroups]) => {
      this.dataSource2 = new MatTableDataSource(restaurants);
    });
  }

}
