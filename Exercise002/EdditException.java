package Exercise002;

import java.awt.Checkbox;
import java.beans.ExceptionListener;

public class EdditException extends Exception {
    
    public EdditException(Checkbox checkbox1, Checkbox checkbox2) {
        if (checkbox1.getState() == false && checkbox2.getState() == false) {
            System.out.println("outEX");
        }
    }
}
