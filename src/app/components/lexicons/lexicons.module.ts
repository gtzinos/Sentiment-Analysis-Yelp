import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LexiconsComponent } from './lexicons.component';
import { RouterModule } from '@angular/router';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatTableModule } from '@angular/material/table';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatSortModule } from '@angular/material/sort';
import { MatInputModule, MatTooltipModule, MatToolbarModule } from '@angular/material';

@NgModule({
  imports: [
    CommonModule, MatIconModule, MatToolbarModule, MatSortModule, MatInputModule, MatTooltipModule, MatPaginatorModule, MatTableModule, FormsModule, MatButtonModule,
    RouterModule.forChild([{ path: '', component: LexiconsComponent }])
  ],
  declarations: [LexiconsComponent]
})
export class LexiconsModule { }
