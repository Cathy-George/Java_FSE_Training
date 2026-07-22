import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private isLoggedInSubject = new BehaviorSubject<boolean>(true); // Default to logged in

  isLoggedIn$: Observable<boolean> = this.isLoggedInSubject.asObservable();

  isAuthenticated(): boolean {
    return this.isLoggedInSubject.value;
  }

  login(): void {
    this.isLoggedInSubject.next(true);
  }

  logout(): void {
    this.isLoggedInSubject.next(false);
  }
}
