import { MatInputModule } from '@angular/material';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './home.component';
import { RouterModule } from '@angular/router';
import { MatCardModule } from '@angular/material/card';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatDividerModule } from '@angular/material/divider';
import { MatListModule } from '@angular/material/list';
import {MatSnackBarModule} from '@angular/material/snack-bar';

@NgModule({
  imports: [
    CommonModule, MatInputModule,MatSnackBarModule, MatDividerModule, MatListModule, ReactiveFormsModule, FormsModule, MatCardModule,
    RouterModule.forChild([{ path: '', component: HomeComponent }])
  ],
  declarations: [HomeComponent]
})
export class HomeModule { }
