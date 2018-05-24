import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { RestaurantsByWifiComponent } from './restaurants-by-wifi.component';

describe('RestaurantsByWifiComponent', () => {
  let component: RestaurantsByWifiComponent;
  let fixture: ComponentFixture<RestaurantsByWifiComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RestaurantsByWifiComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RestaurantsByWifiComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
