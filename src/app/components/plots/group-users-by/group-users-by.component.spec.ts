import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { GroupUsersByComponent } from './group-users-by.component';

describe('GroupUsersByComponent', () => {
  let component: GroupUsersByComponent;
  let fixture: ComponentFixture<GroupUsersByComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GroupUsersByComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GroupUsersByComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
