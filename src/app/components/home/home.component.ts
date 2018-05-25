import { Predictions } from './../../shared/models/Predictions';
import { environment } from './../../../environments/environment';
import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  public reviewText;

  public predictions: Predictions;

  constructor(public http: HttpClient) { }

  ngOnInit() {
  }

  search() {
    this.predictions = new Predictions();

    this.http.get(environment.api + "/cnn").subscribe(results => {
      this.predictions.cnn = results['prediction'];
    })

    this.http.get(environment.api + "/cnn").subscribe(results => {
      this.predictions.cnn = results['prediction'];
    })

    this.http.get(environment.api + "/cnn").subscribe(results => {
      this.predictions.cnn = results['prediction'];
    })
  }
}
