import { Component, OnInit, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterLink, RouterOutlet, RouterLinkActive } from '@angular/router';
import { CourseService } from '../../services/course.service';
import { Course } from '../../models/course.model';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-course-detail',
  imports: [CommonModule, RouterLink, RouterOutlet, RouterLinkActive],
  templateUrl: './course-detail.html',
  styleUrl: './course-detail.css'
})
export class CourseDetail implements OnInit, OnDestroy {
  course: Course | null = null;
  private routeSub!: Subscription;

  constructor(
    private route: ActivatedRoute,
    private courseService: CourseService
  ) {}

  ngOnInit(): void {
    this.routeSub = this.route.paramMap.subscribe(params => {
      const courseId = Number(params.get('id'));
      
      this.courseService.getCourses().subscribe(courses => {
        const found = courses.find(c => c.id === courseId);
        this.course = found || null;
      });
    });
  }

  ngOnDestroy(): void {
    if (this.routeSub) {
      this.routeSub.unsubscribe();
    }
  }
}
