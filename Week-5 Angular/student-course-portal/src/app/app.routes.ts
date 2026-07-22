import { Routes } from '@angular/router';
import { authGuard } from './services/auth.guard';
import { canDeactivateProfile } from './services/deactivate.guard';

export const routes: Routes = [
  { 
    path: '', 
    loadComponent: () => import('./pages/home/home').then(m => m.Home) 
  },
  { 
    path: 'courses', 
    loadComponent: () => import('./pages/course-list/course-list').then(m => m.CourseList) 
  },
  {
    path: 'courses/:id',
    loadComponent: () => import('./pages/course-detail/course-detail').then(m => m.CourseDetail),
    children: [
      { path: '', redirectTo: 'syllabus', pathMatch: 'full' },
      { 
        path: 'syllabus', 
        loadComponent: () => import('./pages/course-detail/syllabus/syllabus').then(m => m.CourseSyllabus) 
      },
      { 
        path: 'reviews', 
        loadComponent: () => import('./pages/course-detail/reviews/reviews').then(m => m.CourseReviews) 
      }
    ]
  },
  { 
    path: 'profile', 
    loadComponent: () => import('./pages/student-profile/student-profile').then(m => m.StudentProfile),
    canActivate: [authGuard],
    canDeactivate: [canDeactivateProfile]
  },
  { 
    path: 'login', 
    loadComponent: () => import('./pages/login/login').then(m => m.Login) 
  },
  { 
    path: 'not-found', 
    loadComponent: () => import('./pages/not-found/not-found').then(m => m.NotFound) 
  },
  { path: '**', redirectTo: 'not-found' }
];
