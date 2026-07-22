import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { AuthService } from './auth.service';
import { NotificationService } from './notification.service';

export const authGuard: CanActivateFn = () => {
  const authService = inject(AuthService);
  const router = inject(Router);
  const notificationService = inject(NotificationService);

  if (authService.isAuthenticated()) {
    return true;
  } else {
    notificationService.show('Please log in to view the profile page.', 'warning');
    router.navigate(['/login']);
    return false;
  }
};
