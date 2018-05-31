import { environment } from './../../../environments/environment';
import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { MatSnackBar } from '@angular/material';
import { Predictions } from '../../shared/models/Predictions';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  public reviewText;
  public searchDisabled: boolean;

  public predictions: Predictions;

  constructor(public http: HttpClient, public snackBar: MatSnackBar) {
    this.predictions = new Predictions();
  }

  ngOnInit() {
  }

  search() {
    delete this.predictions.dnn;
    delete this.predictions.svm;
    delete this.predictions.nb;

    if (this.searchDisabled) {
      this.snackBar.open('Please wait to complete the previous request', "OK", { duration: 3000 });
    }
    else if (!this.reviewText) {
      this.snackBar.open('Empty term.', "OK", { duration: 3000 });
    }
    else {
      this.searchDisabled = true;

      let promises = [];

      promises.push(this.http.post(environment.mlapi + "/dnn", { term: this.reviewText }).toPromise());
      promises.push(this.http.post(environment.mlapi + "/svm", { term: this.reviewText }).toPromise());
      promises.push(this.http.post(environment.mlapi + "/nb", { term: this.reviewText }).toPromise());

      Promise.all(promises).then(results => {
        results.forEach(result => {
          this.predictions[result.algorithm] = result.prediction;
          console.log(this.predictions);
          console.log(result);
        });
        this.searchDisabled = false;
      }, error => {
        this.searchDisabled = false;
      })
    }

  }
}
