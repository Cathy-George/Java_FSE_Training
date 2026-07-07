package Excercise2;
public class FinancialForecast {

    // Recursive method
    public static double futureValue(double principal, double growthRate, int years) {

        // Base case
        if (years == 0) {
            return principal;
        }

        // Recursive case
        return futureValue(principal, growthRate, years - 1) * (1 + growthRate);
    }

    public static void main(String[] args) {

        double principal = 10000;
        double growthRate = 0.08; // 8%
        int years = 5;

        double result = futureValue(principal, growthRate, years);

        System.out.printf("Future Value after %d years = %.2f", years, result);
    }
}