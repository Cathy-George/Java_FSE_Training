import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { BehaviorSubject, Observable, throwError, forkJoin, of } from 'rxjs';
import { catchError, retry, tap, map, switchMap } from 'rxjs/operators';
import { Course } from '../models/course.model';

@Injectable({
  providedIn: 'root'
})
export class CourseService {
  private apiUrl = 'http://localhost:3000/courses';
  
  private mockInitialCourses: Course[] = [
    {
      id: 1,
      title: 'Introduction to Angular framework',
      code: 'CS-301',
      instructor: 'Dr. Sarah Connor',
      credits: 4,
      department: 'Computer Science',
      enrolled: false,
      description: 'Learn the fundamentals of Angular including components, directives, routing, data binding and form integration.'
    },
    {
      id: 2,
      title: 'Advanced Web Applications',
      code: 'CS-402',
      instructor: 'Prof. Alan Turing',
      credits: 3,
      department: 'Computer Science',
      enrolled: true,
      description: 'Deep dive into asynchronous programming, state management, HTTP communication, performance optimization and SSR.'
    },
    {
      id: 3,
      title: 'Database Management Systems',
      code: 'CS-205',
      instructor: 'Dr. Grace Hopper',
      credits: 4,
      department: 'Information Technology',
      enrolled: false,
      description: 'Explore relational database design, SQL querying, transaction management, indexing techniques and NoSQL alternatives.'
    },
    {
      id: 4,
      title: 'Human Computer Interaction',
      code: 'DS-110',
      instructor: 'Dr. Donald Norman',
      credits: 3,
      department: 'Design',
      enrolled: false,
      description: 'Introduction to user-centered design, prototyping, usability testing guidelines and interaction models.'
    },
    {
      id: 5,
      title: 'Cloud Architecture & DevOps',
      code: 'IT-440',
      instructor: 'Prof. Werner Vogels',
      credits: 3,
      department: 'Information Technology',
      enrolled: true,
      description: 'Analyze cloud deployment models, containerization with Docker, orchestration, CI/CD pipelines and microservices.'
    },
    {
      id: 6,
      title: 'Artificial Intelligence Basics',
      code: 'CS-380',
      instructor: 'Dr. John McCarthy',
      credits: 4,
      department: 'Computer Science',
      enrolled: false,
      description: 'Fundamental concepts in machine learning, search algorithms, neural networks and knowledge representation systems.'
    }
  ];

  private coursesSubject = new BehaviorSubject<Course[]>(this.mockInitialCourses);

  constructor(private http: HttpClient) {
    this.refreshCourses().subscribe({
      error: (err) => console.warn('Could not auto-fetch from JSON server, using local mocks:', err.message)
    });
  }

  getCourses(): Observable<Course[]> {
    return this.coursesSubject.asObservable();
  }

  refreshCourses(): Observable<Course[]> {
    return this.http.get<Course[]>(this.apiUrl).pipe(
      retry(2),
      map(courses => courses.map(c => ({ ...c, title: c.title.trim() }))),
      tap(courses => this.coursesSubject.next(courses)),
      catchError(this.handleError)
    );
  }

  createCourse(course: Omit<Course, 'id' | 'enrolled'>): Observable<Course[]> {
    const tempId = Math.max(...this.coursesSubject.value.map(c => c.id), 0) + 1;
    const newCourse: Course = { ...course, id: tempId, enrolled: false };
    
    // Optimistic update
    const current = this.coursesSubject.value;
    this.coursesSubject.next([...current, newCourse]);

    return this.http.post<Course>(this.apiUrl, { ...course, enrolled: false }).pipe(
      tap(created => console.log('Created course on server:', created.code)),
      switchMap(() => this.refreshCourses()),
      catchError(err => {
        console.warn('Could not create course on server, kept offline changes:', err.message);
        return of(this.coursesSubject.value);
      })
    );
  }

  updateCourseCredits(id: number, credits: number): void {
    // Optimistic update
    const current = this.coursesSubject.value;
    const updated = current.map(c => c.id === id ? { ...c, credits } : c);
    this.coursesSubject.next(updated);

    this.http.patch<Course>(`${this.apiUrl}/${id}`, { credits }).pipe(
      tap(updatedCourse => console.log('Updated credits on server:', updatedCourse.code, credits)),
      catchError(err => {
        console.warn('Could not update credits on server, kept offline changes:', err.message);
        return of(updated);
      })
    ).subscribe();
  }

  updateCourseEnrollment(id: number, enrolled: boolean): Observable<Course[]> {
    // Optimistic update
    const current = this.coursesSubject.value;
    const updated = current.map(c => c.id === id ? { ...c, enrolled } : c);
    this.coursesSubject.next(updated);

    return this.http.patch<Course>(`${this.apiUrl}/${id}`, { enrolled }).pipe(
      tap(updatedCourse => console.log('Updated enrollment on server:', updatedCourse.code, enrolled)),
      switchMap(() => this.refreshCourses()),
      catchError(err => {
        console.warn('Could not update enrollment on server, kept offline changes:', err.message);
        return of(this.coursesSubject.value);
      })
    );
  }

  deleteCourse(id: number): Observable<Course[]> {
    // Optimistic update
    const current = this.coursesSubject.value;
    const updated = current.filter(c => c.id !== id);
    this.coursesSubject.next(updated);

    return this.http.delete<void>(`${this.apiUrl}/${id}`).pipe(
      tap(() => console.log('Deleted course from server, id:', id)),
      switchMap(() => this.refreshCourses()),
      catchError(err => {
        console.warn('Could not delete course on server, kept offline changes:', err.message);
        return of(this.coursesSubject.value);
      })
    );
  }

  incrementAllCredits(): void {
    // Optimistic update
    const current = this.coursesSubject.value;
    const updated = current.map(c => ({ ...c, credits: c.credits + 1 }));
    this.coursesSubject.next(updated);

    this.http.get<Course[]>(this.apiUrl).pipe(
      retry(2),
      switchMap((courses) => {
        const updateObservables = courses.map(c => 
          this.http.patch<Course>(`${this.apiUrl}/${c.id}`, { credits: c.credits + 1 })
        );
        return forkJoin(updateObservables);
      }),
      switchMap(() => this.refreshCourses()),
      catchError(err => {
        console.warn('Could not increment credits on server, kept offline changes:', err.message);
        return of([]);
      })
    ).subscribe();
  }

  private handleError(error: HttpErrorResponse): Observable<never> {
    console.error('CourseService HTTP error:', error);
    return throwError(() => new Error(error.message || 'Server connection error'));
  }
}
