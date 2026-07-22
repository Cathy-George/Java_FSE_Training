import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

def build_pdf():
    pdf_filename = r"c:\JavaTrainingFSE\Week-5 Angular\HandsOn9_Report.pdf"
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
        [Paragraph("<b>Hands-On:</b>", meta_style), Paragraph("Hands-On 9 [Advanced-Professional]", meta_style)],
        [Paragraph("<b>Topic:</b>", meta_style), Paragraph("NgRx Store, Reducers, Effects, Selectors, Actions & DevTools", meta_style)],
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
    obj_text = ("The primary objective of this exercise is to implement reactive state management inside the "
                "Student Course Portal using the NgRx framework. By establishing a dedicated 'Enrollment Store', "
                "we abstract enrollment tracking away from ad-hoc component variables. We introduce structured Actions "
                "representing state events, pure Reducer functions to handle state modifications synchronously, asynchronous "
                "Effects to integrate server catalog patches, and memoized Selectors to retrieve optimized state slices. "
                "Lastly, we register Redux DevTools for real-time history debugging.")
    story.append(Paragraph(obj_text, body_style))
    story.append(Spacer(1, 6))

    # --- SECTION 3: ANGULAR CONCEPTS COVERED ---
    story.append(Paragraph("2. Angular Concepts Covered", h1_style))
    concepts = [
        "<b>NgRx Store:</b> Redux-inspired global state container providing single-source-of-truth reactivity.",
        "<b>Actions (createAction):</b> Strongly typed payloads representing unique events that trigger state updates.",
        "<b>Reducers (createReducer):</b> Pure functions taking current state and actions, and returning new immutable state.",
        "<b>Effects (createEffect):</b> Side-effect handlers mapping actions to HTTP network payloads and dispatching result states.",
        "<b>Selectors (createSelector):</b> High-performance memoized queries yielding specific state properties.",
        "<b>DevTools (provideStoreDevtools):</b> Integrating Redux DevTools Extension to inspect state transitions and trigger time-travel logs."
    ]
    for c in concepts:
        story.append(Paragraph(f"• {c}", body_style))
    story.append(Spacer(1, 6))

    # --- SECTION 4: ACTIONS AND REDUCERS ---
    story.append(Paragraph("3. NgRx Store Configuration & State Definition", h1_style))
    
    story.append(Paragraph("Enrollment Actions (src/app/store/enrollment/enrollment.actions.ts)", h2_style))
    actions_code = ("export const loadEnrollments = createAction('[Enrollment] Load Enrollments');<br/>"
                    "export const loadEnrollmentsSuccess = createAction(<br/>"
                    "  '[Enrollment] Load Enrollments Success', props&lt;{ enrolledIds: number[] }&gt;()<br/>"
                    ");<br/>"
                    "export const enrollCourse = createAction(<br/>"
                    "  '[Enrollment] Enroll Course', props&lt;{ courseId: number; courseCode: string }&gt;()<br/>"
                    ");<br/>"
                    "export const enrollCourseSuccess = createAction(<br/>"
                    "  '[Enrollment] Enroll Course Success', props&lt;{ courseId: number; courseCode: string }&gt;()<br/>"
                    ");")
    story.append(Paragraph(actions_code, code_style))
    
    story.append(Paragraph("Enrollment Reducer (src/app/store/enrollment/enrollment.reducer.ts)", h2_style))
    reducer_code = ("export const enrollmentReducer = createReducer(<br/>"
                    "  initialState,<br/>"
                    "  on(EnrollmentActions.loadEnrollmentsSuccess, (state, { enrolledIds }) =&gt; ({<br/>"
                    "    ...state, enrolledCourseIds: enrolledIds, loading: false<br/>"
                    "  })),<br/>"
                    "  on(EnrollmentActions.enrollCourseSuccess, (state, { courseId }) =&gt; ({<br/>"
                    "    ...state,<br/>"
                    "    enrolledCourseIds: state.enrolledCourseIds.includes(courseId)<br/>"
                    "      ? state.enrolledCourseIds : [...state.enrolledCourseIds, courseId],<br/>"
                    "    loading: false<br/>"
                    "  }))<br/>"
                    ");")
    story.append(Paragraph(reducer_code, code_style))
    story.append(PageBreak())

    # --- SECTION 5: EFFECTS AND SELECTORS ---
    story.append(Paragraph("4. NgRx Effects & Service Binding", h1_style))
    
    story.append(Paragraph("Asynchronous Side-Effects (src/app/store/enrollment/enrollment.effects.ts)", h2_style))
    effects_code = ("enrollCourse$ = createEffect(() =&gt;<br/>"
                    "  this.actions$.pipe(<br/>"
                    "    ofType(EnrollmentActions.enrollCourse),<br/>"
                    "    switchMap(action =&gt;<br/>"
                    "      this.courseService.updateCourseEnrollment(action.courseId, true).pipe(<br/>"
                    "        map(() =&gt; EnrollmentActions.enrollCourseSuccess({<br/>"
                    "          courseId: action.courseId, courseCode: action.courseCode<br/>"
                    "        })),<br/>"
                    "        catchError(error =&gt; of(EnrollmentActions.enrollCourseFailure({ error: error.message })))<br/>"
                    "      )<br/>"
                    "    )<br/>"
                    "  )<br/>"
                    ");")
    story.append(Paragraph(effects_code, code_style))
    
    story.append(Paragraph("Refactored Enrollment Service (src/app/services/enrollment.service.ts)", h2_style))
    service_code = ("export class EnrollmentService {<br/>"
                    "  private store = inject(Store);<br/>"
                    "  private courseService = inject(CourseService);<br/><br/>"
                    "  getEnrolledCourseIds(): Observable&lt;Set&lt;number&gt;&gt; {<br/>"
                    "    return this.store.select(selectEnrolledCourseIds).pipe(<br/>"
                    "      map(ids =&gt; new Set(ids))<br/>"
                    "    );<br/>"
                    "  }<br/><br/>"
                    "  enrollCourse(course: Course): void {<br/>"
                    "    this.store.dispatch(EnrollmentActions.enrollCourse({<br/>"
                    "      courseId: course.id, courseCode: course.code<br/>"
                    "    }));<br/>"
                    "  }<br/>"
                    "}")
    story.append(Paragraph(service_code, code_style))
    story.append(Spacer(1, 8))

    # --- SECTION 6: SCREENSHOTS ---
    story.append(Paragraph("5. Verification and Store Debugging", h1_style))
    story.append(Paragraph("The enrollment store operations and state travels were successfully verified:", body_style))
    
    story.append(Paragraph("<b>[Screenshot Placeholder]: NgRx Initial State Load</b> - Redux DevTools displays [Enrollment] Load Enrollments action followed by [Enrollment] Load Enrollments Success, initializing active course enrollment lists.", body_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>[Screenshot Placeholder]: Enroll Action Dispatch</b> - Clicking 'Enroll' on a course card triggers the [Enrollment] Enroll Course action, displaying action properties and updating state asynchronously.", body_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>[Screenshot Placeholder]: State Diff Inspection</b> - Developer tools panel highlights the state array changes (e.g. adding ID 1 to enrolledCourseIds) in a highlighted green difference tree.", body_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>[Screenshot Placeholder]: Redux Time Travel Playback</b> - Running the devtools timeline slider dynamically rewinds enrollment states, recalculating credits count reactive labels instantly.", body_style))
    story.append(PageBreak())

    # --- SECTION 7: OUTCOMES ---
    story.append(Paragraph("6. Learning Outcomes & Conclusion", h1_style))
    learnings = [
        "Constructed structured action schemas for modular, scaleable states.",
        "Implemented immutable array expansions and filter operations inside pure Reducers.",
        "Created side-effect handlers to capture network requests asynchronously.",
        "Used memoized selectors to map course items and compute aggregated credit values.",
        "Integrated Redux DevTools providers to enable visual history tracking."
    ]
    for l in learnings:
        story.append(Paragraph(f"✓ {l}", body_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Conclusion", h1_style))
    concl_text = ("Hands-On 9 successfully migrates dynamic enrollment tracking in the Student Course Portal to an "
                  "enterprise-grade NgRx store. The implementation fulfills standard declarative architecture guidelines, "
                  "providing centralized state control and visual time-travel logging.")
    story.append(Paragraph(concl_text, body_style))

    doc.build(story)
    print("PDF Report compiled successfully at:", pdf_filename)

if __name__ == '__main__':
    build_pdf()
