import { Injectable } from '@angular/core';
import { Subject, Observable } from 'rxjs';

export interface AppNotification {
  message: string;
  type: 'success' | 'info' | 'warning';
  id: number;
}

@Injectable({
  providedIn: 'root'
})
export class NotificationService {
  private notificationsSubject = new Subject<AppNotification>();
  private nextId = 0;

  getNotifications(): Observable<AppNotification> {
    return this.notificationsSubject.asObservable();
  }

  show(message: string, type: 'success' | 'info' | 'warning' = 'success'): void {
    this.notificationsSubject.next({
      message,
      type,
      id: this.nextId++
    });
  }
}
