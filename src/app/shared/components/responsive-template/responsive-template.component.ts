import { Component, OnInit, ChangeDetectorRef, OnDestroy } from '@angular/core';
import {MediaMatcher} from '@angular/cdk/layout';
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
      url: "/lexicons",
      children: [
        {
          title: "Lexicons",
          url: "/lexicons"
        },
        {
          title: "Frequent Words",
          url: "/fwords"
        },
        {
          title: "Revies Per Month",
          url: "/reviews"
        }
      ]
    },
    {
      title: "Tables",
      url: "/table"
    },
    {
      title: "Compare Algorithms",
      url: "/compare",
      children: [
        {
          title: "Algorithm 1",
          url: "/algorithm"
        }
      ]
    },
    {
      title: "About",
      url: "/about",
      children: [
        
      ]
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
