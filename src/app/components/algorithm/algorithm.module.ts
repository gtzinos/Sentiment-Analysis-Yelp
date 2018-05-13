import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AlgorithmComponent } from './algorithm.component';
import { RouterModule } from '@angular/router';
import {MatCardModule} from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';

@NgModule({
  imports: [
    CommonModule,MatIconModule,MatCardModule, FormsModule, MatButtonModule,
    RouterModule.forChild([{path: '', component: AlgorithmComponent}])
  ],
  declarations: [AlgorithmComponent]
})
export class AlgorithmModule { }
