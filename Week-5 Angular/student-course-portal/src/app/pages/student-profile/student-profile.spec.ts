import { describe, it, expect, beforeEach } from 'vitest';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ReactiveFormsModule } from '@angular/forms';
import { provideHttpClient } from '@angular/common/http';
import { StudentProfile } from './student-profile';

describe('StudentProfile', () => {
  let component: StudentProfile;
  let fixture: ComponentFixture<StudentProfile>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [StudentProfile, ReactiveFormsModule],
      providers: [provideHttpClient()]
    }).compileComponents();

    fixture = TestBed.createComponent(StudentProfile);
    component = fixture.componentInstance;
    fixture.detectChanges();
    await fixture.whenStable();
  });

  it('should create the component', () => {
    expect(component).toBeTruthy();
  });

  it('should initialize with default baseline values', () => {
    expect(component.profileForm.get('name')?.value).toBe('Cathy George');
    expect(component.profileForm.get('gpa')?.value).toBe(3.85);
    expect(component.projects.length).toBe(2);
  });

  it('should change avatar emoji when selected', () => {
    component.onAvatarChange('🤖');
    expect(component.profileForm.get('avatar')?.value).toBe('🤖');
    expect(component.student.avatar).toBe('🤖');
  });

  it('should invalidate email domain if not @university.edu', () => {
    const emailCtrl = component.profileForm.get('email');
    emailCtrl?.setValue('cathy@gmail.com');
    expect(emailCtrl?.errors?.['invalidDomain']).toBe(true);
  });

  it('should validate email domain if ends with @university.edu', () => {
    const emailCtrl = component.profileForm.get('email');
    emailCtrl?.setValue('cathy@university.edu');
    expect(emailCtrl?.errors?.['invalidDomain']).toBeUndefined();
  });

  it('should check email uniqueness asynchronously', async () => {
    // Wait for initial validations to settle
    await new Promise((resolve) => setTimeout(resolve, 950));
    fixture.detectChanges();

    const emailCtrl = component.profileForm.get('email');
    emailCtrl?.setValue('taken@university.edu');
    
    // Status is pending before timer fires
    expect(emailCtrl?.status).toBe('PENDING');
    
    // Wait for the async timer to resolve (800ms)
    await new Promise((resolve) => setTimeout(resolve, 950));
    fixture.detectChanges();
    
    expect(emailCtrl?.status).toBe('INVALID');
    expect(emailCtrl?.errors?.['emailTaken']).toBe(true);
  });

  it('should allow dynamic FormArray additions and removals of projects', () => {
    expect(component.projects.length).toBe(2);
    
    component.addProject('Test Project', 'Angular Testing');
    expect(component.projects.length).toBe(3);
    expect(component.projects.at(2).get('title')?.value).toBe('Test Project');
    
    component.removeProject(2);
    expect(component.projects.length).toBe(2);
  });

  it('should trigger onSubmit and set showSuccess flags', async () => {
    // Wait for the initial email validation to finish
    await new Promise((resolve) => setTimeout(resolve, 950));
    fixture.detectChanges();

    expect(component.showSuccess).toBe(false);
    component.onSubmit();
    expect(component.showSuccess).toBe(true);
  });

  it('should reset form values on call to onReset', async () => {
    // Wait for the initial email validation to finish
    await new Promise((resolve) => setTimeout(resolve, 950));
    fixture.detectChanges();

    component.profileForm.get('name')?.setValue('Modified Name');
    component.addProject('Brand New', 'Spring Boot');
    expect(component.projects.length).toBe(3);

    component.onReset();
    fixture.detectChanges();
    
    expect(component.profileForm.get('name')?.value).toBe('Cathy George');
    expect(component.projects.length).toBe(2); // Restored to initial projects
  });
});
