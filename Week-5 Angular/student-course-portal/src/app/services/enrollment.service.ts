import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, combineLatest } from 'rxjs';
import { map } from 'rxjs/operators';
import { Course } from '../models/course.model';
import { CourseService } from './course.service';
import { NotificationService } from './notification.service';

@Injectable({
  providedIn: 'root'
})
export class EnrollmentService {
  private enrolledCourseIdsSubject = new BehaviorSubject<Set<number>>(new Set([2, 5]));

  constructor(
    private courseService: CourseService,
    private notificationService: NotificationService
  ) {
    // Reactively update enrolled ids based on server courses catalog state
    this.courseService.getCourses().subscribe(courses => {
      const enrolledSet = new Set<number>(
        courses.filter(c => c.enrolled).map(c => c.id)
      );
      const current = this.enrolledCourseIdsSubject.value;
      const isDifferent = current.size !== enrolledSet.size || [...enrolledSet].some(id => !current.has(id));
      if (isDifferent) {
        this.enrolledCourseIdsSubject.next(enrolledSet);
      }
    });
  }

  getEnrolledCourseIds(): Observable<Set<number>> {
    return this.enrolledCourseIdsSubject.asObservable();
  }

  getEnrolledCreditsCount(): Observable<number> {
    return combineLatest([
      this.courseService.getCourses(),
      this.enrolledCourseIdsSubject.asObservable()
    ]).pipe(
      map(([courses, enrolledIds]) => {
        return courses
          .filter(c => enrolledIds.has(c.id))
          .reduce((sum, c) => sum + c.credits, 0);
      })
    );
  }

  enrollCourse(course: Course): void {
    this.courseService.updateCourseEnrollment(course.id, true).subscribe({
      next: () => this.notificationService.show(`Enrolled in ${course.code} successfully!`, 'success'),
      error: () => this.notificationService.show(`Could not enroll in ${course.code}.`, 'warning')
    });
  }

  unenrollCourse(course: Course): void {
    this.courseService.updateCourseEnrollment(course.id, false).subscribe({
      next: () => this.notificationService.show(`Unenrolled from ${course.code}.`, 'info'),
      error: () => this.notificationService.show(`Could not unenroll from ${course.code}.`, 'warning')
    });
  }
}
