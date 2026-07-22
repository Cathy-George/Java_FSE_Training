import { CanDeactivateFn } from '@angular/router';
import { StudentProfile } from '../pages/student-profile/student-profile';

export const canDeactivateProfile: CanDeactivateFn<StudentProfile> = (component: StudentProfile) => {
  // If profile form is dirty and has not just been successfully submitted, warn
  if (component.profileForm && component.profileForm.dirty && !component.showSuccess) {
    return confirm('You have unsaved changes. Do you really want to leave this page?');
  }
  return true;
};
