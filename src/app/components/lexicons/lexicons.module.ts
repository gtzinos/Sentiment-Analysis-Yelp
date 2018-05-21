import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LexiconsComponent } from './lexicons.component';
import { RouterModule } from '@angular/router';

@NgModule({
  imports: [
    CommonModule, FormsModule,
    RouterModule.forChild([{ path: '', component: LexiconsComponent }])
  ],
  declarations: [LexiconsComponent]
})
export class LexiconsModule { }
