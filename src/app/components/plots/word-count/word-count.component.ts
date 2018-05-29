import { TopWords } from './../../../shared/models/TopWords';
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
import * as d3 from 'd3';
import { DEFAULT_RESIZE_TIME } from '@angular/cdk/scrolling';
import * as m from './d3-layout.js';

@Component({
  selector: 'app-word-count',
  templateUrl: './word-count.component.html',
  styleUrls: ['./word-count.component.css']
})
export class WordCountComponent implements OnInit {

  public graphConfigurations = [];
  public words: [TopWords];
  public layout;

  constructor(public http: HttpClient, public graphService: GraphsService) { }

  ngOnInit() {
    this.http.get(environment.api + "/top-words").subscribe((words: [TopWords]) => {

      this.words = words['message'];

      this.setGraph();
    })
  }

  setGraph() {
    this.layout = m()
      .words(this.words.map(word => {
        word.frequency *= 2;
        return { text: word.id, size: word.frequency };
      }))
      .padding(1)
      .rotate(function () { return ~~(Math.random() * 2) * 90; })
      .font("Impact")
      .fontSize(function (d) {
        return d.size;
      })
      .on("end", this.draw);

    this.layout.start();
  }

  draw(words) {
    d3.select(".word-frequency").append("svg")
      .attr("width", m().size()[0])
      .attr("height", m().size()[1])
      .append("g")
      .attr("transform", "translate(" + m().size()[0] / 2 + "," + m().size()[1] / 2 + ")")
      .selectAll("text")
      .data(words)
      .enter().append("text")
      .style("font-size", function (d: any) { return d.size + "px"; })
      .style("font-family", "Impact")
      .attr("text-anchor", "middle")
      .attr("transform", function (d: any) {
        return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
      })
      .text(function (d: any) { return d.text; });
  }
}
