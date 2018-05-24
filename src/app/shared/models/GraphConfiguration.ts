import { GraphDataConfiguration } from './GraphDataConfiguration';
export class GraphConfiguration {
  chartLabel: string;
  chartElement: CanvasRenderingContext2D;
  type: string;
  graphDataConfiguration: GraphDataConfiguration;

  constructor(chartLabel: string, chartElement: CanvasRenderingContext2D,
    type: string, graphDataConfiguration: GraphDataConfiguration) {
      this.chartLabel = chartLabel;
      this.type = type;
      this.chartElement = chartElement;
      this.graphDataConfiguration = graphDataConfiguration;
    }
}
