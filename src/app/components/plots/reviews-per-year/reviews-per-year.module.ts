import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReviewsPerYearComponent } from './reviews-per-year.component';
import { RouterModule } from '@angular/router';

@NgModule({
  imports: [
    CommonModule, FormsModule,
    RouterModule.forChild([{ path: '', component: ReviewsPerYearComponent }])
  ],
  declarations: [ReviewsPerYearComponent]
})
export class ReviewsPerYearModule { }
