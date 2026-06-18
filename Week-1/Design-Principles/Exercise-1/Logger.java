public class Logger {

    private static Logger instance = new Logger();

    private Logger() {
        System.out.println("Logger Created");
    }

    public static Logger getInstance() {
        return instance;
    }

    public void log(String msg) {
        System.out.println(msg);
    }
}