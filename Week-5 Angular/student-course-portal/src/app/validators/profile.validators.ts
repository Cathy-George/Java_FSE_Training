import { AbstractControl, AsyncValidatorFn, ValidationErrors, ValidatorFn } from '@angular/forms';
import { Observable, timer } from 'rxjs';
import { map } from 'rxjs/operators';

/**
 * Custom Validator to verify email domain ends with '@university.edu'
 */
export function universityEmailValidator(): ValidatorFn {
  return (control: AbstractControl): ValidationErrors | null => {
    const val = control.value;
    if (!val) return null;
    return val.toLowerCase().endsWith('@university.edu') ? null : { invalidDomain: true };
  };
}

/**
 * Async Validator to simulate checking if the email has already been registered
 */
export function emailUniqueValidator(): AsyncValidatorFn {
  return (control: AbstractControl): Observable<ValidationErrors | null> => {
    const val = control.value;
    if (!val) return timer(0).pipe(map(() => null));
    
    // Simulate API delay using a timer
    return timer(800).pipe(
      map(() => {
        const takenEmails = [
          'taken@university.edu',
          'admin@university.edu',
          'already.registered@university.edu'
        ];
        return takenEmails.includes(val.toLowerCase()) ? { emailTaken: true } : null;
      })
    );
  };
}
