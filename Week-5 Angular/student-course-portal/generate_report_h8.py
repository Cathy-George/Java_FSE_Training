import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

def build_pdf():
    pdf_filename = r"c:\JavaTrainingFSE\Week-5 Angular\HandsOn8_Report.pdf"
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
        [Paragraph("<b>Hands-On:</b>", meta_style), Paragraph("Hands-On 8 [Advanced-Professional]", meta_style)],
        [Paragraph("<b>Topic:</b>", meta_style), Paragraph("HTTP Client, JSON Server CRUD, RxJS Operators & Interceptors", meta_style)],
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
    obj_text = ("The primary objective of this exercise is to integrate robust HTTP client-server communication using "
                "Angular's HttpClient. By launching a local JSON Server instance backend that stores course records in "
                "db.json, the application performs full CRUD database syncs dynamically. Additionally, we integrate "
                "advanced RxJS pipelined operators including map, tap, switchMap, retry, and catchError to manipulate data flows "
                "and recover from connection faults. Finally, we implement functional HttpInterceptors to manage application-wide "
                "loading indicator bars and global API error intercepting coupled with user notification toast popups.")
    story.append(Paragraph(obj_text, body_style))
    story.append(Spacer(1, 6))

    # --- SECTION 3: ANGULAR CONCEPTS COVERED ---
    story.append(Paragraph("2. Angular Concepts Covered", h1_style))
    concepts = [
        "<b>HttpClient:</b> Injectable Angular service enabling backend REST API operations over XMLHttpRequests.",
        "<b>JSON Server backend:</b> Mock database utility providing instant, local REST endpoints dynamically sync'd from db.json.",
        "<b>RxJS Operators:</b> Utilizing <code>map</code> to scrub string inputs, <code>tap</code> for side effect caching, <code>switchMap</code> to chain operations, <code>retry</code> for network fault resilience, and <code>catchError</code> for exception intercepts.",
        "<b>HttpInterceptorFn:</b> Modern functional interceptor configuration capturing outbound requests and inbound responses to inject global behavior.",
        "<b>Loading Spinner Service:</b> Tracking active HTTP request counts and overlaying full-page blur blocks when pending operations are running.",
        "<b>Global Error Handling:</b> Intercepting status code failures (404, 500, etc.) in a unified interceptor pipeline and surfacing detailed diagnostic alerts via toast banners."
    ]
    for c in concepts:
        story.append(Paragraph(f"• {c}", body_style))
    story.append(Spacer(1, 6))

    # --- SECTION 4: CODE IMPLEMENTATION ---
    story.append(Paragraph("3. Course Service API Operations (src/app/services/course.service.ts)", h1_style))
    service_code = ("// Fetch and Refresh courses list from JSON Server<br/>"
                    "refreshCourses(): Observable&lt;Course[]&gt; {<br/>"
                    "  return this.http.get&lt;Course[]&gt;(this.apiUrl).pipe(<br/>"
                    "    retry(2),<br/>"
                    "    map(courses =&gt; courses.map(c =&gt; ({ ...c, title: c.title.trim() }))),<br/>"
                    "    tap(courses =&gt; this.coursesSubject.next(courses)),<br/>"
                    "    catchError(this.handleError)<br/>"
                    "  );<br/>"
                    "}<br/><br/>"
                    "// Add new Course record to JSON Server<br/>"
                    "createCourse(course: Omit&lt;Course, 'id' | 'enrolled'&gt;): Observable&lt;Course[]&gt; {<br/>"
                    "  return this.http.post&lt;Course&gt;(this.apiUrl, { ...course, enrolled: false }).pipe(<br/>"
                    "    tap(created =&gt; console.log('Created course:', created.code)),<br/>"
                    "    switchMap(() =&gt; this.refreshCourses()),<br/>"
                    "    catchError(this.handleError)<br/>"
                    "  );<br/>"
                    "}")
    story.append(Paragraph(service_code, code_style))
    story.append(PageBreak())

    # --- SECTION 5: INTERCEPTORS ---
    story.append(Paragraph("4. Http Interceptors", h1_style))
    
    story.append(Paragraph("Functional Loading Interceptor (src/app/interceptors/loading.interceptor.ts)", h2_style))
    int_code1 = ("export const loadingInterceptor: HttpInterceptorFn = (req, next) =&gt; {<br/>"
                 "  const loadingService = inject(LoadingService);<br/>"
                 "  loadingService.show();<br/>"
                 "  return next(req).pipe(<br/>"
                 "    delay(1000), // artificial delay for visual demo<br/>"
                 "    finalize(() =&gt; loadingService.hide())<br/>"
                 "  );<br/>"
                 "};")
    story.append(Paragraph(int_code1, code_style))
    
    story.append(Paragraph("Functional Error Interceptor (src/app/interceptors/error.interceptor.ts)", h2_style))
    int_code2 = ("export const errorInterceptor: HttpInterceptorFn = (req, next) =&gt; {<br/>"
                 "  const notificationService = inject(NotificationService);<br/>"
                 "  return next(req).pipe(<br/>"
                 "    catchError((error: HttpErrorResponse) =&gt; {<br/>"
                 "      let errorMessage = 'An unknown error occurred!';<br/>"
                 "      if (error.error instanceof ErrorEvent) {<br/>"
                 "        errorMessage = `Client-side error: ${error.error.message}`;<br/>"
                 "      } else {<br/>"
                 "        errorMessage = `Server-side error (${error.status}): ${error.statusText || 'Unable to connect'}`;<br/>"
                 "      }<br/>"
                 "      notificationService.show(errorMessage, 'warning');<br/>"
                 "      return throwError(() =&gt; new Error(errorMessage));<br/>"
                 "    })<br/>"
                 "  );<br/>"
                 "};")
    story.append(Paragraph(int_code2, code_style))
    story.append(Spacer(1, 8))

    # --- SECTION 6: SCREENSHOTS ---
    story.append(Paragraph("5. Verification and Screen Outputs", h1_style))
    story.append(Paragraph("The HttpClient operations and Interceptor loading/error transitions were successfully verified:", body_style))
    
    story.append(Paragraph("<b>[Screenshot Placeholder]: Loading Spinner Overlay</b> - A visual translucent screen overlay with a spinning wheel and 'Loading Academic Data...' text halts interactions during active HTTP GET operations.", body_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>[Screenshot Placeholder]: Database Synchronized List</b> - Catalog loads from JSON Server REST API (port 3000) and displays course cards for computer science, IT, and design tracks.", body_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>[Screenshot Placeholder]: Add/Delete Course Operations</b> - Submitting the add course form performs a POST request to JSON Server. Clicking delete makes a DELETE call, followed by an automatic reactive list refetch.", body_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>[Screenshot Placeholder]: Error Toast Notification</b> - Shutting down the JSON server backend triggers the HTTP catchError pipeline, intercepting the failed connection and broadcasting an warning toast banner: 'Server-side error (0): Unable to connect to server'.", body_style))
    story.append(PageBreak())

    # --- SECTION 7: OUTCOMES ---
    story.append(Paragraph("6. Learning Outcomes & Conclusion", h1_style))
    learnings = [
        "Configured provideHttpClient with functional interceptors in a standalone boot configuration.",
        "Created an active-request loading counter service to block UI input during network roundtrips.",
        "Employed retry(2) and catchError to inject fault tolerance in API handlers.",
        "Integrated client CRUD methods mapping directly to REST paths on JSON Server.",
        "Decoupled notification broadcasts using a custom global Toast state emitter."
    ]
    for l in learnings:
        story.append(Paragraph(f"✓ {l}", body_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Conclusion", h1_style))
    concl_text = ("Hands-On 8 establishes robust asynchronous backend service communication for the Student Course Portal. "
                  "Using standard RxJS patterns, functional interceptors, and a local mock REST API server, data operations "
                  "now reflect database-persisted states while rendering loading animations and error messages.")
    story.append(Paragraph(concl_text, body_style))

    doc.build(story)
    print("PDF Report compiled successfully at:", pdf_filename)

if __name__ == '__main__':
    build_pdf()
