import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-course-reviews',
  imports: [CommonModule],
  template: `
    <div class="tab-content-card">
      <h4 class="tab-content-title">⭐ Student Reviews & Ratings</h4>
      <div class="reviews-list">
        <div *ngFor="let rev of reviews" class="review-item">
          <div class="review-header">
            <span class="reviewer-name">{{ rev.author }}</span>
            <span class="reviewer-rating">{{ '⭐'.repeat(rev.rating) }}</span>
          </div>
          <p class="review-text">"{{ rev.text }}"</p>
        </div>
      </div>
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
    .reviews-list {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }
    .review-item {
      background: rgba(255, 255, 255, 0.015);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 1rem;
    }
    .review-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.5rem;
    }
    .reviewer-name {
      font-size: 0.9rem;
      font-weight: 600;
      color: var(--text-primary);
    }
    .reviewer-rating {
      font-size: 0.85rem;
    }
    .review-text {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin: 0;
      line-height: 1.4;
      font-style: italic;
    }
  `]
})
export class CourseReviews implements OnInit {
  courseId: number = 0;
  reviews: any[] = [];

  constructor(private route: ActivatedRoute) {}

  ngOnInit(): void {
    // Read parent route parameter
    this.route.parent?.paramMap.subscribe(params => {
      this.courseId = Number(params.get('id'));
      this.loadReviews(this.courseId);
    });
  }

  loadReviews(id: number): void {
    const reviewsMap: Record<number, any[]> = {
      1: [
        { author: 'Jane Miller', rating: 5, text: 'This course is exceptionally well structured. The projects are highly engaging.' },
        { author: 'Bob Peterson', rating: 4, text: 'Very clear explanations of components and standalone architecture. Solid foundation.' }
      ],
      2: [
        { author: 'Alice Vance', rating: 5, text: 'Advanced concepts are broken down perfectly. The validator logic was super helpful.' }
      ]
    };

    this.reviews = reviewsMap[id] || [
      { author: 'David Jones', rating: 5, text: 'Excellent instructor and highly relevant curriculum. Learnt a lot.' },
      { author: 'Megan Smith', rating: 4, text: 'Very comprehensive overview with hands-on lab exercises. Highly recommended.' }
    ];
  }
}
