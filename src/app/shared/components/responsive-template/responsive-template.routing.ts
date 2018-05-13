import { Routes, RouterModule } from '@angular/router';
import { ResponsiveTemplateComponent } from './responsive-template.component';


export const routes: Routes = [
 {
    path: '', component: ResponsiveTemplateComponent, children: [
      {
        path: '', redirectTo: 'home', pathMatch: 'full'
      },
      {
        path: 'home', loadChildren: '../../../components/home/home.module#HomeModule'
      },
      {
        path: 'about', loadChildren: '../../../components/about/about.module#AboutModule'
      },
      {
        path: 'lexicons', loadChildren: '../../../components/lexicons/lexicons.module#LexiconsModule'
      },
      {
        path: 'table', loadChildren: '../../../components/table/table.module#TableModule'
      },
      {
        path: 'reviews', loadChildren: '../../../components/reviews/reviews.module#ReviewsModule'
      }

    ]
  }
]
