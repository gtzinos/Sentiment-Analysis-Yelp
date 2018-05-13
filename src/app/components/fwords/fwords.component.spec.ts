import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FwordsComponent } from './fwords.component';

describe('FwordsComponent', () => {
  let component: FwordsComponent;
  let fixture: ComponentFixture<FwordsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FwordsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FwordsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
