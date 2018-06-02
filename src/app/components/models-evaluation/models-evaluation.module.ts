import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ModelsEvaluationComponent } from './models-evaluation.component';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import {MatSnackBarModule} from '@angular/material/snack-bar';
import { ChartElementModule } from '../../shared/components/chart-element/chart-element.module';
import { GraphsService } from '../../shared/services/graphs.service';

@NgModule({
  imports: [
    CommonModule,MatSnackBarModule, ChartElementModule, ReactiveFormsModule, FormsModule,
    RouterModule.forChild([{ path: '', component: ModelsEvaluationComponent }])
  ],
  declarations: [ModelsEvaluationComponent],
  providers: [GraphsService]
})
export class ModelsEvaluationModule { }
