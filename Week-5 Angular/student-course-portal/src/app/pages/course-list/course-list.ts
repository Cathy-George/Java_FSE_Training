import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Course } from '../../models/course.model';
import { CourseCardComponent } from '../../components/course-card/course-card';
import { CourseService } from '../../services/course.service';
import { EnrollmentService } from '../../services/enrollment.service';
import { combineLatest, Subscription } from 'rxjs';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-course-list',
  imports: [FormsModule, CourseCardComponent, CommonModule],
  templateUrl: './course-list.html',
  styleUrl: './course-list.css',
})
export class CourseList implements OnInit, OnDestroy {
  courses: Course[] = [];
  searchText: string = '';
  showEnrolledOnly: boolean = false;
  showAddForm = false;

  newCourse = {
    title: '',
    code: '',
    instructor: '',
    credits: 3,
    department: 'Computer Science',
    description: ''
  };

  private stateSub!: Subscription;
  private querySub!: Subscription;

  constructor(
    private courseService: CourseService,
    private enrollmentService: EnrollmentService,
    private route: ActivatedRoute
  ) {}

  ngOnInit(): void {
    // Combine singleton course state and enrollment set state reactively
    this.stateSub = combineLatest([
      this.courseService.getCourses(),
      this.enrollmentService.getEnrolledCourseIds()
    ]).subscribe(([courses, enrolledIds]) => {
      this.courses = courses.map((c) => ({
        ...c,
        enrolled: enrolledIds.has(c.id)
      }));
    });

    // Listen to query parameters for category/department filter direct navigation
    this.querySub = this.route.queryParamMap.subscribe((queryParams) => {
      if (queryParams.has('department')) {
        this.searchText = queryParams.get('department') || '';
      }
    });
  }

  get filteredCourses(): Course[] {
    return this.courses.filter(course => {
      const matchesSearch = !this.searchText || 
        course.title.toLowerCase().includes(this.searchText.toLowerCase()) ||
        course.code.toLowerCase().includes(this.searchText.toLowerCase()) ||
        course.instructor.toLowerCase().includes(this.searchText.toLowerCase()) ||
        course.department.toLowerCase().includes(this.searchText.toLowerCase());
      
      const matchesEnrollment = !this.showEnrolledOnly || course.enrolled;
      
      return matchesSearch && matchesEnrollment;
    });
  }

  get enrolledCount(): number {
    return this.courses.filter(c => c.enrolled).length;
  }

  get totalCredits(): number {
    return this.courses.filter(c => c.enrolled).reduce((acc, c) => acc + c.credits, 0);
  }

  onEnrollmentToggled(id: number): void {
    const course = this.courses.find(c => c.id === id);
    if (course) {
      if (course.enrolled) {
        this.enrollmentService.unenrollCourse(course);
      } else {
        this.enrollmentService.enrollCourse(course);
      }
    }
  }

  onCreditsChanged(event: { id: number; credits: number }): void {
    this.courseService.updateCourseCredits(event.id, event.credits);
  }

  incrementAllCredits(): void {
    this.courseService.incrementAllCredits();
  }

  addCourse(): void {
    if (this.newCourse.title && this.newCourse.code && this.newCourse.instructor) {
      this.courseService.createCourse(this.newCourse).subscribe({
        next: () => {
          this.newCourse = {
            title: '',
            code: '',
            instructor: '',
            credits: 3,
            department: 'Computer Science',
            description: ''
          };
          this.showAddForm = false;
        }
      });
    }
  }

  deleteCourse(id: number): void {
    if (confirm('Are you sure you want to delete this course from the catalog?')) {
      this.courseService.deleteCourse(id).subscribe();
    }
  }

  trackByCourseId(index: number, course: Course): number {
    return course.id;
  }

  ngOnDestroy(): void {
    if (this.stateSub) {
      this.stateSub.unsubscribe();
    }
    if (this.querySub) {
      this.querySub.unsubscribe();
    }
  }
}
