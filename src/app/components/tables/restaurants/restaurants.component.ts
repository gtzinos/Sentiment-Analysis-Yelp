import { Component, OnInit, ViewChild } from '@angular/core';
import { MatTableDataSource, MatSort, MatPaginator } from '@angular/material';
import { environment } from '../../../../environments/environment';
import { Restaurant } from '../../../shared/models/Restaurant';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-table',
  templateUrl: './restaurants.component.html',
  styleUrls: ['./restaurants.component.css']
})
export class RestaurantsComponent implements OnInit {
  displayedColumns = ['name', 'city', 'stars', 'review_count'];
  dataSource: MatTableDataSource<Restaurant>;

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(public http: HttpClient) {
  }

  ngOnInit() {
    this.http.get(environment.api + "/restaurants").subscribe((restaurants: [Restaurant]) => {
      this.dataSource = new MatTableDataSource(restaurants);
      this.dataSource.paginator = this.paginator;
      this.dataSource.sort = this.sort;
    })
  }

  applyFilter(filterValue: string) {
    filterValue = filterValue.trim(); // Remove whitespace
    filterValue = filterValue.toLowerCase(); // Datasource defaults to lowercase matches
    this.dataSource.filter = filterValue;
  }
}
