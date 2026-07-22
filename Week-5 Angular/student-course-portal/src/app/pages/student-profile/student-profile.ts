import { Component, OnInit, OnDestroy } from '@angular/core';
import { ReactiveFormsModule, FormBuilder, FormGroup, FormArray, Validators } from '@angular/forms';
import { DecimalPipe, CommonModule } from '@angular/common';
import { universityEmailValidator, emailUniqueValidator } from '../../validators/profile.validators';
import { EnrollmentService } from '../../services/enrollment.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-student-profile',
  imports: [ReactiveFormsModule, DecimalPipe, CommonModule],
  templateUrl: './student-profile.html',
  styleUrl: './student-profile.css',
})
export class StudentProfile implements OnInit, OnDestroy {
  avatars: string[] = ['👩‍💻', '👨‍💻', '🎓', '🚀', '🤖'];
  
  student = {
    name: 'Cathy George',
    email: 'cathy.george@university.edu',
    department: 'Computer Science & Engineering',
    bio: 'Passionate software engineer in training. Interested in Angular, cloud infrastructure, and databases.',
    avatar: '👩‍💻',
    gpa: 3.85,
    enrolledCredits: 6
  };

  profileForm!: FormGroup;
  showSuccess = false;
  private committedStudent = { ...this.student };
  private enrollmentSub!: Subscription;

  constructor(
    private fb: FormBuilder,
    private enrollmentService: EnrollmentService
  ) {}

  ngOnInit(): void {
    this.committedStudent = { ...this.student };
    this.profileForm = this.fb.group({
      name: [this.student.name, [Validators.required, Validators.minLength(3), Validators.pattern('^[a-zA-Z\\s]*$')]],
      email: [
        this.student.email,
        [Validators.required, Validators.email, universityEmailValidator()],
        [emailUniqueValidator()]
      ],
      department: [this.student.department, [Validators.required, Validators.minLength(4)]],
      gpa: [this.student.gpa, [Validators.required, Validators.min(0), Validators.max(4)]],
      enrolledCredits: [
        this.student.enrolledCredits,
        [Validators.required, Validators.min(1), Validators.max(30), Validators.pattern('^[0-9]+$')]
      ],
      avatar: [this.student.avatar, [Validators.required]],
      bio: [this.student.bio, [Validators.required, Validators.minLength(10), Validators.maxLength(200)]],
      projects: this.fb.array([])
    });

    // Populate initial projects
    this.addProject('Student Course Portal', 'Angular, HTML, CSS');
    this.addProject('Microservices Framework', 'Spring Boot, Java, Docker');

    // Subscribe to form value changes to mirror updates to preview card in real-time
    this.profileForm.valueChanges.subscribe((value) => {
      this.student.name = value.name || '';
      this.student.department = value.department || '';
      this.student.email = value.email || '';
      this.student.bio = value.bio || '';
      this.student.gpa = parseFloat(value.gpa) || 0;
      this.student.enrolledCredits = parseInt(value.enrolledCredits, 10) || 0;
    });

    // Subscribe to shared enrollment credits count state
    this.enrollmentSub = this.enrollmentService.getEnrolledCreditsCount().subscribe((credits) => {
      this.student.enrolledCredits = credits;
      if (this.profileForm) {
        this.profileForm.patchValue({ enrolledCredits: credits }, { emitEvent: false });
      }
    });
  }

  get projects(): FormArray {
    return this.profileForm.get('projects') as FormArray;
  }

  addProject(title: string = '', tech: string = ''): void {
    const projectGroup = this.fb.group({
      title: [title, [Validators.required, Validators.minLength(3)]],
      tech: [tech, [Validators.required]]
    });
    this.projects.push(projectGroup);
  }

  removeProject(index: number): void {
    this.projects.removeAt(index);
  }

  onAvatarChange(avatar: string): void {
    this.profileForm.patchValue({ avatar });
    this.student.avatar = avatar;
  }

  onSubmit(): void {
    if (this.profileForm.valid) {
      // Commit changes to preview
      this.committedStudent = { ...this.committedStudent, ...this.profileForm.value };
      this.student = { ...this.student, ...this.profileForm.value };
      this.showSuccess = true;
      this.profileForm.markAsPristine();
      
      setTimeout(() => {
        this.showSuccess = false;
      }, 5000);
    }
  }

  onReset(): void {
    this.student = { ...this.committedStudent };
    this.profileForm.reset({
      name: this.student.name,
      email: this.student.email,
      department: this.student.department,
      gpa: this.student.gpa,
      enrolledCredits: this.student.enrolledCredits,
      avatar: this.student.avatar,
      bio: this.student.bio
    });

    // Reload baseline projects
    while (this.projects.length !== 0) {
      this.projects.removeAt(0);
    }
    this.addProject('Student Course Portal', 'Angular, HTML, CSS');
    this.addProject('Microservices Framework', 'Spring Boot, Java, Docker');

    this.showSuccess = false;
  }

  ngOnDestroy(): void {
    if (this.enrollmentSub) {
      this.enrollmentSub.unsubscribe();
    }
  }
}
