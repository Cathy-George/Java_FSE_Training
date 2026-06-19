import org.junit.Test;

import static org.junit.Assert.*;

public class AssertionsTest {

    @Test
    public void testAssertions() {

        // Assert equals
        assertEquals(5, 2 + 3);
        System.out.println("assertEquals passed!");

        // Assert true
        if (assertTrue(5 > 3)){
            System.out.println("assertTrue passed!");
        }
        else{
            System.out.println("assertTrue False");
        }

        // Assert false
        assertFalse(5 < 3);

        // Assert null
        assertNull(null);

        // Assert not null
        assertNotNull(new Object());
    }
}