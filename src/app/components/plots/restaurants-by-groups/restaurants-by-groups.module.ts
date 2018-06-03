import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RestaurantsByGroupsComponent } from './restaurants-by-groups.component';
import { RouterModule } from '@angular/router';
import {MatSelectModule} from '@angular/material/select';


@NgModule({
  imports: [
    CommonModule, MatSelectModule,FormsModule, MatSelectModule,
    RouterModule.forChild([{ path: '', component: RestaurantsByGroupsComponent }])
  ],
  declarations: [RestaurantsByGroupsComponent]
})

export class RestaurantsByGroupsModule { }
