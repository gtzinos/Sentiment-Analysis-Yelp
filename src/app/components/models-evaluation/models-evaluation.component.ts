import { environment } from './../../../environments/environment';
import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { MatSnackBar } from '@angular/material';
import { Predictions } from '../../shared/models/Predictions';
import { GraphConfiguration } from '../../shared/models/GraphConfiguration';
import { GraphDataConfiguration } from '../../shared/models/GraphDataConfiguration';

@Component({
  selector: 'app-home',
  templateUrl: './models-evaluation.component.html',
  styleUrls: ['./models-evaluation.component.css']
})
export class ModelsEvaluationComponent implements OnInit {
  public metrics: any[] = [];
  public graphConfigurations = [];

  constructor(public http: HttpClient, public snackBar: MatSnackBar) {
  }

  ngOnInit() {
    this.http.get(environment.mlapi + "/metrics").subscribe((metrics: any[]) => {
      this.metrics = metrics;
      this.graphConfigurations.push(new GraphConfiguration("Models Accuracy", "bar", new GraphDataConfiguration("Accuracy")));
      this.graphConfigurations.push(new GraphConfiguration("Models Precision", "bar", new GraphDataConfiguration("Precision")));
      this.graphConfigurations.push(new GraphConfiguration("Models Recall", "bar", new GraphDataConfiguration("Recall")));
      this.graphConfigurations.push(new GraphConfiguration("Models F1", "bar", new GraphDataConfiguration("F1")));

    })
  }
}
