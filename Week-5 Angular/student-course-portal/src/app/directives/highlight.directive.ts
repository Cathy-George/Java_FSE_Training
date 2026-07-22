import { Directive, ElementRef, HostListener, Input, Renderer2 } from '@angular/core';

@Directive({
  selector: '[appHighlight]',
  standalone: true
})
export class HighlightDirective {
  @Input('appHighlight') highlightColor: string = '';

  constructor(private el: ElementRef, private renderer: Renderer2) {}

  @HostListener('mouseenter') onMouseEnter(): void {
    const color = this.highlightColor || 'rgba(99, 102, 241, 0.08)';
    this.renderer.setStyle(this.el.nativeElement, 'background-color', color);
    this.renderer.setStyle(this.el.nativeElement, 'border-color', 'var(--color-primary)');
    this.renderer.setStyle(this.el.nativeElement, 'box-shadow', 'var(--shadow-lg), var(--shadow-glow)');
  }

  @HostListener('mouseleave') onMouseLeave(): void {
    this.renderer.removeStyle(this.el.nativeElement, 'background-color');
    this.renderer.removeStyle(this.el.nativeElement, 'border-color');
    this.renderer.removeStyle(this.el.nativeElement, 'box-shadow');
  }
}
