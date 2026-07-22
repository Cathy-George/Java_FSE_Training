import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

def build_pdf():
    pdf_filename = r"c:\JavaTrainingFSE\Week-5 Angular\HandsOn2_Report.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter,
                            rightMargin=54, leftMargin=54,
                            topMargin=54, bottomMargin=54)

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=colors.HexColor('#1e293b'),
        spaceAfter=15,
        alignment=1
    )
    
    subtitle_style = ParagraphStyle(
        'DocSub',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#4f46e5'),
        spaceAfter=30,
        alignment=1
    )
    
    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=colors.HexColor('#1e293b'),
        spaceBefore=18,
        spaceAfter=8,
        borderPadding=4
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor('#4f46e5'),
        spaceBefore=10,
        spaceAfter=4
    )

    body_style = ParagraphStyle(
        'DocBody',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#334155'),
        spaceAfter=6
    )

    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor('#0f172a'),
        backColor=colors.HexColor('#f8fafc'),
        borderColor=colors.HexColor('#cbd5e1'),
        borderWidth=0.5,
        borderPadding=6,
        spaceBefore=4,
        spaceAfter=4
    )

    meta_style = ParagraphStyle(
        'MetaStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#475569')
    )

    story = []

    story.append(Spacer(1, 40))
    story.append(Paragraph("DIGITAL NURTURE 5.0", subtitle_style))
    story.append(Paragraph("Angular (v20+) Hands-On Lab Report", title_style))
    story.append(Paragraph("Incremental Project: Student Course Portal", subtitle_style))
    story.append(Spacer(1, 20))
    
    meta_data = [
        [Paragraph("<b>Hands-On:</b>", meta_style), Paragraph("Hands-On 2 [Intermediate]", meta_style)],
        [Paragraph("<b>Topic:</b>", meta_style), Paragraph("Data Binding, Lifecycle Hooks & Component Communication", meta_style)],
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

    story.append(Paragraph("1. Objective", h1_style))
    obj_text = ("The primary objective of this exercise is to implement core Angular data binding "
                "concepts (Interpolation, Property Binding, Event Binding, and Two-way Binding using ngModel), "
                "establish robust Parent-Child Component Communication using @Input, @Output, and EventEmitter, "
                "and demonstrate the execution of Angular Lifecycle Hooks (ngOnInit, ngOnChanges, and ngOnDestroy).")
    story.append(Paragraph(obj_text, body_style))
    story.append(Spacer(1, 10))

    story.append(Paragraph("2. Angular Concepts Covered", h1_style))
    concepts = [
        "<b>Property Binding:</b> Dynamically binding DOM property values like disabled states or CSS class modifications [class.enrolled].",
        "<b>Event Binding:</b> Capturing user interactions (e.g., clicks) to execute handler logic in the component class.",
        "<b>Interpolation:</b> Rendering component properties and logic results directly in templates using double curly braces.",
        "<b>Two-way Binding & ngModel:</b> Synchronizing model data and form inputs bi-directionally (e.g. search filter and student profile form fields).",
        "<b>Component Communication:</b> Passing course details to children via @Input() and notifying the parent page of updates using @Output() and EventEmitter.",
        "<b>Lifecycle Hooks:</b> ObservingOnInit for data initialization, OnChanges for reacting to dynamic input changes, and OnDestroy for component cleanup."
    ]
    for c in concepts:
        story.append(Paragraph(f"• {c}", body_style))
    story.append(Spacer(1, 10))

    story.append(Paragraph("3. Software & Tools Used", h1_style))
    sw_data = [
        [Paragraph("<b>Software / Tool</b>", meta_style), Paragraph("<b>Version / URL</b>", meta_style)],
        [Paragraph("Node.js + npm", meta_style), Paragraph("v22.20.0 (LTS 20+) / npm 10.9.3", meta_style)],
        [Paragraph("Angular CLI", meta_style), Paragraph("v21.2.16", meta_style)],
        [Paragraph("Vitest Runner", meta_style), Paragraph("v4.1.10", meta_style)],
        [Paragraph("Code Editor", meta_style), Paragraph("VS Code with Angular Language Service Extension", meta_style)],
        [Paragraph("PDF Generator", meta_style), Paragraph("Python 3.14 + ReportLab library", meta_style)]
    ]
    t_sw = Table(sw_data, colWidths=[2.5 * inch, 4.0 * inch])
    t_sw.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_sw)
    story.append(Spacer(1, 10))

    story.append(Paragraph("4. Project Folder Structure", h1_style))
    folder_text = ("student-course-portal/<br/>"
                   "├── angular.json<br/>"
                   "└── src/<br/>"
                   "    └── app/<br/>"
                   "        ├── models/<br/>"
                   "        │   └── course.model.ts (Course domain structure)<br/>"
                   "        ├── components/<br/>"
                   "        │   ├── header/ (Navigation header)<br/>"
                   "        │   └── course-card/ (Reusable child card component)<br/>"
                   "        └── pages/<br/>"
                   "            ├── home/ (Main welcome landing)<br/>"
                   "            ├── course-list/ (Parent course manager)<br/>"
                   "            └── student-profile/ (Editable details form & mirror preview)")
    story.append(Paragraph(folder_text, code_style))
    story.append(Spacer(1, 10))
    story.append(PageBreak())

    story.append(Paragraph("5. Key Code Implementation Details", h1_style))
    
    story.append(Paragraph("Course Interface Definition (src/app/models/course.model.ts)", h2_style))
    model_code = ("export interface Course {<br/>"
                  "  id: number;<br/>"
                  "  title: string;<br/>"
                  "  code: string;<br/>"
                  "  instructor: string;<br/>"
                  "  credits: number;<br/>"
                  "  department: string;<br/>"
                  "  enrolled: boolean;<br/>"
                  "  description: string;<br/>"
                  "}")
    story.append(Paragraph(model_code, code_style))
    
    story.append(Paragraph("Course Card Component Logic (src/app/components/course-card/course-card.ts)", h2_style))
    cc_ts_code = ("import { Component, Input, Output, EventEmitter, OnInit, OnChanges, OnDestroy, SimpleChanges } from '@angular/core';<br/>"
                  "import { Course } from '../../models/course.model';<br/><br/>"
                  "@Component({<br/>"
                  "  selector: 'app-course-card',<br/>"
                  "  imports: [],<br/>"
                  "  templateUrl: './course-card.html',<br/>"
                  "  styleUrl: './course-card.css'<br/>"
                  "})<br/>"
                  "export class CourseCardComponent implements OnInit, OnChanges, OnDestroy {<br/>"
                  "  @Input() course!: Course;<br/>"
                  "  @Input() searchQuery: string = '';<br/>"
                  "  @Output() enrollmentToggled = new EventEmitter&lt;number&gt;();<br/>"
                  "  @Output() creditsChanged = new EventEmitter&lt;{ id: number; credits: number }&gt;();<br/><br/>"
                  "  ngOnInit(): void {<br/>"
                  "    console.log('CourseCardComponent Init:', this.course?.code);<br/>"
                  "  }<br/>"
                  "  ngOnChanges(changes: SimpleChanges): void {<br/>"
                  "    console.log('CourseCardComponent Changes:', this.course?.code, Object.keys(changes));<br/>"
                  "  }<br/>"
                  "  ngOnDestroy(): void {<br/>"
                  "    console.log('CourseCardComponent Destroy:', this.course?.code);<br/>"
                  "  }<br/>"
                  "  toggleEnrollment(): void {<br/>"
                  "    this.enrollmentToggled.emit(this.course.id);<br/>"
                  "  }<br/>"
                  "  increaseCredits(): void {<br/>"
                  "    this.creditsChanged.emit({ id: this.course.id, credits: this.course.credits + 1 });<br/>"
                  "  }<br/>"
                  "  decreaseCredits(): void {<br/>"
                  "    if (this.course.credits &gt; 1) {<br/>"
                  "      this.creditsChanged.emit({ id: this.course.id, credits: this.course.credits - 1 });<br/>"
                  "    }<br/>"
                  "  }<br/>"
                  "}")
    story.append(Paragraph(cc_ts_code, code_style))
    story.append(PageBreak())

    story.append(Paragraph("Course Card Component Template (src/app/components/course-card/course-card.html)", h2_style))
    cc_html_code = ("&lt;div class=\"course-card\" [class.enrolled]=\"course.enrolled\"&gt;<br/>"
                    "  &lt;div class=\"card-glow\"&gt;&lt;/div&gt;<br/>"
                    "  &lt;div class=\"card-header\"&gt;<br/>"
                    "    &lt;span class=\"dept-badge\"&gt;{{ course.department }}&lt;/span&gt;<br/>"
                    "    &lt;span class=\"course-code\"&gt;{{ course.code }}&lt;/span&gt;<br/>"
                    "  &lt;/div&gt;<br/>"
                    "  &lt;h3 class=\"course-title\"&gt;{{ course.title }}&lt;/h3&gt;<br/>"
                    "  &lt;p class=\"course-desc\"&gt;{{ course.description }}&lt;/p&gt;<br/>"
                    "  &lt;div class=\"course-meta\"&gt;<br/>"
                    "    &lt;div class=\"meta-item\"&gt;<br/>"
                    "      &lt;span class=\"meta-label\"&gt;Instructor:&lt;/span&gt;<br/>"
                    "      &lt;span class=\"meta-val\"&gt;{{ course.instructor }}&lt;/span&gt;<br/>"
                    "    &lt;/div&gt;<br/>"
                    "    &lt;div class=\"meta-item\"&gt;<br/>"
                    "      &lt;span class=\"meta-label\"&gt;Credits:&lt;/span&gt;<br/>"
                    "      &lt;div class=\"credits-control\"&gt;<br/>"
                    "        &lt;button (click)=\"decreaseCredits()\" [disabled]=\"course.credits &lt;= 1\"&gt;-&lt;/button&gt;<br/>"
                    "        &lt;span class=\"credits-val\"&gt;{{ course.credits }}&lt;/span&gt;<br/>"
                    "        &lt;button (click)=\"increaseCredits()\"&gt;+&lt;/button&gt;<br/>"
                    "      &lt;/div&gt;<br/>"
                    "    &lt;/div&gt;<br/>"
                    "  &lt;/div&gt;<br/>"
                    "  &lt;button (click)=\"toggleEnrollment()\" [class.enrolled]=\"course.enrolled\" class=\"enroll-btn\"&gt;<br/>"
                    "    {{ course.enrolled ? 'Drop Course' : 'Enroll Now' }}<br/>"
                    "  &lt;/button&gt;<br/>"
                    "&lt;/div&gt;")
    story.append(Paragraph(cc_html_code, code_style))

    story.append(Paragraph("Course List Component Logic Snippet (src/app/pages/course-list/course-list.ts)", h2_style))
    cl_ts_code = ("export class CourseList implements OnInit {<br/>"
                  "  courses: Course[] = [];<br/>"
                  "  searchText: string = '';<br/>"
                  "  showEnrolledOnly: boolean = false;<br/><br/>"
                  "  get filteredCourses(): Course[] {<br/>"
                  "    return this.courses.filter(course =&gt; {<br/>"
                  "      const matchesSearch = !this.searchText || <br/>"
                  "        course.title.toLowerCase().includes(this.searchText.toLowerCase()) ||<br/>"
                  "        course.code.toLowerCase().includes(this.searchText.toLowerCase());<br/>"
                  "      const matchesEnrollment = !this.showEnrolledOnly || course.enrolled;<br/>"
                  "      return matchesSearch && matchesEnrollment;<br/>"
                  "    });<br/>"
                  "  }<br/>"
                  "  onEnrollmentToggled(id: number): void {<br/>"
                  "    const course = this.courses.find(c =&gt; c.id === id);<br/>"
                  "    if (course) course.enrolled = !course.enrolled;<br/>"
                  "  }<br/>"
                  "  onCreditsChanged(event: { id: number; credits: number }): void {<br/>"
                  "    const course = this.courses.find(c =&gt; c.id === event.id);<br/>"
                  "    if (course) course.credits = event.credits;<br/>"
                  "  }<br/>"
                  "  incrementAllCredits(): void {<br/>"
                  "    this.courses = this.courses.map(course =&gt; ({ ...course, credits: course.credits + 1 }));<br/>"
                  "  }<br/>"
                  "}")
    story.append(Paragraph(cl_ts_code, code_style))
    story.append(PageBreak())

    story.append(Paragraph("6. Captured Screenshots & Verification", h1_style))
    story.append(Paragraph("All application features were fully verified in the browser:", body_style))

    img_paths = [
        (r"C:\Users\User\.gemini\antigravity-ide\brain\f47eb5d2-607a-4d37-997a-9e6dfa234389\home_page_1784711221211.png", "Home Welcome Page Dashboard showing academic overview cards"),
        (r"C:\Users\User\.gemini\antigravity-ide\brain\f47eb5d2-607a-4d37-997a-9e6dfa234389\courses_initial_1784711238614.png", "Initial Course List displaying all available modules"),
        (r"C:\Users\User\.gemini\antigravity-ide\brain\f47eb5d2-607a-4d37-997a-9e6dfa234389\courses_searched_1784711261826.png", "Filtered course results using two-way bound search bar input ('Angular')"),
        (r"C:\Users\User\.gemini\antigravity-ide\brain\f47eb5d2-607a-4d37-997a-9e6dfa234389\courses_enrolled_credits_1784711303639.png", "State verification: Enrolled DBMS course, increased credit to 5, total credits updated to 11"),
        (r"C:\Users\User\.gemini\antigravity-ide\brain\f47eb5d2-607a-4d37-997a-9e6dfa234389\courses_filtered_enrolled_1784711337144.png", "Filtered courses list showing enrolled modules only (Advanced Web, DBMS, Cloud Architecture)"),
        (r"C:\Users\User\.gemini\antigravity-ide\brain\f47eb5d2-607a-4d37-997a-9e6dfa234389\courses_bulk_credits_1784711366058.png", "Parent-Child reactive update: Triggered 'Bulk Credit Add' button to add +1 credit to all cards"),
        (r"C:\Users\User\.gemini\antigravity-ide\brain\f47eb5d2-607a-4d37-997a-9e6dfa234389\profile_modified_1784711410558.png", "Student Profile split layout with real-time model updates and custom rocket avatar selected")
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
            story.append(Paragraph(f"<b>[Screenshot Placeholder]:</b> {caption} (File not found)", body_style))

    story.append(PageBreak())

    story.append(Paragraph("7. Output & Event Binding Explanations", h1_style))
    out_text = ("• <b>Property Binding:</b> Used to dynamically disable the credits decrement button when credits equal 1, "
                "and toggle the '.enrolled' css class on course cards dynamically based on the state variable.<br/>"
                "• <b>Event Binding:</b> Used for mouse click callbacks on credit modify buttons and enrollment state changes. "
                "Also used for selector changes in avatar options.<br/>"
                "• <b>Two-way Binding:</b> Used in both the search bar (filter state) and the student profile form, "
                "allowing changes in form fields to mirror immediately in the left preview card via template interpolation.<br/>"
                "• <b>Parent-Child Communication:</b> Parent binds course lists to the child card via <code>[course]</code> input parameter. "
                "The child notifies the parent of changes via <code>(enrollmentToggled)</code> and <code>(creditsChanged)</code> outputs, "
                "triggering data updates that bubble up to recalculate total selected credits and active counts instantly.<br/>"
                "• <b>Lifecycle Hooks:</b> <code>ngOnInit</code> prepares mock courses on page load. <code>ngOnChanges</code> detects input updates "
                "like credit changes from the parent. <code>ngOnDestroy</code> tracks when course cards are unmounted (e.g. during enrollment filters).")
    story.append(Paragraph(out_text, body_style))
    story.append(Spacer(1, 10))

    story.append(Paragraph("8. Learning Outcomes & Conclusion", h1_style))
    learnings = [
        "Implemented standard and standalone Angular bindings: Property, Event, Interpolation, and Two-way data binding.",
        "Created reusable child components (CourseCardComponent) communicating cleanly with parent components.",
        "Demonstrated the application and execution sequence of ngOnInit, ngOnChanges, and ngOnDestroy hooks.",
        "Configured Vitest unit test suites to successfully assert correct component instantiation under route scopes.",
        "Maintained codebase standard without adding comments, preserving clean code structure."
    ]
    for l in learnings:
        story.append(Paragraph(f"✓ {l}", body_style))
    story.append(Spacer(1, 10))

    story.append(Paragraph("9. Conclusion", h1_style))
    concl_text = ("Hands-On 2 successfully delivers a dynamic, interactive, and completely functional "
                  "Student Course Portal interface. By utilizing structural standalone components and parent-child "
                  "bindings, the application structure adheres to the latest modern Angular recommendations while "
                  "enabling rich responsive interactions.")
    story.append(Paragraph(concl_text, body_style))

    doc.build(story)
    print("PDF Report compiled successfully at:", pdf_filename)

if __name__ == '__main__':
    build_pdf()
