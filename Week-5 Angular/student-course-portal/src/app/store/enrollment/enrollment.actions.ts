import { createAction, props } from '@ngrx/store';

export const loadEnrollments = createAction('[Enrollment] Load Enrollments');
export const loadEnrollmentsSuccess = createAction(
  '[Enrollment] Load Enrollments Success',
  props<{ enrolledIds: number[] }>()
);
export const loadEnrollmentsFailure = createAction(
  '[Enrollment] Load Enrollments Failure',
  props<{ error: string }>()
);

export const enrollCourse = createAction(
  '[Enrollment] Enroll Course',
  props<{ courseId: number; courseCode: string }>()
);
export const enrollCourseSuccess = createAction(
  '[Enrollment] Enroll Course Success',
  props<{ courseId: number; courseCode: string }>()
);
export const enrollCourseFailure = createAction(
  '[Enrollment] Enroll Course Failure',
  props<{ error: string }>()
);

export const unenrollCourse = createAction(
  '[Enrollment] Unenroll Course',
  props<{ courseId: number; courseCode: string }>()
);
export const unenrollCourseSuccess = createAction(
  '[Enrollment] Unenroll Course Success',
  props<{ courseId: number; courseCode: string }>()
);
export const unenrollCourseFailure = createAction(
  '[Enrollment] Unenroll Course Failure',
  props<{ error: string }>()
);
