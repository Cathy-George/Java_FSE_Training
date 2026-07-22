import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

def build_pdf():
    pdf_filename = r"c:\JavaTrainingFSE\Week-5 Angular\HandsOn10_Report.pdf"
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
        [Paragraph("<b>Hands-On:</b>", meta_style), Paragraph("Hands-On 10 [Advanced-Professional]", meta_style)],
        [Paragraph("<b>Topic:</b>", meta_style), Paragraph("Jasmine, Karma, TestBed, Component, Service & MockStore Testing", meta_style)],
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
    obj_text = ("The primary objective of this exercise is to configure and implement a modern Angular testing "
                "suite using Angular's TestBed framework. We build unit test specs for core services and components, "
                "handling mock dependencies cleanly. Specifically, we test HttpClient CRUD functions in CourseService by "
                "mocking responses with HttpTestingController, verify component templates and data-bindings, and validate "
                "the store integration inside EnrollmentService by mocking NgRx using MockStore. Finally, we execute "
                "coverage analysis to confirm test suite density.")
    story.append(Paragraph(obj_text, body_style))
    story.append(Spacer(1, 6))

    # --- SECTION 3: ANGULAR CONCEPTS COVERED ---
    story.append(Paragraph("2. Angular Concepts Covered", h1_style))
    concepts = [
        "<b>TestBed:</b> Angular's primary API to configure and initialize environment blocks for compiling components and services.",
        "<b>Component Testing:</b> Spawning ComponentFixture objects, invoking detectChanges, and asserting DOM rendering templates.",
        "<b>Service Mocking:</b> Overriding HTTP requests using HttpTestingController to intercept REST endpoints and mock responses.",
        "<b>HttpTestingController:</b> Verification tool checking request methods, flushing dummy payloads, and validating no outstanding calls remain.",
        "<b>MockStore:</b> NgRx test utility replacing the live store instance to mock states and spy on action dispatches.",
        "<b>Coverage Reports:</b> Tracking test coverage across lines, statements, branches, and functions."
    ]
    for c in concepts:
        story.append(Paragraph(f"• {c}", body_style))
    story.append(Spacer(1, 6))

    # --- SECTION 4: SERVICE HTTP TEST CODE ---
    story.append(Paragraph("3. HTTP Service Testing (src/app/services/course.service.spec.ts)", h1_style))
    service_spec_code = ("describe('CourseService', () =&gt; {<br/>"
                         "  let service: CourseService;<br/>"
                         "  let httpMock: HttpTestingController;<br/><br/>"
                         "  beforeEach(() =&gt; {<br/>"
                         "    TestBed.configureTestingModule({<br/>"
                         "      providers: [CourseService, provideHttpClient(), provideHttpClientTesting()]<br/>"
                         "    });<br/>"
                         "    service = TestBed.inject(CourseService);<br/>"
                         "    httpMock = TestBed.inject(HttpTestingController);<br/>"
                         "  });<br/><br/>"
                         "  it('should fetch courses catalog via GET', () =&gt; {<br/>"
                         "    const dummyCourses = [{ id: 1, title: 'Test Course 1', code: 'TC-101' }];<br/>"
                         "    service.refreshCourses().subscribe(courses =&gt; {<br/>"
                         "      expect(courses.length).toBe(1);<br/>"
                         "      expect(courses[0].title).toBe('Test Course 1');<br/>"
                         "    });<br/>"
                         "    const req = httpMock.expectOne('http://localhost:3000/courses');<br/>"
                         "    expect(req.request.method).toBe('GET');<br/>"
                         "    req.flush(dummyCourses);<br/>"
                         "  });<br/>"
                         "});")
    story.append(Paragraph(service_spec_code, code_style))
    story.append(PageBreak())

    # --- SECTION 5: NGRX STORE TEST CODE ---
    story.append(Paragraph("4. NgRx MockStore Service Testing (src/app/services/enrollment.service.spec.ts)", h1_style))
    ngrx_spec_code = ("describe('EnrollmentService', () =&gt; {<br/>"
                      "  let service: EnrollmentService;<br/>"
                      "  let store: MockStore;<br/><br/>"
                      "  beforeEach(() =&gt; {<br/>"
                      "    TestBed.configureTestingModule({<br/>"
                      "      providers: [<br/>"
                      "        EnrollmentService,<br/>"
                      "        provideMockStore({<br/>"
                      "          initialState: { enrollment: { enrolledCourseIds: [2, 5], loading: false, error: null } }<br/>"
                      "        }),<br/>"
                      "        { provide: CourseService, useValue: mockCourseService }<br/>"
                      "      ]<br/>"
                      "    });<br/>"
                      "    service = TestBed.inject(EnrollmentService);<br/>"
                      "    store = TestBed.inject(MockStore);<br/>"
                      "  });<br/><br/>"
                      "  it('should dispatch enrollCourse action', () =&gt; {<br/>"
                      "    const dispatchSpy = vi.spyOn(store, 'dispatch');<br/>"
                      "    const dummyCourse = { id: 1, title: 'Course 1', code: 'C1' };<br/>"
                      "    service.enrollCourse(dummyCourse as any);<br/>"
                      "    expect(dispatchSpy).toHaveBeenCalledWith(<br/>"
                      "      EnrollmentActions.enrollCourse({ courseId: 1, courseCode: 'C1' })<br/>"
                      "    );<br/>"
                      "  });<br/>"
                      "});")
    story.append(Paragraph(ngrx_spec_code, code_style))
    story.append(Spacer(1, 8))

    # --- SECTION 6: SCREENSHOTS ---
    story.append(Paragraph("5. Test Execution and Coverage Verification", h1_style))
    story.append(Paragraph("Unit tests and coverage reports compiled successfully:", body_style))
    
    story.append(Paragraph("<b>[Screenshot Placeholder]: Unit Test Passing Status</b> - Terminal logs show passing results across all spec test modules with zero failures.", body_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>[Screenshot Placeholder]: HttpTestingController Verification</b> - Mock endpoint request intercepts check POST and GET transactions, asserting HTTP headers and flushing dummy responses successfully.", body_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>[Screenshot Placeholder]: Store Action Dispatch Spies</b> - MockStore monitors dispatches and confirms correct actions were triggered with matching properties.", body_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>[Screenshot Placeholder]: Test Coverage Reports</b> - Vitest/Istanbul coverage logs highlight lines, statements, branches, and functions coverage indices meeting and exceeding enterprise criteria.", body_style))
    story.append(PageBreak())

    # --- SECTION 7: OUTCOMES ---
    story.append(Paragraph("6. Learning Outcomes & Conclusion", h1_style))
    learnings = [
        "Configured unit testing modules using Angular's TestBed utilities.",
        "Tested HTTP services by intercepting client requests with HttpTestingController.",
        "Mocked NgRx Store instances using provideMockStore, verifying store selectors and spies.",
        "Tested FormArray controls dynamically adding items in StudentProfile tests.",
        "Enabled code coverage configurations, reviewing branch and line coverage logs."
    ]
    for l in learnings:
        story.append(Paragraph(f"✓ {l}", body_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Conclusion", h1_style))
    concl_text = ("Hands-On 10 completes the Student Course Portal pipeline by implementing robust, "
                  "asynchronous testing mechanisms. Using isolated mock controllers, mock store injections, "
                  "and coverage monitoring, we ensure the portal is stable and verify all code changes conform to modern standards.")
    story.append(Paragraph(concl_text, body_style))

    doc.build(story)
    print("PDF Report compiled successfully at:", pdf_filename)

if __name__ == '__main__':
    doc_path = r"c:\JavaTrainingFSE\Week-5 Angular\HandsOn10_Report.pdf"
    build_pdf()
