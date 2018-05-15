import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReviewsComponent } from './reviews.component';
import { RouterModule } from '@angular/router';
import {MatCardModule} from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { ChartsModule } from 'ng2-charts/ng2-charts'
import { Chart } from 'chart.js'

@NgModule({
  imports: [
    CommonModule,MatIconModule,MatCardModule, FormsModule, MatButtonModule,
    RouterModule.forChild([{path: '', component: ReviewsComponent}]),
    ChartsModule
  ],
  declarations: [ReviewsComponent]
})
export class ReviewsModule { }
