import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-course-syllabus',
  imports: [CommonModule],
  template: `
    <div class="tab-content-card">
      <h4 class="tab-content-title">📅 Course Syllabus & Schedule</h4>
      <ul class="syllabus-list">
        <li *ngFor="let item of syllabus" class="syllabus-item">
          <span class="week-badge">Week {{ item.week }}</span>
          <div class="syllabus-info">
            <h5 class="syllabus-topic">{{ item.topic }}</h5>
            <p class="syllabus-desc">{{ item.description }}</p>
          </div>
        </li>
      </ul>
    </div>
  `,
  styles: [`
    .tab-content-card {
      background: rgba(255, 255, 255, 0.015);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 1.5rem;
      margin-top: 1rem;
    }
    .tab-content-title {
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--text-primary);
      margin-bottom: 1.25rem;
      font-family: 'Outfit', sans-serif;
    }
    .syllabus-list {
      display: flex;
      flex-direction: column;
      gap: 1rem;
      list-style: none;
      padding: 0;
    }
    .syllabus-item {
      display: flex;
      gap: 1rem;
      align-items: flex-start;
      padding-bottom: 1rem;
      border-bottom: 1px dashed var(--border-color);
    }
    .syllabus-item:last-child {
      border-bottom: none;
      padding-bottom: 0;
    }
    .week-badge {
      background: rgba(99, 102, 241, 0.15);
      color: #a5b4fc;
      border: 1px solid rgba(99, 102, 241, 0.3);
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.25rem 0.6rem;
      border-radius: 6px;
      white-space: nowrap;
    }
    .syllabus-topic {
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--text-primary);
      margin: 0 0 0.25rem 0;
    }
    .syllabus-desc {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin: 0;
      line-height: 1.4;
    }
  `]
})
export class CourseSyllabus implements OnInit {
  courseId: number = 0;
  syllabus: any[] = [];

  constructor(private route: ActivatedRoute) {}

  ngOnInit(): void {
    // Read the parent's route parameter
    this.route.parent?.paramMap.subscribe(params => {
      this.courseId = Number(params.get('id'));
      this.loadSyllabus(this.courseId);
    });
  }

  loadSyllabus(id: number): void {
    const syllabi: Record<number, any[]> = {
      1: [
        { week: 1, topic: 'Introduction to Angular Architecture', description: 'Overview of modules, components, standalone structures, and the bootstrapping lifecycle.' },
        { week: 2, topic: 'Templates & Directives', description: 'Deep dive into template bindings, structural directives (*ngIf, *ngFor), and custom directives.' },
        { week: 3, topic: 'Reactive State & Services', description: 'Dependency Injection mechanics, singleton services, RxJS BehaviorSubject state sharing.' }
      ],
      2: [
        { week: 1, topic: 'Advanced Routing & Lazy Loading', description: 'Route parameters, lazy loading components, and protecting modules with CanActivate guards.' },
        { week: 2, topic: 'Asynchronous Form Validators', description: 'Writing synchronous and asynchronous form controls validations using RxJS timers.' }
      ]
    };
    
    this.syllabus = syllabi[id] || [
      { week: 1, topic: 'Course Groundwork & Environment Setup', description: 'Installing dependencies, setting up CLI builders, and defining schemas.' },
      { week: 2, topic: 'Primary Architecture Principles', description: 'Constructing components, layout directives, and styling bindings.' },
      { week: 3, topic: 'Modular Implementations', description: 'Testing validations, form entries, service injections, and routing structures.' }
    ];
  }
}
