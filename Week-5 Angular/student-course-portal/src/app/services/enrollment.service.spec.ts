import { describe, it, expect, beforeEach, vi } from 'vitest';
import { TestBed } from '@angular/core/testing';
import { provideMockStore, MockStore } from '@ngrx/store/testing';
import { EnrollmentService } from './enrollment.service';
import { CourseService } from './course.service';
import { NotificationService } from './notification.service';
import * as EnrollmentActions from '../store/enrollment/enrollment.actions';
import { of } from 'rxjs';

describe('EnrollmentService', () => {
  let service: EnrollmentService;
  let store: MockStore;
  let mockCourseService: any;
  let mockNotificationService: any;

  beforeEach(() => {
    mockCourseService = {
      getCourses: () => of([]),
      updateCourseEnrollment: () => of([])
    };

    mockNotificationService = {
      show: () => {}
    };

    TestBed.configureTestingModule({
      providers: [
        EnrollmentService,
        provideMockStore({
          initialState: {
            enrollment: {
              enrolledCourseIds: [2, 5],
              loading: false,
              error: null
            }
          }
        }),
        { provide: CourseService, useValue: mockCourseService },
        { provide: NotificationService, useValue: mockNotificationService }
      ]
    });

    service = TestBed.inject(EnrollmentService);
    store = TestBed.inject(MockStore);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should return enrolled course IDs from store', async () => {
    service.getEnrolledCourseIds().subscribe(ids => {
      expect(ids.has(2)).toBe(true);
      expect(ids.has(5)).toBe(true);
      expect(ids.has(1)).toBe(false);
    });
  });

  it('should dispatch enrollCourse action', () => {
    const dispatchSpy = vi.spyOn(store, 'dispatch');
    const dummyCourse = { id: 1, title: 'Course 1', code: 'C1', instructor: 'Ins', credits: 3, department: 'CS', enrolled: false, description: '' };
    
    service.enrollCourse(dummyCourse);
    
    expect(dispatchSpy).toHaveBeenCalledWith(
      EnrollmentActions.enrollCourse({ courseId: 1, courseCode: 'C1' })
    );
  });
});
