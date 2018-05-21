import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppComponent } from './app.component';
import { RouterModule } from '@angular/router';
import { FwordsComponent } from './components/fwords/fwords.component';
import { ReviewsComponent } from './components/reviews/reviews.component';
import { AlgorithmComponent } from './components/algorithm/algorithm.component';
import { OverlayModule } from '@angular/cdk/overlay';


@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserAnimationsModule,
    BrowserModule,
    OverlayModule,
    RouterModule.forRoot([{
      path: '', component: AppComponent, children: [
        {
          path: '', loadChildren: "./shared/components/responsive-template/responsive-template.module#ResponsiveTemplateModule"
        }
      ]
    }])

  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

