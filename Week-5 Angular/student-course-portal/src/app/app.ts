import { Component, OnInit, OnDestroy, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';
import { Header } from './components/header/header';
import { NotificationService, AppNotification } from './services/notification.service';
import { LoadingService } from './services/loading.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, Header, CommonModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App implements OnInit, OnDestroy {
  protected readonly title = signal('student-course-portal');
  activeNotifications: AppNotification[] = [];
  isLoading = false;
  private notifSub!: Subscription;
  private loadingSub!: Subscription;

  constructor(
    private notificationService: NotificationService,
    private loadingService: LoadingService
  ) {}

  ngOnInit(): void {
    this.notifSub = this.notificationService.getNotifications().subscribe((notif) => {
      this.activeNotifications.push(notif);
      // Auto-expire toast in 4 seconds
      setTimeout(() => {
        this.dismissNotification(notif.id);
      }, 4000);
    });

    this.loadingSub = this.loadingService.loading$.subscribe((status) => {
      this.isLoading = status;
    });
  }

  dismissNotification(id: number): void {
    this.activeNotifications = this.activeNotifications.filter((n) => n.id !== id);
  }

  ngOnDestroy(): void {
    if (this.notifSub) {
      this.notifSub.unsubscribe();
    }
    if (this.loadingSub) {
      this.loadingSub.unsubscribe();
    }
  }
}

