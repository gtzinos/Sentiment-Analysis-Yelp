import { SideNavModule } from './sidenav/sidenav.module';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { SidenavComponent } from './sidenav/sidenav.component';

@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    BrowserModule,SideNavModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

