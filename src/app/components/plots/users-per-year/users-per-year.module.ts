import { ChartElementModule } from './../../../shared/components/chart-element/chart-element.module';
import { GraphsService } from './../../../shared/services/graphs.service';
import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UsersPerYearComponent } from './users-per-year.component';
import { RouterModule } from '@angular/router';

@NgModule({
  imports: [
    CommonModule, FormsModule,ChartElementModule,
    RouterModule.forChild([{ path: '', component: UsersPerYearComponent }])
  ],
  declarations: [UsersPerYearComponent],
  providers: [GraphsService]
})
export class UsersPerYearModule { }
