import { CommonModule } from '@angular/common';
import { routes } from './sidenav.routing';
import { RouterModule } from '@angular/router';
import { NgModule } from "@angular/core";
import { SidenavComponent } from './sidenav.component';

@NgModule({
  imports: [
    RouterModule.forRoot(routes), CommonModule
  ],
  declarations: [
    SidenavComponent
  ],
  exports: [
    SidenavComponent
  ]
})
export class SideNavModule {

}
