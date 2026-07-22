import { Injectable, inject } from '@angular/core';
import { BehaviorSubject, Observable, combineLatest } from 'rxjs';
import { map, tap } from 'rxjs/operators';
import { Course } from '../models/course.model';
import { CourseService } from './course.service';
import { NotificationService } from './notification.service';
import { Store } from '@ngrx/store';
import * as EnrollmentActions from '../store/enrollment/enrollment.actions';
import { selectEnrolledCourseIds } from '../store/enrollment/enrollment.selectors';

@Injectable({
  providedIn: 'root'
})
export class EnrollmentService {
  private store = inject(Store);
  private courseService = inject(CourseService);
  private notificationService = inject(NotificationService);

  constructor() {
    // Load initial enrollments from catalog
    this.store.dispatch(EnrollmentActions.loadEnrollments());

    // Sync state whenever the courses catalog is updated directly
    this.courseService.getCourses().subscribe(courses => {
      const enrolledIds = courses.filter(c => c.enrolled).map(c => c.id);
      this.store.dispatch(EnrollmentActions.loadEnrollmentsSuccess({ enrolledIds }));
    });
  }

  getEnrolledCourseIds(): Observable<Set<number>> {
    return this.store.select(selectEnrolledCourseIds).pipe(
      map(ids => new Set(ids))
    );
  }

  getEnrolledCreditsCount(): Observable<number> {
    return combineLatest([
      this.courseService.getCourses(),
      this.store.select(selectEnrolledCourseIds)
    ]).pipe(
      map(([courses, enrolledIds]) => {
        const idSet = new Set(enrolledIds);
        return courses
          .filter(c => idSet.has(c.id))
          .reduce((sum, c) => sum + c.credits, 0);
      })
    );
  }

  enrollCourse(course: Course): void {
    this.store.dispatch(EnrollmentActions.enrollCourse({ courseId: course.id, courseCode: course.code }));
    this.notificationService.show(`Enrolled in ${course.code} successfully!`, 'success');
  }

  unenrollCourse(course: Course): void {
    this.store.dispatch(EnrollmentActions.unenrollCourse({ courseId: course.id, courseCode: course.code }));
    this.notificationService.show(`Unenrolled from ${course.code}.`, 'info');
  }
}
