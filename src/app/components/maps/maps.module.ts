import { CommonModule } from '@angular/common';
import { MapsComponent } from './maps.component';
import { RouterModule } from '@angular/router';
<<<<<<< HEAD
import { FormsModule } from '@angular/forms'
=======
import { NgModule, ApplicationRef } from '@angular/core';
import { FormsModule } from '@angular/forms';
>>>>>>> febfe52b6b84eb2b2290a78ee06e9945bb35a76c

import { AgmCoreModule } from '@agm/core';
@NgModule({
  imports: [
    CommonModule,FormsModule,
<<<<<<< HEAD
    RouterModule.forChild([{path: '', component: MapsComponent}])
=======
    RouterModule.forChild([{path: '', component: MapsComponent}]),
    AgmCoreModule.forRoot({
      apiKey: 'AIzaSyB32E-_zcqUHqw4QZ07ZflxDVElGUZ033I'
    })
>>>>>>> febfe52b6b84eb2b2290a78ee06e9945bb35a76c
  ],
  declarations: [MapsComponent]
})
export class MapsModule { }
