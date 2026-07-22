import { Component, OnInit, OnDestroy } from '@angular/core';
import { RouterLink, RouterLinkActive, Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { EnrollmentService } from '../../services/enrollment.service';
import { AuthService } from '../../services/auth.service';
import { NotificationService } from '../../services/notification.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-header',
  imports: [RouterLink, RouterLinkActive, CommonModule],
  templateUrl: './header.html',
  styleUrl: './header.css',
})
export class Header implements OnInit, OnDestroy {
  enrolledCount = 0;
  isLoggedIn = false;
  private enrollmentSub!: Subscription;
  private authSub!: Subscription;

  constructor(
    private enrollmentService: EnrollmentService,
    private authService: AuthService,
    private notificationService: NotificationService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.enrollmentSub = this.enrollmentService.getEnrolledCourseIds().subscribe((ids) => {
      this.enrolledCount = ids.size;
    });

    this.authSub = this.authService.isLoggedIn$.subscribe((status) => {
      this.isLoggedIn = status;
    });
  }

  logout(): void {
    this.authService.logout();
    this.notificationService.show('Logged out successfully.', 'info');
    this.router.navigate(['/login']);
  }

  ngOnDestroy(): void {
    if (this.enrollmentSub) {
      this.enrollmentSub.unsubscribe();
    }
    if (this.authSub) {
      this.authSub.unsubscribe();
    }
  }
}

