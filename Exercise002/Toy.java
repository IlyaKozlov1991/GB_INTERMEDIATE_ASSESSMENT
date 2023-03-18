package Exercise002;

// import java.io.File;
// import java.io.FileReader;
// import java.io.FileWriter;
// import java.io.IOException;
// import java.util.ArrayList;

import javax.swing.JOptionPane;

public class Toy {
    private int id;
    private String name;
    private int quantity;
    private int chance;
    
    public  Toy(int ID, String NAME, int QUANTITY, int CHANCE) {
        this.id = ID;
        this.name = NAME;
        this.quantity = QUANTITY;
        this.chance = CHANCE;
    }

    // public Toy() {}

    public String toString(){
        String str = name  + "&" +  
        String.valueOf(id) +  "&" +
        String.valueOf(quantity) +  "&" +
        String.valueOf(chance);
        return str;
    }

    public String getName(){
        return name;
    }

    public Integer getChance() {
        return chance;
    }

    public Integer getQuantity() {
        return quantity;
    }

    public Integer getID() {
        return id;
    }

    public String myPrint() {
        String myPrint = name + ": ID-" + id + " quantity-" + quantity + " chance-" + chance;
        return myPrint;
    }

    public void removeToy() {
        if (quantity > 0) {
            this.quantity -= 1;
        }
        else {
            String msg = "There are no such toys anymore.";
            JOptionPane.showMessageDialog(null, msg, "WARNING", JOptionPane.PLAIN_MESSAGE); 
        }
    }

    public void editQuantity(int newQnt) {
        this.quantity += newQnt;
    }

    public void editChance(int newChnc) {
        this.chance = newChnc;
    }

}
