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
        path: 'models-evaluation', loadChildren: '../../../components/models-evaluation/models-evaluation.module#ModelsEvaluationModule'
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
      },
      {
        path: 'users-per-year', loadChildren: '../../../components/plots/users-per-year/users-per-year.module#UsersPerYearModule'
      },
      {
        path: 'top-words', loadChildren: '../../../components/plots/word-count/word-count.module#WordCountModule'
      },
      {
        path: 'maps', loadChildren: '../../../components/maps/maps.module#MapsModule'
      },
      {
        path: 'group-users-by', loadChildren: '../../../components/plots/group-users-by/group-users-by.module#GroupUsersByModule'
      },
      {
        path: 'restaurants-by-groups', loadChildren: '../../../components/plots/restaurants-by-groups/restaurants-by-groups.module#RestaurantsByGroupsModule'
      },
      {
        path: 'neighborhood', loadChildren: '../../../components/tables/neighborhood/neighborhood.module#NeighborhoodModule'
      }
    ]
  }
]
