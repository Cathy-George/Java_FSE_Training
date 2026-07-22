import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

def build_pdf():
    pdf_filename = r"c:\JavaTrainingFSE\Week-5 Angular\HandsOn7_Report.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter,
                            rightMargin=54, leftMargin=54,
                            topMargin=54, bottomMargin=54)

    styles = getSampleStyleSheet()
    
    # Custom Styles for Premium Look
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#1e293b'),
        spaceAfter=15,
        alignment=1 # Center
    )
    
    subtitle_style = ParagraphStyle(
        'DocSub',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#4f46e5'),
        spaceAfter=20,
        alignment=1
    )
    
    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#1e293b'),
        spaceBefore=14,
        spaceAfter=6,
        borderPadding=4
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor('#4f46e5'),
        spaceBefore=8,
        spaceAfter=3
    )

    body_style = ParagraphStyle(
        'DocBody',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#334155'),
        spaceAfter=4
    )

    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=6.5,
        leading=8,
        textColor=colors.HexColor('#0f172a'),
        backColor=colors.HexColor('#f8fafc'),
        borderColor=colors.HexColor('#cbd5e1'),
        borderWidth=0.5,
        borderPadding=4,
        spaceBefore=3,
        spaceAfter=3
    )

    meta_style = ParagraphStyle(
        'MetaStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#475569')
    )

    story = []

    # --- COVER PAGE & GENERAL HEADER ---
    story.append(Spacer(1, 30))
    story.append(Paragraph("DIGITAL NURTURE 5.0", subtitle_style))
    story.append(Paragraph("Angular (v20+) Hands-On Lab Report", title_style))
    story.append(Paragraph("Incremental Project: Student Course Portal", subtitle_style))
    story.append(Spacer(1, 15))
    
    # Metadata Table
    meta_data = [
        [Paragraph("<b>Hands-On:</b>", meta_style), Paragraph("Hands-On 7 [Advanced-Professional]", meta_style)],
        [Paragraph("<b>Topic:</b>", meta_style), Paragraph("Advanced Routing, Dynamic Params, Guards & Lazy Loading", meta_style)],
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
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 30))
    story.append(PageBreak())

    # --- SECTION 2: OBJECTIVE ---
    story.append(Paragraph("1. Objective", h1_style))
    obj_text = ("The primary objective of this exercise is to implement an advanced, modern routing architecture inside "
                "the Student Course Portal. By integrating Lazy Loading across all major page components, we optimize "
                "the initial bundle size and application performance. We introduce parameterized routes for retrieving and "
                "rendering course details (Syllabus and Reviews nested tab components), bind ActivatedRoute query parameters "
                "to execute departmental lists filtering, and establish AuthGuard (CanActivate) security gates to block "
                "unauthorized profile pages access. Furthermore, we construct a CanDeactivate guard to prompt unsaved form "
                "modifications alerts, and implement a custom 404 Not Found fallback view.")
    story.append(Paragraph(obj_text, body_style))
    story.append(Spacer(1, 6))

    # --- SECTION 3: ANGULAR CONCEPTS COVERED ---
    story.append(Paragraph("2. Angular Concepts Covered", h1_style))
    concepts = [
        "<b>Lazy Loading (loadComponent):</b> Dynamically downloading component script bundles only when navigating to their respective routes, improving startup load speeds.",
        "<b>Route Parameters (paramMap):</b> Capturing dynamic URL path tokens (e.g. <code>/courses/:id</code>) to fetch and render specific resource records.",
        "<b>Query Parameters (queryParamMap):</b> Passing state filters through URL keys (e.g. <code>/courses?department=Computer Science</code>) to auto-initialize view filters.",
        "<b>Nested Child Routes (children):</b> Defining hierarchical routing nodes that load inside parent component sub-router outlets (e.g. Syllabus vs Reviews tabs).",
        "<b>Auth Guard (CanActivateFn):</b> Protecting private routes by running interceptor logic (e.g. checking simulated login session and redirecting unauthorized guests).",
        "<b>CanDeactivate Guard (CanDeactivateFn):</b> Protecting dirty input forms by prompting user confirmation checks before leaving the page.",
        "<b>Wildcard Routing (**):</b> Mapping unmatched paths to a dedicated fallback component (404 page)."
    ]
    for c in concepts:
        story.append(Paragraph(f"• {c}", body_style))
    story.append(Spacer(1, 6))

    # --- SECTION 4: ROUTE CONFIGURATION ---
    story.append(Paragraph("3. App Routes Configuration (src/app/app.routes.ts)", h1_style))
    routes_code = ("export const routes: Routes = [<br/>"
                   "  { path: '', loadComponent: () => import('./pages/home/home').then(m => m.Home) },<br/>"
                   "  { path: 'courses', loadComponent: () => import('./pages/course-list/course-list').then(m => m.CourseList) },<br/>"
                   "  {<br/>"
                   "    path: 'courses/:id',<br/>"
                   "    loadComponent: () => import('./pages/course-detail/course-detail').then(m => m.CourseDetail),<br/>"
                   "    children: [<br/>"
                   "      { path: '', redirectTo: 'syllabus', pathMatch: 'full' },<br/>"
                   "      { path: 'syllabus', loadComponent: () => import('./pages/course-detail/syllabus/syllabus').then(m => m.CourseSyllabus) },<br/>"
                   "      { path: 'reviews', loadComponent: () => import('./pages/course-detail/reviews/reviews').then(m => m.CourseReviews) }<br/>"
                   "    ]<br/>"
                   "  },<br/>"
                   "  {<br/>"
                   "    path: 'profile',<br/>"
                   "    loadComponent: () => import('./pages/student-profile/student-profile').then(m => m.StudentProfile),<br/>"
                   "    canActivate: [authGuard],<br/>"
                   "    canDeactivate: [canDeactivateProfile]<br/>"
                   "  },<br/>"
                   "  { path: 'login', loadComponent: () => import('./pages/login/login').then(m => m.Login) },<br/>"
                   "  { path: 'not-found', loadComponent: () => import('./pages/not-found/not-found').then(m => m.NotFound) },<br/>"
                   "  { path: '**', redirectTo: 'not-found' }<br/>"
                   "];")
    story.append(Paragraph(routes_code, code_style))
    story.append(PageBreak())

    # --- SECTION 5: GUARDS IMPLEMENTATION ---
    story.append(Paragraph("4. Route Guards Implementation", h1_style))
    
    story.append(Paragraph("CanActivate AuthGuard (src/app/services/auth.guard.ts)", h2_style))
    guard_code1 = ("export const authGuard: CanActivateFn = () => {<br/>"
                  "  const authService = inject(AuthService);<br/>"
                  "  const router = inject(Router);<br/>"
                  "  const notificationService = inject(NotificationService);<br/><br/>"
                  "  if (authService.isAuthenticated()) { return true; }<br/>"
                  "  else {<br/>"
                  "    notificationService.show('Please log in to view the profile page.', 'warning');<br/>"
                  "    router.navigate(['/login']);<br/>"
                  "    return false;<br/>"
                  "  }<br/>"
                  "};")
    story.append(Paragraph(guard_code1, code_style))
    
    story.append(Paragraph("CanDeactivate Guard (src/app/services/deactivate.guard.ts)", h2_style))
    guard_code2 = ("export const canDeactivateProfile: CanDeactivateFn&lt;StudentProfile&gt; = (component) => {<br/>"
                  "  if (component.profileForm && component.profileForm.dirty && !component.showSuccess) {<br/>"
                  "    return confirm('You have unsaved changes. Do you really want to leave this page?');<br/>"
                  "  }<br/>"
                  "  return true;<br/>"
                  "};")
    story.append(Paragraph(guard_code2, code_style))
    story.append(Spacer(1, 8))

    # --- SECTION 6: SCREENSHOTS ---
    story.append(Paragraph("5. Captured Screenshots & Verification", h1_style))
    story.append(Paragraph("All routing views, param states, and guards were verified in the browser:", body_style))

    img_paths = [
        (r"C:\Users\User\.gemini\antigravity-ide\brain\474ec060-196f-4617-a15e-ca09b2cd8671\profile_h7_home_filters.png", 
         "Home page displaying new departmental shortcuts mapped to routing links with query parameters"),
        (r"C:\Users\User\.gemini\antigravity-ide\brain\474ec060-196f-4617-a15e-ca09b2cd8671\profile_h7_courses_filtered.png", 
         "Courses view auto-filtered to 'Computer Science' after navigating from the home shortcut card"),
        (r"C:\Users\User\.gemini\antigravity-ide\brain\474ec060-196f-4617-a15e-ca09b2cd8671\profile_h7_course_syllabus.png", 
         "Course details view (/courses/2) displaying dynamic course metadata and rendering nested Syllabus component"),
        (r"C:\Users\User\.gemini\antigravity-ide\brain\474ec060-196f-4617-a15e-ca09b2cd8671\profile_h7_course_reviews.png", 
         "Nested reviews route (/courses/2/reviews) displaying ratings and student reviews"),
        (r"C:\Users\User\.gemini\antigravity-ide\brain\474ec060-196f-4617-a15e-ca09b2cd8671\profile_h7_not_found.png", 
         "Fallback wildcard routing redirecting unmatched URLs to a dedicated custom 404 NotFound page"),
        (r"C:\Users\User\.gemini\antigravity-ide\brain\474ec060-196f-4617-a15e-ca09b2cd8671\profile_h7_deactivate_guard.png", 
         "CanDeactivate guard intercepting page departure and prompting dirty form discard warnings"),
        (r"C:\Users\User\.gemini\antigravity-ide\brain\474ec060-196f-4617-a15e-ca09b2cd8671\profile_h7_auth_redirect.png", 
         "AuthGuard blocking unauthorized access to /profile when logged out, redirecting to login page with alert toast")
    ]
    
    for path, caption in img_paths:
        if os.path.exists(path):
            try:
                img = Image(path, width=4.5*inch, height=2.4*inch)
                story.append(Paragraph(f"<b>Screenshot:</b> {caption}", h2_style))
                story.append(img)
                story.append(Spacer(1, 8))
            except Exception as e:
                story.append(Paragraph(f"[Image Render Error: {str(e)}]", body_style))
        else:
            story.append(Paragraph(f"<b>[Screenshot Placeholder]:</b> {caption} (File not found at: {path})", body_style))

    story.append(PageBreak())

    # --- SECTION 7: TESTING & RESULTS ---
    story.append(Paragraph("6. Unit Test Executions", h1_style))
    story.append(Paragraph("All routing modifications and service components compiled cleanly. All unit tests successfully executed and passed in the Vitest test runner. The test output confirms passing specs across all modules.", body_style))
    story.append(Spacer(1, 6))

    # --- SECTION 8: LEARNING OUTCOMES ---
    story.append(Paragraph("7. Learning Outcomes & Conclusion", h1_style))
    learnings = [
        "Configured lazy loading on standalone page components to speed up startup load speeds.",
        "Captured dynamic path tokens using ActivatedRoute ParamMap subscriptions to load granular item records.",
        "Filtered dataset lists based on incoming query parameter tokens.",
        "Protected state paths using Auth guards and dirty-state CanDeactivate confirm overlays.",
        "Set up wildcard fallback routes to render dedicated custom error views.",
        "Resolved routing dependencies and providers inside spec testing harnesses."
    ]
    for l in learnings:
        story.append(Paragraph(f"✓ {l}", body_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Conclusion", h1_style))
    concl_text = ("Hands-On 7 successfully completes the navigation architecture of the Student Course Portal. "
                  "The application incorporates modular lazy loading, route safety guards, nested child views, "
                  "and search state query bindings, meeting all standard enterprise routing criteria.")
    story.append(Paragraph(concl_text, body_style))

    doc.build(story)
    print("PDF Report compiled successfully at:", pdf_filename)

if __name__ == '__main__':
    build_pdf()
