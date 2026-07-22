import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { NotificationService } from '../../services/notification.service';

@Component({
  selector: 'app-login',
  imports: [CommonModule],
  templateUrl: './login.html',
  styleUrl: './login.css'
})
export class Login implements OnInit {
  isLoggedIn = false;

  constructor(
    private authService: AuthService,
    private notificationService: NotificationService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.authService.isLoggedIn$.subscribe(status => {
      this.isLoggedIn = status;
    });
  }

  toggleLogin(): void {
    if (this.isLoggedIn) {
      this.authService.logout();
      this.notificationService.show('Logged out successfully.', 'info');
    } else {
      this.authService.login();
      this.notificationService.show('Logged in successfully.', 'success');
      this.router.navigate(['/profile']);
    }
  }
}
