import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RestaurantsByGroupsComponent } from './restaurants-by-groups.component';
import { RouterModule } from '@angular/router';

@NgModule({
  imports: [
    CommonModule, FormsModule,
    RouterModule.forChild([{ path: '', component: RestaurantsByGroupsComponent }])
  ],
  declarations: [RestaurantsByGroupsComponent]
})
export class RestaurantsByGroupsModule { }
