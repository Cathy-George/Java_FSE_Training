import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'creditLabel',
  standalone: true
})
export class CreditLabelPipe implements PipeTransform {
  transform(value: number): string {
    if (value === 3) {
      return `${value} Credits (Core/General)`;
    } else if (value === 4) {
      return `${value} Credits (Advanced Seminar)`;
    } else {
      return `${value} Credits (Elective/Short)`;
    }
  }
}
