import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { LexiconsComponent } from './lexicons.component';

describe('LexiconsComponent', () => {
  let component: LexiconsComponent;
  let fixture: ComponentFixture<LexiconsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LexiconsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LexiconsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
