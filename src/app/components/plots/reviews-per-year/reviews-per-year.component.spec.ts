import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { ReviewsPerYearComponent } from './reviews-per-year.component';

describe('ReviewsPerYearComponent', () => {
  let component: ReviewsPerYearComponent;
  let fixture: ComponentFixture<ReviewsPerYearComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ReviewsPerYearComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ReviewsPerYearComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
