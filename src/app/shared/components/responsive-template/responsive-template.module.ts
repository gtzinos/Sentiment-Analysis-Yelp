import { CommonModule } from '@angular/common';
import { routes } from './responsive-template.routing';
import { RouterModule, Router } from '@angular/router';
import { NgModule } from "@angular/core";
import { ResponsiveTemplateComponent } from './responsive-template.component';

import {MatDividerModule} from '@angular/material/divider';
import { MatIconModule, MatToolbarModule } from '@angular/material';
import { MatListModule } from '@angular/material/list';
import { MediaMatcher } from '@angular/cdk/layout';
import { MatSidenavModule } from '@angular/material/sidenav';
import { FormsModule } from '@angular/forms';
import {MatExpansionModule} from '@angular/material/expansion';

@NgModule({
  imports: [
    RouterModule.forChild(routes), CommonModule, MatDividerModule, MatIconModule
    , MatToolbarModule,MatExpansionModule, MatListModule, MatSidenavModule, FormsModule
  ],
  declarations: [
    ResponsiveTemplateComponent
  ],
  exports: [
    ResponsiveTemplateComponent, RouterModule
  ],
  providers: [MediaMatcher]
})
export class ResponsiveTemplateModule {

}/*
RouterModule.forChild([{
  path: '', component: ResponsiveTemplateComponent, children: [
    { path: '', redirectTo: 'search', pathMatch: "full" },
    { path: 'search', loadChildren: "../../../components/search/search.module#SearchModule" },
    { path: 'upload', loadChildren: "../../../components/upload/upload.module#UploadModule" },
    { path: '**', redirectTo: 'search' }]
}]*/