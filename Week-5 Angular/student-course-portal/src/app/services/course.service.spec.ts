import { describe, it, expect, beforeEach, afterEach } from 'vitest';
import { TestBed } from '@angular/core/testing';
import { provideHttpClient } from '@angular/common/http';
import { provideHttpClientTesting, HttpTestingController } from '@angular/common/http/testing';
import { CourseService } from './course.service';
import { Course } from '../models/course.model';

describe('CourseService', () => {
  let service: CourseService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        CourseService,
        provideHttpClient(),
        provideHttpClientTesting()
      ]
    });
    service = TestBed.inject(CourseService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    httpMock.verify();
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should fetch courses catalog via GET', () => {
    const dummyCourses: Course[] = [
      { id: 1, title: 'Test Course 1', code: 'TC-101', instructor: 'Instructor 1', credits: 3, department: 'CS', enrolled: false, description: 'Desc 1' }
    ];

    service.refreshCourses().subscribe(courses => {
      expect(courses.length).toBe(1);
      expect(courses[0].title).toBe('Test Course 1');
    });

    const req = httpMock.expectOne('http://localhost:3000/courses');
    expect(req.request.method).toBe('GET');
    req.flush(dummyCourses);
  });

  it('should create a new course via POST', () => {
    const newCourseData = { title: 'New Course', code: 'NC-202', instructor: 'Instructor 2', credits: 4, department: 'IT', description: 'Desc 2' };
    const returnedCourse: Course = { ...newCourseData, id: 9, enrolled: false };

    service.createCourse(newCourseData).subscribe();

    const req = httpMock.expectOne('http://localhost:3000/courses');
    expect(req.request.method).toBe('POST');
    req.flush(returnedCourse);

    // After POST, service refreshCourses() makes a GET request
    const refreshReq = httpMock.expectOne('http://localhost:3000/courses');
    expect(refreshReq.request.method).toBe('GET');
    refreshReq.flush([returnedCourse]);
  });
});
