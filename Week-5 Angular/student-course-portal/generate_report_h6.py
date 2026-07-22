import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

def build_pdf():
    pdf_filename = r"c:\JavaTrainingFSE\Week-5 Angular\HandsOn6_Report.pdf"
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
        [Paragraph("<b>Hands-On:</b>", meta_style), Paragraph("Hands-On 6 [Advanced-Professional]", meta_style)],
        [Paragraph("<b>Topic:</b>", meta_style), Paragraph("Services, Dependency Injection & Shared Reactive State", meta_style)],
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
    obj_text = ("The primary objective of this exercise is to architect a highly modular, decoupled state management "
                "system using Angular Services, Dependency Injection, and the Singleton pattern. By developing three "
                "dedicated services—CourseService for course list data, EnrollmentService for student enrollment tracking "
                "and credit calculations, and NotificationService for application-wide push alerts—we establish a "
                "unified Shared State model. This enables the navigation bar badge count, course cards toggle status, "
                "student profile credit summaries, and floating notification alerts to update reactively and synchronously "
                "as course states transition.")
    story.append(Paragraph(obj_text, body_style))
    story.append(Spacer(1, 8))

    # --- SECTION 3: ANGULAR CONCEPTS COVERED ---
    story.append(Paragraph("2. Angular Concepts Covered", h1_style))
    concepts = [
        "<b>Angular Services:</b> Dedicated class files separating business, data, and state logic from template controllers, ensuring code modularity and high reusability.",
        "<b>Dependency Injection (DI):</b> Design pattern where Angular resolves and injects classes automatically via constructors (e.g. <code>constructor(private courseService: CourseService)</code>).",
        "<b>Singleton Services:</b> Declaring services with <code>providedIn: 'root'</code>. This ensures only a single instance of the service exists globally, forming a perfect anchor for application state sharing.",
        "<b>State Sharing (BehaviorSubject/Observable):</b> Emitting real-time updates through RxJS streams. Multiple independent components subscribe to the same singleton stream to mirror data changes synchronously.",
        "<b>Service Collaboration:</b> Injecting services into other services (e.g. <code>EnrollmentService</code> injects <code>NotificationService</code> to dispatch toasts upon enrollment transitions)."
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
                   "        ├── services/ (Singleton Services)<br/>"
                   "        │   ├── course.service.ts (Master Course data subject)<br/>"
                   "        │   ├── enrollment.service.ts (Reactive enrollment set & credits calculations)<br/>"
                   "        │   └── notification.service.ts (Broadcasts global toasts alert events)<br/>"
                   "        ├── components/<br/>"
                   "        │   └── header/ (Injects EnrollmentService for Dynamic Badge count display)<br/>"
                   "        └── pages/<br/>"
                   "            ├── course-list/ (Delegates toggles and modifications to Course and Enrollment service)<br/>"
                   "            └── student-profile/ (Listens to EnrolledCreditsCount and updates form to readonly)")
    story.append(Paragraph(folder_text, code_style))
    story.append(Spacer(1, 8))
    story.append(PageBreak())

    # --- SECTION 6: KEY CODE IMPLEMENTATION ---
    story.append(Paragraph("5. Key Code Implementation Details", h1_style))
    
    story.append(Paragraph("Enrollment Service - Shared Reactive State (src/app/services/enrollment.service.ts)", h2_style))
    enr_code = ("@Injectable({ providedIn: 'root' })<br/>"
                "export class EnrollmentService {<br/>"
                "  private enrolledCourseIdsSubject = new BehaviorSubject&lt;Set&lt;number&gt;&gt;(new Set([2, 5]));<br/><br/>"
                "  constructor(private courseService: CourseService, private notificationService: NotificationService) {}<br/><br/>"
                "  getEnrolledCourseIds(): Observable&lt;Set&lt;number&gt;&gt; {<br/>"
                "    return this.enrolledCourseIdsSubject.asObservable();<br/>"
                "  }<br/><br/>"
                "  getEnrolledCreditsCount(): Observable&lt;number&gt; {<br/>"
                "    return combineLatest([<br/>"
                "      this.courseService.getCourses(),<br/>"
                "      this.enrolledCourseIdsSubject.asObservable()<br/>"
                "    ]).pipe(<br/>"
                "      map(([courses, enrolledIds]) => courses<br/>"
                "        .filter(c => enrolledIds.has(c.id))<br/>"
                "        .reduce((sum, c) => sum + c.credits, 0))<br/>"
                "    );<br/>"
                "  }<br/><br/>"
                "  enrollCourse(course: Course): void {<br/>"
                "    const ids = new Set(this.enrolledCourseIdsSubject.value);<br/>"
                "    if (!ids.has(course.id)) {<br/>"
                "      ids.add(course.id);<br/>"
                "      this.enrolledCourseIdsSubject.next(ids);<br/>"
                "      this.notificationService.show(`Enrolled in ${course.code} successfully!`);<br/>"
                "    }<br/>"
                "  }<br/>"
                "}")
    story.append(Paragraph(enr_code, code_style))
    
    story.append(Paragraph("CourseList Component Reactive Subscriptions (src/app/pages/course-list/course-list.ts)", h2_style))
    ts_code = ("export class CourseList implements OnInit, OnDestroy {<br/>"
               "  courses: Course[] = [];<br/>"
               "  private stateSub!: Subscription;<br/><br/>"
               "  constructor(private courseService: CourseService, private enrollmentService: EnrollmentService) {}<br/><br/>"
               "  ngOnInit(): void {<br/>"
               "    this.stateSub = combineLatest([<br/>"
               "      this.courseService.getCourses(),<br/>"
               "      this.enrollmentService.getEnrolledCourseIds()<br/>"
               "    ]).subscribe(([courses, enrolledIds]) => {<br/>"
               "      this.courses = courses.map((c) => ({<br/>"
               "        ...c,<br/>"
               "        enrolled: enrolledIds.has(c.id)<br/>"
               "      }));<br/>"
               "    });<br/>"
               "  }<br/><br/>"
               "  onEnrollmentToggled(id: number): void {<br/>"
               "    const course = this.courses.find(c => c.id === id);<br/>"
               "    if (course) {<br/>"
               "      if (course.enrolled) { this.enrollmentService.unenrollCourse(course); }<br/>"
               "      else { this.enrollmentService.enrollCourse(course); }<br/>"
               "    }<br/>"
               "  }<br/>"
               "}")
    story.append(Paragraph(ts_code, code_style))
    story.append(PageBreak())

    story.append(Paragraph("App Shell Layout with Notification Toast Overlay (src/app/app.html)", h2_style))
    html_code = ("&lt;app-header&gt;&lt;/app-header&gt;<br/>"
                 "&lt;main class=\"container\"&gt;<br/>"
                 "  &lt;router-outlet&gt;&lt;/router-outlet&gt;<br/>"
                 "&lt;/main&gt;<br/><br/>"
                 "&lt;!-- Global Notification Toast Overlay --&gt;<br/>"
                 "&lt;div class=\"notification-container\"&gt;<br/>"
                 "  &lt;div *ngFor=\"let notification of activeNotifications\" class=\"toast-alert\" [class.success]=\"...\"&gt;<br/>"
                 "    &lt;span class=\"toast-icon\"&gt;✓&lt;/span&gt;<br/>"
                 "    &lt;span class=\"toast-message\"&gt;{{ notification.message }}&lt;/span&gt;<br/>"
                 "    &lt;button (click)=\"dismissNotification(notification.id)\" class=\"toast-close\"&gt;×&lt;/button&gt;<br/>"
                 "  &lt;/div&gt;<br/>"
                 "&lt;/div&gt;")
    story.append(Paragraph(html_code, code_style))
    story.append(Spacer(1, 8))

    # --- SECTION 7: SCREENSHOTS ---
    story.append(Paragraph("6. Captured Screenshots & Verification", h1_style))
    story.append(Paragraph("All application features were fully verified in the browser:", body_style))

    img_paths = [
        (r"C:\Users\User\.gemini\antigravity-ide\brain\f2fb0647-8016-412c-94ac-d4c721e05542\profile_h6_courses_initial_1784716755265.png", 
         "Initial Course List view with two default courses enrolled (CS-402, IT-440), showing '2' as header courses badge"),
        (r"C:\Users\User\.gemini\antigravity-ide\brain\f2fb0647-8016-412c-94ac-d4c721e05542\profile_h6_enrolled_toast_1784716832277.png", 
         "Dynamic state update: Enrolled in Database Management (CS-205), showing global success notification toast sliding in and header badge count updating to '3' instantly"),
        (r"C:\Users\User\.gemini\antigravity-ide\brain\f2fb0647-8016-412c-94ac-d4c721e05542\profile_h6_profile_credits_1784716880264.png", 
         "Shared State validation: Student Profile page's Enrolled Credits input control set to 'readonly' and automatically displaying '10' total credits")
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
    out_text = ("• <b>Singleton Services (`providedIn: 'root'`):</b> All three services operate as application singletons. "
                "When a component like CourseList modifies the state, other modules immediately reflect the new values.<br/>"
                "• <b>Shared State Reactivity:</b> By combining CourseService courses and EnrollmentService IDs streams in "
                "combineLatest, components automatically rebuild with correct enrolled status flags.<br/>"
                "• <b>Navigation Badge Synchronization:</b> The header component subscribes to the enrolled ID set, updating the count "
                "instantly as courses are toggled. This creates a cohesive cart/enrollment experience.<br/>"
                "• <b>Profile Credits Synchronization:</b> The student profile component listens to the credits calculation stream, "
                "setting the input box values and stat cards. Decoupling this logic prevents human entries and locks it `readonly`.<br/>"
                "• <b>Global Toast Notification Pipeline:</b> The App root component acts as a display host. Whenever EnrollmentService "
                "issues an alert, the notification stream catches the event and spawns a toast, auto-dismissing after 4 seconds.")
    story.append(Paragraph(out_text, body_style))
    story.append(Spacer(1, 8))

    # --- SECTION 9: LEARNINGS & CONCLUSION ---
    story.append(Paragraph("8. Learning Outcomes & Conclusion", h1_style))
    learnings = [
        "Created singleton services in Angular leveraging constructor Dependency Injection parameters.",
        "Managed shared reactive states using BehaviorSubjects, observables, and combineLatest mappings.",
        "Created dynamic UI synchronization between independent page views and header navigation components.",
        "Built global message warning pipelines displaying temporary float toasts.",
        "Asserted service transactions and reactive view transformations through Vitest testing."
    ]
    for l in learnings:
        story.append(Paragraph(f"✓ {l}", body_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph("9. Conclusion", h1_style))
    concl_text = ("Hands-On 6 successfully implements singleton services, constructor dependency injections, "
                  "and a reactive shared state architecture within the portal. The seamless interaction between "
                  "CourseService, EnrollmentService, and NotificationService provides robust data consistency and "
                  "a premium, synchronous user experience across all navigation pages.")
    story.append(Paragraph(concl_text, body_style))

    doc.build(story)
    print("PDF Report compiled successfully at:", pdf_filename)

if __name__ == '__main__':
    build_pdf()
