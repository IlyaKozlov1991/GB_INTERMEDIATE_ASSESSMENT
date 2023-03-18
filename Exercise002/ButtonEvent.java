package Exercise002;

import java.awt.*;
import java.awt.event.*;

// import javax.management.ValueExp;
import javax.swing.*;
import java.util.ArrayList;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Date;
import java.util.Random;
// import java.util.Scanner;


public class ButtonEvent implements ActionListener {
    ArrayList<Toy> toys;
    ArrayList<String> waitingList;
    int option;
    TextArea show1;
    TextArea show2;
    JTextField input1;
    JTextField input2;
    JTextField input3;
    Checkbox checkbox1;
    Checkbox checkbox2;

    public ButtonEvent( ArrayList<Toy> DRAW_SET, 
                        ArrayList<String> WAITING_LIS,   
                        int OPTION, 
                        TextArea SHOW1, 
                        TextArea SHOW2, 
                        JTextField TEXT_FIELD_1, 
                        JTextField TEXT_FIELD_2, 
                        JTextField TEXT_FIELD_3, 
                        Checkbox CHECK_BOX_1, 
                        Checkbox CHECK_BOX_2) {
        this.toys = DRAW_SET;
        this.waitingList = WAITING_LIS;
        this.option = OPTION;
        this.show1 = SHOW1;
        this.show2 = SHOW2;
        this.input1 = TEXT_FIELD_1;
        this.input2 = TEXT_FIELD_2;
        this.input3 = TEXT_FIELD_3;
        this.checkbox1 = CHECK_BOX_1;
        this.checkbox2 = CHECK_BOX_2;
    }

    public void actionPerformed(ActionEvent e) {
        switch (option) {
            case 1:
                String msg =    "PLAY -> play a game\n" +
                                "Add new toys -> add new toys to toys set\n" +
                                "Edit toys -> change chance (weight) or quantity of toys from toys set\n" +
                                "Present a toy -> give a toy from waiting list to Winner\n";
                JOptionPane.showMessageDialog(null, msg, "Commands:", JOptionPane.PLAIN_MESSAGE);
                break;
            case 2:
                try {
                    Random newRandom = new Random();
                    int randomToy = newRandom.nextInt(toys.size());
                    int randomChance = newRandom.nextInt(100);
                    msg = toys.get(randomToy).getName();
                    if (randomChance <= toys.get(randomToy).getChance() || toys.get(randomToy).getQuantity() > 0) {
                        toys.get(randomToy).removeToy();
                        File newWriteFile1 = new File("Exercise002/toysList.txt");
                        FileWriter newWriter1 = new FileWriter(newWriteFile1, false);
                        if (newWriteFile1.createNewFile()) {

                        }
                        else {
                            for (int i = 0; i < toys.size(); i++) {
                                newWriter1.write(toys.get(i).toString()+ ">");
                            }
                        }
                        waitingList.add(toys.get(randomToy).getName());
                        newWriter1.close();
                        String refreshShow1 = "";
                        String refreshShow2 = "";
                        for (int i = 0; i < toys.size(); i++) {
                            refreshShow1 += toys.get(i).myPrint() + "\n";
                        }
                        for (int i = 0; i < waitingList.size(); i++) {
                            refreshShow2 += waitingList.get(i) + "\n";
                        }
                        show1.setText(refreshShow1);
                        show2.setText(refreshShow2);
                        msg = "Toy '" + toys.get(randomToy).getName() + "' has been raffled!";
                        JOptionPane.showMessageDialog(null, msg, ":=)", JOptionPane.PLAIN_MESSAGE);
                    }
                    else {
                        msg = "Fail! Try next time!";
                        JOptionPane.showMessageDialog(null, msg, ":=(", JOptionPane.PLAIN_MESSAGE);
                    }
                }
            catch (Exception exp) {
                exp.fillInStackTrace();
                msg = "Toys set is empty!";
                JOptionPane.showMessageDialog(null, msg, ":=(", JOptionPane.PLAIN_MESSAGE);
            }
                break;
            case 3:
                try {
                    String newName = input1.getText();
                    int newID = toys.size() + 1;
                    int newQuantity = Integer.parseInt(input2.getText());
                    int newChance = Integer.parseInt(input3.getText());
                    Toy newToy = new Toy(newID, newName, newQuantity, newChance);
                    toys.add(newToy);
                    File newFile = new File("Exercise002/toysList.txt");
                        FileWriter newWriter = new FileWriter(newFile, false);
                        if (newFile.createNewFile()) {

                        }
                        else {
                            for (int i = 0; i < toys.size(); i++) {
                                newWriter.write(toys.get(i).toString()+ ">");
                            }
                        }
                    newWriter.close();
                    String refreshShow = "";
                    for (int i = 0; i < toys.size(); i++) {
                        refreshShow += toys.get(i).myPrint() + "\n";
                    }
                    show1.setText(refreshShow);
                    msg = "Toy '" + newToy.getName() + "' has been added to toys set!";
                    JOptionPane.showMessageDialog(null, msg, "Toy Add", JOptionPane.PLAIN_MESSAGE);
                }
                catch (IOException exp) {
                    msg = "Failed to add new toy to the set!";
                    JOptionPane.showMessageDialog(null, msg, "WARNING", JOptionPane.PLAIN_MESSAGE);
                }
                catch (NumberFormatException exp) {
                    msg = "Incorrect (or empty) value!\nTray again.";
                    JOptionPane.showMessageDialog(null, msg, "WARNING", JOptionPane.PLAIN_MESSAGE);
                }
                break;
            case 4:
                try {
                    Integer editID = Integer.parseInt(input1.getText());
                    if (checkbox1.getState() == true) {
                        Integer editChnc = Integer.parseInt(input2.getText());
                        toys.get(editID - 1).editChance(editChnc);
                        File newFile = new File("Exercise002/toysList.txt");
                        FileWriter newWriter = new FileWriter(newFile, false);
                        if (newFile.createNewFile()) {

                        }
                        else {
                            for (int i = 0; i < toys.size(); i++) {
                                newWriter.write(toys.get(i).toString()+ ">");
                            }
                        }
                        newWriter.close();
                        String refreshShow = "";
                        for (int i = 0; i < toys.size(); i++) {
                        refreshShow += toys.get(i).myPrint() + "\n";
                    }
                    show1.setText(refreshShow);
                        msg = "New Chance has been set for toy ID #" + 
                                editID + " <" + toys.get(editID - 1).getName() + ">.";
                        JOptionPane.showMessageDialog(null, msg, "Editor", JOptionPane.PLAIN_MESSAGE);

                    }
                    if (checkbox2.getState() == true) {
                        Integer editQnt = Integer.parseInt(input3.getText());
                        toys.get(editID - 1).editQuantity(editQnt);
                        File newFile = new File("Exercise002/toysList.txt");
                        FileWriter newWriter = new FileWriter(newFile, false);
                        if (newFile.createNewFile()) {

                        }
                        else {
                            for (int i = 0; i < toys.size(); i++) {
                                newWriter.write(toys.get(i).toString()+ ">");
                            }
                        }
                        newWriter.close();
                        String refreshShow = "";
                        for (int i = 0; i < toys.size(); i++) {
                        refreshShow += toys.get(i).myPrint() + "\n";
                    }
                    show1.setText(refreshShow);
                        msg = "New quantity has been added for toy ID #" + 
                                editID + " <" + toys.get(editID - 1).getName() + ">.";
                        JOptionPane.showMessageDialog(null, msg, "Editing", JOptionPane.PLAIN_MESSAGE);
                    }
                }
                catch (IOException exp1) {
                    msg = "Failed to add eddited toy to the set!\nTry again.";
                    JOptionPane.showMessageDialog(null, msg, "WARNING!", JOptionPane.PLAIN_MESSAGE);
                }
                catch (NumberFormatException exp2) {
                    msg = "Incorrect value!\nCheck wich option is chosen and enter new value";
                    JOptionPane.showMessageDialog(null, msg, "WARNING", JOptionPane.PLAIN_MESSAGE);
                }
                catch (IndexOutOfBoundsException exp3) {
                    msg = "ID not found.";
                    JOptionPane.showMessageDialog(null, msg, "WARNING", JOptionPane.PLAIN_MESSAGE);
                }
                break;
            case 5:
                try {
                    Date dateNow = new Date();
                    String register = "";
                    register += dateNow.toString() + " | " + waitingList.get(0) + System.lineSeparator();
                    waitingList.remove(0);
                    String refreshShow = "";
                    for (int i = 0; i < waitingList.size(); i++) {
                        refreshShow += waitingList.get(i) + System.lineSeparator();
                    }
                    show2.setText(refreshShow);
                    File newFile = new File("Exercise002/giftsRegister.txt");
                    FileWriter newWriter = new FileWriter(newFile, true);
                        if (newFile.createNewFile()) {
                            newWriter.write(register);
                        }
                        else {
                            newWriter.write(register);
                            }
                        newWriter.close();
                }
                catch (Exception exp) {
                    exp.fillInStackTrace();
                }
                break;
        }
    }
}
