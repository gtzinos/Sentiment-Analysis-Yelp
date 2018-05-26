import { Component, OnInit, ChangeDetectorRef, OnDestroy } from '@angular/core';
import { MediaMatcher } from '@angular/cdk/layout';
import { Router } from '@angular/router';

@Component({
  selector: 'responsive-template',
  templateUrl: './responsive-template.html',
  styleUrls: ['./responsive-template.css']
})
export class ResponsiveTemplateComponent implements OnDestroy {
  mobileQuery: MediaQueryList;

  parentTitles = [
    {
      title: "Home",
      url: "/home"
    },
    {
      title: "Plots",
      url: "/reviews-per-year",
      children: [
        {
          title: "Reviews Per Year",
          url: "/reviews-per-year"
        },
        {
          title: "Restaurants By Wifi",
          url: "/restaurants-by-wifi"
        },
        {
          title: "Users Per Year",
          url: "/users-per-year"
        },
        {
          title: "Restaurants by Groups",
          url: "/restaurants-by-groups"
        }
      ]
    },
    {
      title: "Top 10",
      url: "/restaurants",
      children: [
        {
          title: "Restaurants",
          url: "/restaurants"
        },
        {
          title: "Reviews",
          url: "/reviews"
        },
        {
          title: "Users",
          url: "/users"
        }
      ]
    },
    {
      title: "Models Evaluation",
      url: "/evaluation",
      children: [
        {
          title: "Algorithm 1",
          url: "/algorithm"
        }
      ]
    },
    {
      title:"Maps",
      url:"/maps"
    },
    {
      title: "About",
      url: "/about"
    }
    
  ]

  private _mobileQueryListener: () => void;

  constructor(changeDetectorRef: ChangeDetectorRef, media: MediaMatcher) {
    this.mobileQuery = media.matchMedia('(max-width: 600px)');
    this._mobileQueryListener = () => changeDetectorRef.detectChanges();
    this.mobileQuery.addListener(this._mobileQueryListener);
  }

  ngOnDestroy(): void {
    this.mobileQuery.removeListener(this._mobileQueryListener);
  }

  shouldRun = [/(^|\.)plnkr\.co$/, /(^|\.)stackblitz\.io$/].some(h => h.test(window.location.host));

}
