import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

def build_pdf():
    pdf_filename = r"c:\JavaTrainingFSE\Week-5 Angular\HandsOn5_Report.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter,
                            rightMargin=54, leftMargin=54,
                            topMargin=54, bottomMargin=54)

    styles = getSampleStyleSheet()
    
    # Custom Styles for Premium Look
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=colors.HexColor('#1e293b'),
        spaceAfter=15,
        alignment=1 # Center
    )
    
    subtitle_style = ParagraphStyle(
        'DocSub',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#4f46e5'),
        spaceAfter=25,
        alignment=1
    )
    
    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=17,
        textColor=colors.HexColor('#1e293b'),
        spaceBefore=15,
        spaceAfter=6,
        borderPadding=4
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#4f46e5'),
        spaceBefore=8,
        spaceAfter=3
    )

    body_style = ParagraphStyle(
        'DocBody',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#334155'),
        spaceAfter=5
    )

    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7,
        leading=9,
        textColor=colors.HexColor('#0f172a'),
        backColor=colors.HexColor('#f8fafc'),
        borderColor=colors.HexColor('#cbd5e1'),
        borderWidth=0.5,
        borderPadding=5,
        spaceBefore=3,
        spaceAfter=3
    )

    meta_style = ParagraphStyle(
        'MetaStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#475569')
    )

    story = []

    # --- COVER PAGE & GENERAL HEADER ---
    story.append(Spacer(1, 40))
    story.append(Paragraph("DIGITAL NURTURE 5.0", subtitle_style))
    story.append(Paragraph("Angular (v20+) Hands-On Lab Report", title_style))
    story.append(Paragraph("Incremental Project: Student Course Portal", subtitle_style))
    story.append(Spacer(1, 15))
    
    # Metadata Table
    meta_data = [
        [Paragraph("<b>Hands-On:</b>", meta_style), Paragraph("Hands-On 5 [Advanced]", meta_style)],
        [Paragraph("<b>Topic:</b>", meta_style), Paragraph("Reactive Forms, Custom Sync/Async Validators & FormArrays", meta_style)],
        [Paragraph("<b>Developer:</b>", meta_style), Paragraph("Cathy George", meta_style)],
        [Paragraph("<b>OS Version:</b>", meta_style), Paragraph("Windows 11", meta_style)],
        [Paragraph("<b>Date:</b>", meta_style), Paragraph("July 22, 2026", meta_style)],
        [Paragraph("<b>Track:</b>", meta_style), Paragraph("Java FSE Angular Track", meta_style)]
    ]
    t_meta = Table(meta_data, colWidths=[2.0 * inch, 4.5 * inch])
    t_meta.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#f1f5f9')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 40))
    story.append(PageBreak())

    # --- SECTION 2: OBJECTIVE ---
    story.append(Paragraph("1. Objective", h1_style))
    obj_text = ("The primary objective of this exercise is to implement and configure a fully Reactive Form inside the "
                "Student Profile component of the portal using Angular's ReactiveFormsModule. We replace template-driven directives "
                "with an explicitly constructed component-side FormGroup tree managed via FormBuilder. Key goals include implementing a custom "
                "synchronous domain-restricting validator, writing an asynchronous uniqueness check validator with RxJS simulated timer "
                "delays, managing a list of academic project sub-form controls dynamically using FormArray, and binding error validation status "
                "reactively in the template to create a premium, responsive UX.")
    story.append(Paragraph(obj_text, body_style))
    story.append(Spacer(1, 8))

    # --- SECTION 3: ANGULAR CONCEPTS COVERED ---
    story.append(Paragraph("2. Angular Concepts Covered", h1_style))
    concepts = [
        "<b>Reactive Forms (ReactiveFormsModule):</b> Modeling forms explicitly inside the TypeScript class code. Offers robust unit-testability, programmatic form changes, and synchronous/asynchronous validator bindings.",
        "<b>FormBuilder & FormGroup:</b> Syntactic sugar mapping form fields into a unified tree hierarchy control model containing FormGroups and FormArrays.",
        "<b>FormArray:</b> A dynamic collection of FormControls or FormGroups. Used here to permit students to dynamically append and remove academic projects in real-time.",
        "<b>Custom Sync Validator:</b> Component-side rule functions returning ValidationErrors. Implemented as <code>universityEmailValidator()</code> which restricts emails to the <code>@university.edu</code> domain.",
        "<b>Async Validator:</b> Asynchronous checking functions returning Observables or Promises. Implemented as <code>emailUniqueValidator()</code> using an RxJS <code>timer(800)</code> debounce delay to mock network queries checking if an email is taken.",
        "<b>Dynamic Control Manipulations:</b> Exposing methods like <code>addProject()</code> and <code>removeProject(i)</code> that alter the FormArray control count at runtime.",
        "<b>Reactive Validation Feedback:</b> Displaying error messages and disabling submit buttons by directly querying <code>profileForm.get('field')?.errors</code> status changes in the template."
    ]
    for c in concepts:
        story.append(Paragraph(f"• {c}", body_style))
    story.append(Spacer(1, 8))

    # --- SECTION 4: SOFTWARE USED ---
    story.append(Paragraph("3. Software & Tools Used", h1_style))
    sw_data = [
        [Paragraph("<b>Software / Tool</b>", meta_style), Paragraph("<b>Version / URL</b>", meta_style)],
        [Paragraph("Node.js + npm", meta_style), Paragraph("v22.20.0 (LTS 20+) / npm 10.9.3", meta_style)],
        [Paragraph("Angular CLI", meta_style), Paragraph("v21.2.16", meta_style)],
        [Paragraph("Vitest Runner", meta_style), Paragraph("v4.1.10", meta_style)],
        [Paragraph("PDF Generator", meta_style), Paragraph("Python 3.14 + ReportLab library", meta_style)]
    ]
    t_sw = Table(sw_data, colWidths=[2.5 * inch, 4.0 * inch])
    t_sw.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_sw)
    story.append(Spacer(1, 8))

    # --- SECTION 5: PROJECT STRUCTURE ---
    story.append(Paragraph("4. Project Folder Structure", h1_style))
    folder_text = ("student-course-portal/<br/>"
                   "└── src/<br/>"
                   "    └── app/<br/>"
                   "        ├── validators/<br/>"
                   "        │   └── profile.validators.ts (Custom domain sync & async email taken validators)<br/>"
                   "        └── pages/<br/>"
                   "            └── student-profile/<br/>"
                   "                ├── student-profile.ts (FormBuilder Reactive configuration, FormArray logic, onReset)<br/>"
                   "                ├── student-profile.html (Reactive formGroup and formArrayName templates bindings)<br/>"
                   "                ├── student-profile.css (FormArray projects card grids and pending loading dot styles)<br/>"
                   "                └── student-profile.spec.ts (Vitest specs testing async validators, resets and array sizes)")
    story.append(Paragraph(folder_text, code_style))
    story.append(Spacer(1, 8))
    story.append(PageBreak())

    # --- SECTION 6: KEY CODE IMPLEMENTATION ---
    story.append(Paragraph("5. Key Code Implementation Details", h1_style))
    
    story.append(Paragraph("Custom Synchronous & Asynchronous Validators (src/app/validators/profile.validators.ts)", h2_style))
    val_code = ("export function universityEmailValidator(): ValidatorFn {<br/>"
                "  return (control: AbstractControl): ValidationErrors | null => {<br/>"
                "    const val = control.value;<br/>"
                "    if (!val) return null;<br/>"
                "    return val.toLowerCase().endsWith('@university.edu') ? null : { invalidDomain: true };<br/>"
                "  };<br/>"
                "}<br/><br/>"
                "export function emailUniqueValidator(): AsyncValidatorFn {<br/>"
                "  return (control: AbstractControl): Observable&lt;ValidationErrors | null&gt; => {<br/>"
                "    const val = control.value;<br/>"
                "    if (!val) return timer(0).pipe(map(() => null));<br/>"
                "    return timer(800).pipe(<br/>"
                "      map(() => {<br/>"
                "        const takenEmails = ['taken@university.edu', 'admin@university.edu', 'already.registered@university.edu'];<br/>"
                "        return takenEmails.includes(val.toLowerCase()) ? { emailTaken: true } : null;<br/>"
                "      })<br/>"
                "    );<br/>"
                "  };<br/>"
                "}")
    story.append(Paragraph(val_code, code_style))
    
    story.append(Paragraph("Student Profile Component Initialization & FormArray Logic (src/app/pages/student-profile/student-profile.ts)", h2_style))
    ts_code = ("this.profileForm = this.fb.group({<br/>"
               "  name: [this.student.name, [Validators.required, Validators.minLength(3), Validators.pattern('^[a-zA-Z\\\\s]*$')]],<br/>"
               "  email: [this.student.email, [Validators.required, Validators.email, universityEmailValidator()], [emailUniqueValidator()]],<br/>"
               "  department: [this.student.department, [Validators.required, Validators.minLength(4)]],<br/>"
               "  gpa: [this.student.gpa, [Validators.required, Validators.min(0), Validators.max(4)]],<br/>"
               "  enrolledCredits: [this.student.enrolledCredits, [Validators.required, Validators.min(1), Validators.max(30), Validators.pattern('^[0-9]+$')]],<br/>"
               "  avatar: [this.student.avatar, [Validators.required]],<br/>"
               "  bio: [this.student.bio, [Validators.required, Validators.minLength(10), Validators.maxLength(200)]],<br/>"
               "  projects: this.fb.array([])<br/>"
               "});<br/><br/>"
               "get projects(): FormArray {<br/>"
               "  return this.profileForm.get('projects') as FormArray;<br/>"
               "}<br/>"
               "addProject(title: string = '', tech: string = ''): void {<br/>"
               "  this.projects.push(this.fb.group({<br/>"
               "    title: [title, [Validators.required, Validators.minLength(3)]],<br/>"
               "    tech: [tech, [Validators.required]]<br/>"
               "  }));<br/>"
               "}<br/>"
               "removeProject(index: number): void {<br/>"
               "  this.projects.removeAt(index);<br/>"
               "}")
    story.append(Paragraph(ts_code, code_style))
    story.append(PageBreak())

    story.append(Paragraph("Template Markup for FormArray Loops & Pending Status (src/app/pages/student-profile/student-profile.html)", h2_style))
    html_code = ("&lt;div *ngIf=\"profileForm.get('email')?.pending\" class=\"pending-msg\"&gt;<br/>"
                 "  &lt;span class=\"pulse-dot\"&gt;&lt;/span&gt; Checking email uniqueness...<br/>"
                 "&lt;/div&gt;<br/>"
                 "&lt;div *ngIf=\"profileForm.get('email')?.invalid && (profileForm.get('email')?.touched || profileForm.get('email')?.dirty)\" class=\"error-msg\"&gt;<br/>"
                 "  &lt;span *ngIf=\"profileForm.get('email')?.errors?.['invalidDomain']\"&gt;Email must end with @university.edu.&lt;/span&gt;<br/>"
                 "  &lt;span *ngIf=\"profileForm.get('email')?.errors?.['emailTaken']\"&gt;This email is already taken.&lt;/span&gt;<br/>"
                 "&lt;/div&gt;<br/><br/>"
                 "&lt;div formArrayName=\"projects\" class=\"projects-list\"&gt;<br/>"
                 "  &lt;div *ngFor=\"let proj of projects.controls; let i=index\" [formGroupName]=\"i\" class=\"project-item\"&gt;<br/>"
                 "    &lt;input type=\"text\" formControlName=\"title\" placeholder=\"Project Title\" class=\"form-input\" /&gt;<br/>"
                 "    &lt;input type=\"text\" formControlName=\"tech\" placeholder=\"Technologies\" class=\"form-input\" /&gt;<br/>"
                 "    &lt;button type=\"button\" class=\"btn-remove-project\" (click)=\"removeProject(i)\"&gt;×&lt;/button&gt;<br/>"
                 "  &lt;/div&gt;<br/>"
                 "&lt;/div&gt;")
    story.append(Paragraph(html_code, code_style))
    story.append(Spacer(1, 8))

    # --- SECTION 7: SCREENSHOTS ---
    story.append(Paragraph("6. Captured Screenshots & Verification", h1_style))
    story.append(Paragraph("All application features were fully verified in the browser:", body_style))

    img_paths = [
        (r"C:\Users\User\.gemini\antigravity-ide\brain\f2fb0647-8016-412c-94ac-d4c721e05542\profile_h5_initial_1784715673257.png", 
         "Initial loaded Student Profile with Reactive form states, FormBuilder initial mapping, and projects list from FormArray"),
        (r"C:\Users\User\.gemini\antigravity-ide\brain\f2fb0647-8016-412c-94ac-d4c721e05542\profile_h5_invalid_1784715762734.png", 
         "Form showing validation errors: name pattern mismatch, department too short, sync domain validation failure, and async validator marking email taken error"),
        (r"C:\Users\User\.gemini\antigravity-ide\brain\f2fb0647-8016-412c-94ac-d4c721e05542\profile_h5_submitted_1784715967413.png", 
         "Form submitted successfully, success banner visible, with the newly added academic project ('Distributed Database Store') visible in the FormArray list")
    ]
    
    for path, caption in img_paths:
        if os.path.exists(path):
            try:
                img = Image(path, width=4.5*inch, height=2.8*inch)
                story.append(Paragraph(f"<b>Screenshot:</b> {caption}", h2_style))
                story.append(img)
                story.append(Spacer(1, 8))
            except Exception as e:
                story.append(Paragraph(f"[Image Render Error: {str(e)}]", body_style))
        else:
            story.append(Paragraph(f"<b>[Screenshot Placeholder]:</b> {caption} (File not found at: {path})", body_style))

    story.append(PageBreak())

    # --- SECTION 8: OUTPUTS ---
    story.append(Paragraph("7. Output & Behavioral Explanations", h1_style))
    out_text = ("• <b>Reactive Form Model:</b> We instantiated a TypeScript object using <code>fb.group()</code>. Unlike templates, "
                "this gives the component programmatic command over validity tracking and field manipulations.<br/>"
                "• <b>Custom Domain Synchronous Validator:</b> The <code>universityEmailValidator()</code> restricts email field inputs to "
                "domains ending in <code>@university.edu</code>. If invalid, the FormControl receives the <code>{ invalidDomain: true }</code> error.<br/>"
                "• <b>Asynchronous Uniqueness Validator:</b> The <code>emailUniqueValidator()</code> returns an Observable timer. While checking "
                "database status, the email control transitions to a PENDING status, triggering a spinner overlay. If the input matches a registered email, "
                "it returns <code>{ emailTaken: true }</code>.<br/>"
                "• <b>FormArray Dynamic Controls:</b> The projects sub-structure array represents a collection of FormGroups. Users can append items "
                "using <code>projects.push()</code> or remove items via index <code>projects.removeAt(i)</code> dynamically inside the view.<br/>"
                "• <b>Rollback capability (onReset):</b> Calling <code>profileForm.reset()</code> and recreating FormArray controls reverts inputs to "
                "committed models while cleaning validation flags.")
    story.append(Paragraph(out_text, body_style))
    story.append(Spacer(1, 8))

    # --- SECTION 9: LEARNINGS & CONCLUSION ---
    story.append(Paragraph("8. Learning Outcomes & Conclusion", h1_style))
    learnings = [
        "Constructed advanced Reactive Forms in Angular using ReactiveFormsModule, FormBuilder, and FormGroup models.",
        "Built dynamic controls inside views by utilizing FormArray arrays containing multiple sub-groups.",
        "Implemented custom validation rules checking synchronous domains and asynchronous unique criteria with debounce timers.",
        "Created loading visual states indicating when async validators are query-pending.",
        "Asserted validation states, FormArray insertions/deletions, and async status updates through Vitest testing."
    ]
    for l in learnings:
        story.append(Paragraph(f"✓ {l}", body_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph("9. Conclusion", h1_style))
    concl_text = ("Hands-On 5 successfully transitions the Student Profile page form implementation from a basic Template-driven "
                  "architecture into a programmatically managed Reactive Form. Utilizing advanced custom and asynchronous validators, "
                  "dynamic FormArray listings, and real-time validation checks, the form provides clean data entry logic, comprehensive "
                  "unit-testing interfaces, and a premium responsive user experience.")
    story.append(Paragraph(concl_text, body_style))

    doc.build(story)
    print("PDF Report compiled successfully at:", pdf_filename)

if __name__ == '__main__':
    build_pdf()
