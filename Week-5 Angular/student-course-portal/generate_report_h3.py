import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

def build_pdf():
    pdf_filename = r"c:\JavaTrainingFSE\Week-5 Angular\HandsOn3_Report.pdf"
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
        [Paragraph("<b>Hands-On:</b>", meta_style), Paragraph("Hands-On 3 [Intermediate-Advanced]", meta_style)],
        [Paragraph("<b>Topic:</b>", meta_style), Paragraph("Directives & Pipes (HighlightDirective, CreditLabelPipe)", meta_style)],
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
    obj_text = ("The primary objective of this exercise is to implement and configure Angular "
                "directives and pipes to improve templates functionality, performance, and formatting. "
                "Specifically, we implement classic structural directives (*ngIf, *ngFor, and *ngSwitch), "
                "render performance tracking using trackBy, dynamically modify visual styles using ngClass and ngStyle, "
                "build a custom hover HighlightDirective, and write a custom CreditLabelPipe to format course credits.")
    story.append(Paragraph(obj_text, body_style))
    story.append(Spacer(1, 10))

    story.append(Paragraph("2. Angular Concepts Covered", h1_style))
    concepts = [
        "<b>*ngIf Directive:</b> Conditionally mounts or destroys templates based on logical expressions (e.g. results empty state).",
        "<b>*ngFor Directive with trackBy:</b> Iterates arrays to render lists efficiently, identifying items by unique IDs to avoid total DOM redraws.",
        "<b>*ngSwitch Directive (*ngSwitchCase, *ngSwitchDefault):</b> Evaluates conditional states to render specific elements matching distinct department categories.",
        "<b>ngClass & ngStyle Directives:</b> Integrates dynamic, multi-state visual stylings based on component variables.",
        "<b>Custom Attribute Directive:</b> Restructures HostListener events (mouseenter/mouseleave) to change background and borders of elements dynamically.",
        "<b>Custom Pipe:</b> Implements Custom transforms to translate raw model counts (e.g. 4 credits) into contextual descriptive labels."
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
                   "└── src/<br/>"
                   "    └── app/<br/>"
                   "        ├── directives/<br/>"
                   "        │   └── highlight.directive.ts (Custom Attribute Directive)<br/>"
                   "        ├── pipes/<br/>"
                   "        │   └── credit-label.pipe.ts (Custom Pipe Transform)<br/>"
                   "        ├── components/<br/>"
                   "        │   └── course-card/ (Directives and custom elements application)<br/>"
                   "        └── pages/<br/>"
                   "            ├── course-list/ (Parent structural loop application)<br/>"
                   "            └── student-profile/ (Custom avatars loop implementation)")
    story.append(Paragraph(folder_text, code_style))
    story.append(Spacer(1, 10))
    story.append(PageBreak())

    story.append(Paragraph("5. Key Code Implementation Details", h1_style))
    
    story.append(Paragraph("Custom Highlight Directive (src/app/directives/highlight.directive.ts)", h2_style))
    dir_code = ("import { Directive, ElementRef, HostListener, Input, Renderer2 } from '@angular/core';<br/><br/>"
                "@Directive({<br/>"
                "  selector: '[appHighlight]',<br/>"
                "  standalone: true<br/>"
                "})<br/>"
                "export class HighlightDirective {<br/>"
                "  @Input('appHighlight') highlightColor: string = '';<br/><br/>"
                "  constructor(private el: ElementRef, private renderer: Renderer2) {}<br/><br/>"
                "  @HostListener('mouseenter') onMouseEnter(): void {<br/>"
                "    const color = this.highlightColor || 'rgba(99, 102, 241, 0.08)';<br/>"
                "    this.renderer.setStyle(this.el.nativeElement, 'background-color', color);<br/>"
                "    this.renderer.setStyle(this.el.nativeElement, 'border-color', 'var(--color-primary)');<br/>"
                "    this.renderer.setStyle(this.el.nativeElement, 'box-shadow', 'var(--shadow-lg), var(--shadow-glow)');<br/>"
                "  }<br/><br/>"
                "  @HostListener('mouseleave') onMouseLeave(): void {<br/>"
                "    this.renderer.removeStyle(this.el.nativeElement, 'background-color');<br/>"
                "    this.renderer.removeStyle(this.el.nativeElement, 'border-color');<br/>"
                "    this.renderer.removeStyle(this.el.nativeElement, 'box-shadow');<br/>"
                "  }<br/>"
                "}")
    story.append(Paragraph(dir_code, code_style))
    
    story.append(Paragraph("Custom Credit Label Pipe (src/app/pipes/credit-label.pipe.ts)", h2_style))
    pipe_code = ("import { Pipe, PipeTransform } from '@angular/core';<br/><br/>"
                 "@Pipe({<br/>"
                 "  name: 'creditLabel',<br/>"
                 "  standalone: true<br/>"
                 "})<br/>"
                 "export class CreditLabelPipe implements PipeTransform {<br/>"
                 "  transform(value: number): string {<br/>"
                 "    if (value === 3) {<br/>"
                 "      return `${value} Credits (Core/General)`;<br/>"
                 "    } else if (value === 4) {<br/>"
                 "      return `${value} Credits (Advanced Seminar)`;<br/>"
                 "    } else {<br/>"
                 "      return `${value} Credits (Elective/Short)`;<br/>"
                 "    }<br/>"
                 "  }<br/>"
                 "}")
    story.append(Paragraph(pipe_code, code_style))
    story.append(PageBreak())

    story.append(Paragraph("Course Card Template with Directives (src/app/components/course-card/course-card.html)", h2_style))
    cc_html_code = ("&lt;div class=\"course-card\" [appHighlight]=\"'rgba(99, 102, 241, 0.08)'\" <br/>"
                    "     [ngClass]=\"{'enrolled': course.enrolled, 'not-enrolled': !course.enrolled}\"<br/>"
                    "     [ngStyle]=\"{'box-shadow': course.enrolled ? '0 0 15px rgba(16, 185, 129, 0.15)' : 'none'}\"&gt;<br/>"
                    "  &lt;div class=\"card-glow\"&gt;&lt;/div&gt;<br/>"
                    "  &lt;div class=\"card-header\"&gt;<br/>"
                    "    &lt;div class=\"dept-info\"&gt;<br/>"
                    "      &lt;span [ngSwitch]=\"course.department\" class=\"dept-icon\"&gt;<br/>"
                    "        &lt;span *ngSwitchCase=\"'Computer Science'\"&gt;💻&lt;/span&gt;<br/>"
                    "        &lt;span *ngSwitchCase=\"'Information Technology'\"&gt;☁️&lt;/span&gt;<br/>"
                    "        &lt;span *ngSwitchCase=\"'Design'\"&gt;🎨&lt;/span&gt;<br/>"
                    "        &lt;span *ngSwitchDefault&gt;📚&lt;/span&gt;<br/>"
                    "      &lt;/span&gt;<br/>"
                    "      &lt;span class=\"dept-badge\"&gt;{{ course.department }}&lt;/span&gt;<br/>"
                    "    &lt;/div&gt;<br/>"
                    "    &lt;span class=\"course-code\"&gt;{{ course.code }}&lt;/span&gt;<br/>"
                    "  &lt;/div&gt;<br/>"
                    "  &lt;h3 class=\"course-title\"&gt;{{ course.title }}&lt;/h3&gt;<br/>"
                    "  &lt;p class=\"course-desc\"&gt;{{ course.description }}&lt;/p&gt;<br/>"
                    "  &lt;div class=\"course-meta\"&gt;<br/>"
                    "    &lt;div class=\"meta-item credit-row\"&gt;<br/>"
                    "      &lt;span class=\"meta-label\"&gt;Credits:&lt;/span&gt;<br/>"
                    "      &lt;div class=\"credits-control\"&gt;<br/>"
                    "        &lt;button (click)=\"decreaseCredits()\" [disabled]=\"course.credits &lt;= 1\"&gt;-&lt;/button&gt;<br/>"
                    "        &lt;span class=\"credits-val\"&gt;{{ course.credits | creditLabel }}&lt;/span&gt;<br/>"
                    "        &lt;button (click)=\"increaseCredits()\"&gt;+&lt;/button&gt;<br/>"
                    "      &lt;/div&gt;<br/>"
                    "    &lt;/div&gt;<br/>"
                    "  &lt;/div&gt;<br/>"
                    "&lt;/div&gt;")
    story.append(Paragraph(cc_html_code, code_style))

    story.append(Paragraph("Course List Template with Structural Directives (src/app/pages/course-list/course-list.html)", h2_style))
    cl_html_code = ("&lt;div class=\"page-wrapper fade-in\"&gt;<br/>"
                    "  &lt;div class=\"search-box\"&gt;<br/>"
                    "    &lt;input type=\"text\" [(ngModel)]=\"searchText\" class=\"search-input\" /&gt;<br/>"
                    "    &lt;button *ngIf=\"searchText\" (click)=\"searchText = ''\"&gt;×&lt;/button&gt;<br/>"
                    "  &lt;/div&gt;<br/><br/>"
                    "  &lt;div *ngIf=\"filteredCourses.length &gt; 0; else noResults\" class=\"courses-grid\"&gt;<br/>"
                    "    &lt;app-course-card <br/>"
                    "      *ngFor=\"let course of filteredCourses; trackBy: trackByCourseId\"<br/>"
                    "      [course]=\"course\" <br/>"
                    "      [searchQuery]=\"searchText\"<br/>"
                    "      (enrollmentToggled)=\"onEnrollmentToggled($event)\"<br/>"
                    "      (creditsChanged)=\"onCreditsChanged($event)\"&gt;<br/>"
                    "    &lt;/app-course-card&gt;<br/>"
                    "  &lt;/div&gt;<br/><br/>"
                    "  &lt;ng-template #noResults&gt;<br/>"
                    "    &lt;div class=\"placeholder-card no-results\"&gt;<br/>"
                    "      &lt;h2&gt;No courses found&lt;/h2&gt;<br/>"
                    "    &lt;/div&gt;<br/>"
                    "  &lt;/ng-template&gt;<br/>"
                    "&lt;/div&gt;")
    story.append(Paragraph(cl_html_code, code_style))
    story.append(PageBreak())

    story.append(Paragraph("6. Captured Screenshots & Verification", h1_style))
    story.append(Paragraph("All application features were fully verified in the browser:", body_style))

    img_paths = [
        (r"C:\Users\User\.gemini\antigravity-ide\brain\f47eb5d2-607a-4d37-997a-9e6dfa234389\courses_h3_initial_1784711824396.png", "Course Offerings list applying *ngFor, custom CreditLabelPipe labels, and *ngSwitch icon badges"),
        (r"C:\Users\User\.gemini\antigravity-ide\brain\f47eb5d2-607a-4d37-997a-9e6dfa234389\courses_h3_hover_1784711857581.png", "Custom HighlightDirective in action when mouse enters the course card element (purple bg highlight & border glow)"),
        (r"C:\Users\User\.gemini\antigravity-ide\brain\f47eb5d2-607a-4d37-997a-9e6dfa234389\courses_h3_searched_1784711899869.png", "Course List filtered by search key 'Database' with clear button visible via *ngIf"),
        (r"C:\Users\User\.gemini\antigravity-ide\brain\f47eb5d2-607a-4d37-997a-9e6dfa234389\profile_h3_modified_1784712010159.png", "Student Profile page displaying dynamic avatar emoji selections generated using *ngFor loop")
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

    story.append(Paragraph("7. Output & Behavioral Explanations", h1_style))
    out_text = ("• <b>Structural Directives:</b> Replaced modern controls flow with classic Angular structural directives. "
                "<code>*ngIf</code> handles displaying the clear search buttons and toggling grids vs empty placeholders. "
                "<code>*ngFor</code> loops through filtered courses in the catalog list and emojis in the profile editor.<br/>"
                "• <b>trackBy optimization:</b> <code>trackByCourseId</code> was implemented to ensure Angular selectively redraws modified cards "
                "rather than recreating the complete card set on every input trigger.<br/>"
                "• <b>*ngSwitch evaluation:</b> Implemented <code>[ngSwitch]</code> on the card's header, mapping department strings to emojis "
                "(e.g. CS maps to 💻, IT to ☁️, Design to 🎨) dynamically.<br/>"
                "• <b>Custom Highlight Directive:</b> Utilized HostListeners on <code>appHighlight</code> to respond to mouse pointer movements. "
                "It adjusts the element's style dynamically using Renderer2 to ensure direct DOM manipulations are clean.<br/>"
                "• <b>Custom CreditLabelPipe:</b> Created a pure pipe implementing <code>PipeTransform</code>. It transforms a number "
                "(e.g., 3, 4) into a detailed academic descriptor (e.g. '3 Credits (Core/General)' or '4 Credits (Advanced Seminar)') dynamically.")
    story.append(Paragraph(out_text, body_style))
    story.append(Spacer(1, 10))

    story.append(Paragraph("8. Learning Outcomes & Conclusion", h1_style))
    learnings = [
        "Understood classic structural directives (*ngIf, *ngFor, and *ngSwitch) alongside modern control flows.",
        "Created custom attribute directives responding to mouse pointer gestures using HostListeners and Renderer2.",
        "Built custom formatting pipes to translate model integers into semantic string descriptors.",
        "Implemented trackBy functions to optimize list redraw cycles and improve memory profiling.",
        "Asserted build checks and tests compilation, maintaining zero code comment styles."
    ]
    for l in learnings:
        story.append(Paragraph(f"✓ {l}", body_style))
    story.append(Spacer(1, 10))

    story.append(Paragraph("9. Conclusion", h1_style))
    concl_text = ("Hands-On 3 successfully implements custom pipes, directives, and loops in the Student Course "
                  "Portal. By replacing modern controls with structural directives and integrating trackBy, the portal "
                  "features robust modularity, performance optimizations, and sleek aesthetic styles.")
    story.append(Paragraph(concl_text, body_style))

    doc.build(story)
    print("PDF Report compiled successfully at:", pdf_filename)

if __name__ == '__main__':
    build_pdf()
