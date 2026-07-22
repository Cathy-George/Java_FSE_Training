import { describe, it, expect, beforeEach } from 'vitest';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { CourseList } from './course-list';
import { CourseService } from '../../services/course.service';
import { EnrollmentService } from '../../services/enrollment.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { provideRouter } from '@angular/router';
import { BehaviorSubject, of } from 'rxjs';
import { Course } from '../../models/course.model';

describe('CourseList', () => {
  let component: CourseList;
  let fixture: ComponentFixture<CourseList>;
  let courseService: CourseService;
  let enrollmentService: EnrollmentService;

  let mockCourses: Course[];
  let coursesSubject: BehaviorSubject<Course[]>;

  beforeEach(async () => {
    mockCourses = [
      {
        id: 1,
        title: 'Introduction to Angular framework',
        code: 'CS-301',
        instructor: 'Dr. Sarah Connor',
        credits: 4,
        department: 'Computer Science',
        enrolled: false,
        description: 'Learn the fundamentals of Angular.'
      },
      {
        id: 2,
        title: 'Advanced Web Applications',
        code: 'CS-402',
        instructor: 'Prof. Alan Turing',
        credits: 3,
        department: 'Computer Science',
        enrolled: true,
        description: 'Deep dive into advanced topics.'
      }
    ];

    coursesSubject = new BehaviorSubject<Course[]>(mockCourses);

    const mockCourseService = {
      getCourses: () => coursesSubject.asObservable(),
      updateCourseCredits: (id: number, credits: number) => {
        const current = coursesSubject.value;
        const updated = current.map(c => c.id === id ? { ...c, credits } : c);
        coursesSubject.next(updated);
      },
      incrementAllCredits: () => {
        const current = coursesSubject.value;
        const updated = current.map(c => ({ ...c, credits: c.credits + 1 }));
        coursesSubject.next(updated);
      },
      updateCourseEnrollment: (id: number, enrolled: boolean) => {
        const current = coursesSubject.value;
        const updated = current.map(c => c.id === id ? { ...c, enrolled } : c);
        coursesSubject.next(updated);
        return of(updated);
      }
    };

    await TestBed.configureTestingModule({
      imports: [CourseList, CommonModule, FormsModule],
      providers: [
        provideRouter([]),
        { provide: CourseService, useValue: mockCourseService }
      ]
    }).compileComponents();

    fixture = TestBed.createComponent(CourseList);
    component = fixture.componentInstance;
    courseService = TestBed.inject(CourseService);
    enrollmentService = TestBed.inject(EnrollmentService);
    fixture.detectChanges();
    await fixture.whenStable();
  });

  it('should create the component', () => {
    expect(component).toBeTruthy();
  });

  it('should populate courses collection from CourseService', () => {
    expect(component.courses.length).toBeGreaterThan(0);
    expect(component.courses[0].title).toBe('Introduction to Angular framework');
  });

  it('should toggle enrollment using the EnrollmentService', () => {
    const targetCourse = component.courses[0];
    const initialEnrolled = targetCourse.enrolled;
    
    component.onEnrollmentToggled(targetCourse.id);
    fixture.detectChanges();
    
    expect(component.courses[0].enrolled).toBe(!initialEnrolled);
  });

  it('should dispatch credit changes to the CourseService', () => {
    const targetCourse = component.courses[0];
    component.onCreditsChanged({ id: targetCourse.id, credits: 5 });
    fixture.detectChanges();
    
    expect(component.courses[0].credits).toBe(5);
  });
});
