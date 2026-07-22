import { createReducer, on } from '@ngrx/store';
import * as EnrollmentActions from './enrollment.actions';

export interface EnrollmentState {
  enrolledCourseIds: number[];
  loading: boolean;
  error: string | null;
}

export const initialState: EnrollmentState = {
  enrolledCourseIds: [2, 5], // default enrolled ids from mock
  loading: false,
  error: null
};

export const enrollmentReducer = createReducer(
  initialState,
  on(EnrollmentActions.loadEnrollments, (state) => ({
    ...state,
    loading: true,
    error: null
  })),
  on(EnrollmentActions.loadEnrollmentsSuccess, (state, { enrolledIds }) => ({
    ...state,
    enrolledCourseIds: enrolledIds,
    loading: false
  })),
  on(EnrollmentActions.loadEnrollmentsFailure, (state, { error }) => ({
    ...state,
    error,
    loading: false
  })),
  on(EnrollmentActions.enrollCourse, (state) => ({
    ...state,
    loading: true,
    error: null
  })),
  on(EnrollmentActions.enrollCourseSuccess, (state, { courseId }) => ({
    ...state,
    enrolledCourseIds: state.enrolledCourseIds.includes(courseId)
      ? state.enrolledCourseIds
      : [...state.enrolledCourseIds, courseId],
    loading: false
  })),
  on(EnrollmentActions.enrollCourseFailure, (state, { error }) => ({
    ...state,
    error,
    loading: false
  })),
  on(EnrollmentActions.unenrollCourse, (state) => ({
    ...state,
    loading: true,
    error: null
  })),
  on(EnrollmentActions.unenrollCourseSuccess, (state, { courseId }) => ({
    ...state,
    enrolledCourseIds: state.enrolledCourseIds.filter(id => id !== courseId),
    loading: false
  })),
  on(EnrollmentActions.unenrollCourseFailure, (state, { error }) => ({
    ...state,
    error,
    loading: false
  }))
);
