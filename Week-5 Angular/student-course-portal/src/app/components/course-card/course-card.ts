import { Component, Input, Output, EventEmitter, OnInit, OnChanges, OnDestroy, SimpleChanges } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { Course } from '../../models/course.model';
import { HighlightDirective } from '../../directives/highlight.directive';
import { CreditLabelPipe } from '../../pipes/credit-label.pipe';

@Component({
  selector: 'app-course-card',
  imports: [CommonModule, HighlightDirective, CreditLabelPipe, RouterLink],
  templateUrl: './course-card.html',
  styleUrl: './course-card.css'
})
export class CourseCardComponent implements OnInit, OnChanges, OnDestroy {
  @Input() course!: Course;
  @Input() searchQuery: string = '';
  @Output() enrollmentToggled = new EventEmitter<number>();
  @Output() creditsChanged = new EventEmitter<{ id: number; credits: number }>();
  @Output() courseDeleted = new EventEmitter<number>();

  ngOnInit(): void {
    console.log('CourseCardComponent Init:', this.course?.code);
  }

  ngOnChanges(changes: SimpleChanges): void {
    console.log('CourseCardComponent Changes:', this.course?.code, Object.keys(changes));
  }

  ngOnDestroy(): void {
    console.log('CourseCardComponent Destroy:', this.course?.code);
  }

  toggleEnrollment(): void {
    this.enrollmentToggled.emit(this.course.id);
  }

  increaseCredits(): void {
    this.creditsChanged.emit({ id: this.course.id, credits: this.course.credits + 1 });
  }

  decreaseCredits(): void {
    if (this.course.credits > 1) {
      this.creditsChanged.emit({ id: this.course.id, credits: this.course.credits - 1 });
    }
  }

  highlightMatch(text: string): boolean {
    if (!this.searchQuery) return false;
    return text.toLowerCase().includes(this.searchQuery.toLowerCase());
  }

  deleteCourse(): void {
    this.courseDeleted.emit(this.course.id);
  }
}
