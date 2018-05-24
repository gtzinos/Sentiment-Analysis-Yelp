import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RestaurantsByWifiComponent } from './restaurants-by-wifi.component';
import { RouterModule } from '@angular/router';

@NgModule({
  imports: [
    CommonModule, FormsModule,
    RouterModule.forChild([{ path: '', component: RestaurantsByWifiComponent }])
  ],
  declarations: [RestaurantsByWifiComponent]
})
export class RestaurantsByWifiModule { }
