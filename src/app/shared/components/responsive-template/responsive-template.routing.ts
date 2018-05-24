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
        path: 'restaurants', loadChildren: '../../../components/tables/restaurants/restaurants.module#RestaurantsModule'
      },
      {
        path: 'reviews', loadChildren: '../../../components/tables/reviews/reviews.module#ReviewsModule'
      },
      {
        path: 'users', loadChildren: '../../../components/tables/users/users.module#UsersModule'
      },
      {
        path: 'reviews', loadChildren: '../../../components/reviews/reviews.module#ReviewsModule'
      },
      {
        path: 'reviews-per-year', loadChildren: '../../../components/plots/reviews-per-year/reviews-per-year.module#ReviewsPerYearModule'
      },
      {
        path: 'restaurants-by-wifi', loadChildren: '../../../components/plots/restaurants-by-wifi/restaurants-by-wifi.module#RestaurantsByWifiModule'
      }

    ]
  }
]
