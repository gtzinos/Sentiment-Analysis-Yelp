import { GraphDataConfiguration } from './../models/GraphDataConfiguration';
import { GraphConfiguration } from './../models/GraphConfiguration';
import { Injectable } from '@angular/core';
import { Chart } from 'chart.js';

@Injectable({
  providedIn: 'root',
})
export class GraphsService {

  constructor() { }

  getData(dataArray, graphDataConf: GraphDataConfiguration) {
    let labels = [];
    let graphsData = {};

    dataArray.forEach(dataItem => {
      labels.push(dataItem.id);

      graphDataConf.keys.forEach(conf => {
        if (!graphsData[conf]) {
          graphsData[conf] = [];
        }

        graphsData[conf].push(dataItem[conf]);
      })
    });

    return {
      graphsData: graphsData,
      labels: labels
    };
  }

  createChart(graphConf: GraphConfiguration, dataArray) {
    let data = this.getData(dataArray, graphConf.graphDataConfiguration);
    let graphsData = data.graphsData;
    let labels = data.labels;

    console.log(data);
    console.log(graphConf);
    var chartData = {
      labels: labels,
      datasets: [
        {
          "label": graphConf.chartLabel,
          "data": graphsData[graphConf.graphDataConfiguration.id],
          "backgroundColor": [
            "#F08080",
            "#696969",
            "#1fc8f8",
            "#76a346"
          ]
        }]
    };

    var chart = new Chart(
      graphConf.chartElement,
      {
        "type": graphConf.type,
        "data": chartData,
        "options": {
          scales: {
            yAxes: [{
              stacked: true
            }]
          }
        }
      }
    );
  }

}
