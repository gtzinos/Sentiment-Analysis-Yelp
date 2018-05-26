import { ChartElementModule } from './../../../shared/components/chart-element/chart-element.module';
import { GraphsService } from './../../../shared/services/graphs.service';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { GroupUsersByComponent } from './group-users-by.component';
import { RouterModule } from '@angular/router';
import {MatSelectModule} from '@angular/material/select';

@NgModule({
  imports: [
    CommonModule,MatSelectModule, FormsModule,ChartElementModule,ReactiveFormsModule,
    RouterModule.forChild([{ path: '', component: GroupUsersByComponent }])
  ],
  declarations: [GroupUsersByComponent],
  providers: [GraphsService]
})
export class GroupUsersByModule { }
