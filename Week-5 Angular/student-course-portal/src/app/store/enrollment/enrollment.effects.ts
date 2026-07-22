import { Injectable, inject } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { of } from 'rxjs';
import { catchError, map, switchMap, tap } from 'rxjs/operators';
import * as EnrollmentActions from './enrollment.actions';
import { CourseService } from '../../services/course.service';

@Injectable()
export class EnrollmentEffects {
  private actions$ = inject(Actions);
  private courseService = inject(CourseService);

  loadEnrollments$ = createEffect(() =>
    this.actions$.pipe(
      ofType(EnrollmentActions.loadEnrollments),
      switchMap(() =>
        this.courseService.getCourses().pipe(
          map(courses => {
            const enrolledIds = courses.filter(c => c.enrolled).map(c => c.id);
            return EnrollmentActions.loadEnrollmentsSuccess({ enrolledIds });
          }),
          catchError(error =>
            of(EnrollmentActions.loadEnrollmentsFailure({ error: error.message || 'Error loading enrollments' }))
          )
        )
      )
    )
  );

  enrollCourse$ = createEffect(() =>
    this.actions$.pipe(
      ofType(EnrollmentActions.enrollCourse),
      switchMap(action =>
        this.courseService.updateCourseEnrollment(action.courseId, true).pipe(
          map(() => {
            return EnrollmentActions.enrollCourseSuccess({ courseId: action.courseId, courseCode: action.courseCode });
          }),
          catchError(error => {
            return of(EnrollmentActions.enrollCourseFailure({ error: error.message || 'Error enrolling course' }));
          })
        )
      )
    )
  );

  unenrollCourse$ = createEffect(() =>
    this.actions$.pipe(
      ofType(EnrollmentActions.unenrollCourse),
      switchMap(action =>
        this.courseService.updateCourseEnrollment(action.courseId, false).pipe(
          map(() => {
            return EnrollmentActions.unenrollCourseSuccess({ courseId: action.courseId, courseCode: action.courseCode });
          }),
          catchError(error => {
            return of(EnrollmentActions.unenrollCourseFailure({ error: error.message || 'Error unenrolling course' }));
          })
        )
      )
    )
  );
}
