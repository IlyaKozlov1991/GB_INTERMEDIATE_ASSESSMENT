package Exercise002;

import java.awt.*;
// import java.awt.event.*;

// import javax.management.ValueExp;
import javax.swing.*;
import java.util.ArrayList;
// import java.io.IOException;


public class App extends JFrame {
    
    private JPanel panel1 = new JPanel();
    private JPanel panel2 = new JPanel();
    private JPanel panel3 = new JPanel();
    private JPanel panel4 = new JPanel();
    private JPanel panel5 = new JPanel();
    private JPanel panel6 = new JPanel();
    private JPanel panel7 = new JPanel();
    private JButton button1 = new JButton("Help");
    private JButton button2 = new JButton("PLAY");
    private JButton button3 = new JButton("Add new toys");
    private JButton button4 = new JButton("Edit toys");
    private JButton button5 = new JButton("Present a toy");
    private JLabel label1 = new JLabel("LIST OF TOYS:");
    private JLabel label2 = new JLabel("New name/");
    private JLabel label3 = new JLabel("New quantity/");
    private JLabel label4 = new JLabel("New chance/");
    private JLabel label5 = new JLabel("ID#");
    private JLabel label6 = new JLabel("Set new chance/");
    private JLabel label7 = new JLabel("Add quantity/");
    private JLabel label8 = new JLabel("------------------- WAITING LIST -------------------");
    private JLabel label9 = new JLabel("------------------- EDITING -------------------");
    private TextArea show1 = new TextArea();
    private TextArea show2 = new TextArea();
    private JTextField input1 = new JTextField();
    private JTextField input2 = new JTextField();
    private JTextField input3 = new JTextField();
    private JTextField input4 = new JTextField();
    private JTextField input5 = new JTextField();
    private JTextField input6 = new JTextField();
    private Checkbox checkbox1 = new Checkbox();
    private Checkbox checkbox2 = new Checkbox();
    

    public App(ArrayList<Toy> toys) {
        super("Hello, " + System.getProperty("user.name") + "!");
        this.setBounds(600, 100, 800, 550);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        String showText1 = "";
        if (toys.size() == 0) {
            String msg = "Toys set is empty!\nAdd new toys to the set before any play.";
            JOptionPane.showMessageDialog(null, msg, "WARNING", JOptionPane.PLAIN_MESSAGE);
        }
        for (int i = 0; i < toys.size(); i++) {
            showText1 += toys.get(i).myPrint() + System.lineSeparator();
        }

        ArrayList<String> waitingList = new ArrayList<>();
        
        Container container = this.getContentPane();
        container.setLayout(new BoxLayout(container, BoxLayout.PAGE_AXIS));
        
        
        /*
         * OPTION code (i) for buttons:
         * 1 - Help
         * 2 - Play a draw
         * 3 - Add new toys to draw set
         * 4 - Edit chance or quantity of toys from draw set
         * 5 - Give a toy from Waiting list to winner
         */
        button1.addActionListener(new ButtonEvent(toys, waitingList, 1, null, null, null, null, null, null, null));
        button2.addActionListener(new ButtonEvent(toys, waitingList, 2, show1, show2, null, null, null, null, null));
        button2.setPreferredSize(new Dimension(200, 100));
        button3.addActionListener(new ButtonEvent(toys, waitingList, 3, show1, null, input1, input2, input3, null, null));
        button3.setPreferredSize(new Dimension(130, 30));
        button4.addActionListener(new ButtonEvent(toys, waitingList, 4, show1, null, input4, input5, input6, checkbox1, checkbox2));
        button4.setPreferredSize(new Dimension(130, 30));
        button5.addActionListener(new ButtonEvent(toys, waitingList, 5, null, show2, null, null, null, null, null));
        button5.setPreferredSize(new Dimension(200, 100));
        
        show1.setText(showText1);
        show1.setPreferredSize(new Dimension(300, 100));
        show2.setPreferredSize(new Dimension(300, 100));

        input1.setPreferredSize(new Dimension(130, 30));
        input2.setPreferredSize(new Dimension(50, 30));
        input3.setPreferredSize(new Dimension(50, 30));
        input4.setPreferredSize(new Dimension(50, 30));
        input5.setPreferredSize(new Dimension(50, 30));
        input6.setPreferredSize(new Dimension(50, 30));

        /*
         * Rendering of the App screen for MacOS and WinOS
         */
        if (System.getProperty("os.name").contains("Mac")) {
            panel1.add(Box.createRigidArea(new Dimension(24, 40)));
            panel1.add(button1);
            panel1.add(Box.createRigidArea(new Dimension(340, 0)));
            panel1.add(Box.createRigidArea(new Dimension(190, 0)));
            panel1.add(label1);
            panel1.add(Box.createRigidArea(new Dimension(24, 15)));

            panel2.add(Box.createRigidArea(new Dimension(24, 0)));
            panel2.add(button2);
            panel2.add(Box.createRigidArea(new Dimension(200, 0)));
            panel2.add(show1);
            panel2.add(Box.createRigidArea(new Dimension(24, 0)));

            panel3.add(label9);
            
            panel4.add(Box.createRigidArea(new Dimension(24, 15)));
            panel4.add(button3);
            panel4.add(Box.createRigidArea(new Dimension(20, 15)));
            panel4.add(label2);
            panel4.add(Box.createGlue());
            panel4.add(input1);
            panel4.add(Box.createRigidArea(new Dimension(20, 15)));
            panel4.add(label3);
            panel4.add(Box.createGlue());
            panel4.add(input2);
            panel4.add(Box.createRigidArea(new Dimension(20, 15)));
            panel4.add(label4);
            panel4.add(Box.createGlue());
            panel4.add(input3);
            panel4.add(Box.createRigidArea(new Dimension(24, 15)));

            panel5.add(Box.createRigidArea(new Dimension(24, 15)));
            panel5.add(button4);
            panel5.add(Box.createRigidArea(new Dimension(35, 15)));
            panel5.add(label5);
            panel5.add(Box.createGlue());
            panel5.add(input4);
            panel5.add(Box.createRigidArea(new Dimension(30, 15)));
            panel5.add(checkbox1);
            panel5.add(Box.createGlue());
            panel5.add(label6);
            panel5.add(Box.createGlue());
            panel5.add(input5);
            panel5.add(Box.createRigidArea(new Dimension(30, 15)));
            panel5.add(checkbox2);
            panel5.add(Box.createGlue());
            panel5.add(label7);
            panel5.add(Box.createGlue());
            panel5.add(input6);
            panel5.add(Box.createRigidArea(new Dimension(24, 15)));

            panel6.add(label8);

            panel7.add(Box.createRigidArea(new Dimension(0, 15)));
            panel7.add(button5);
            panel7.add(Box.createRigidArea(new Dimension(200, 0)));
            panel7.add(show2);
            panel7.add(Box.createRigidArea(new Dimension(0, 50)));
        }
        else if (System.getProperty("os.name").contains("Win")) {
            panel1.add(Box.createRigidArea(new Dimension(24, 40)));
            panel1.add(button1);
            panel1.add(Box.createRigidArea(new Dimension(350, 0)));
            panel1.add(Box.createRigidArea(new Dimension(200, 0)));
            panel1.add(label1);
            panel1.add(Box.createRigidArea(new Dimension(24, 15)));

            panel2.add(Box.createRigidArea(new Dimension(24, 0)));
            panel2.add(button2);
            panel2.add(Box.createRigidArea(new Dimension(200, 0)));
            panel2.add(show1);
            panel2.add(Box.createRigidArea(new Dimension(24, 0)));

            panel3.add(label9);
            
            panel4.add(Box.createRigidArea(new Dimension(24, 15)));
            panel4.add(button3);
            panel4.add(Box.createRigidArea(new Dimension(40, 15)));
            panel4.add(label2);
            panel4.add(Box.createGlue());
            panel4.add(input1);
            panel4.add(Box.createRigidArea(new Dimension(20, 15)));
            panel4.add(label3);
            panel4.add(Box.createGlue());
            panel4.add(input2);
            panel4.add(Box.createRigidArea(new Dimension(20, 15)));
            panel4.add(label4);
            panel4.add(Box.createGlue());
            panel4.add(input3);
            panel4.add(Box.createRigidArea(new Dimension(24, 15)));

            panel5.add(Box.createRigidArea(new Dimension(24, 15)));
            panel5.add(button4);
            panel5.add(Box.createRigidArea(new Dimension(70, 15)));
            panel5.add(label5);
            panel5.add(Box.createGlue());
            panel5.add(input4);
            panel5.add(Box.createRigidArea(new Dimension(30, 15)));
            panel5.add(checkbox1);
            panel5.add(Box.createGlue());
            panel5.add(label6);
            panel5.add(Box.createGlue());
            panel5.add(input5);
            panel5.add(Box.createRigidArea(new Dimension(30, 15)));
            panel5.add(checkbox2);
            panel5.add(Box.createGlue());
            panel5.add(label7);
            panel5.add(Box.createGlue());
            panel5.add(input6);
            panel5.add(Box.createRigidArea(new Dimension(24, 15)));

            panel6.add(label8);

            panel7.add(Box.createRigidArea(new Dimension(0, 15)));
            panel7.add(button5);
            panel7.add(Box.createRigidArea(new Dimension(200, 0)));
            panel7.add(show2);
            panel7.add(Box.createRigidArea(new Dimension(0, 50)));
        }

        container.add(panel1);
        container.add(panel2);
        container.add(panel3);
        container.add(panel4);
        container.add(panel5);
        container.add(panel6);
        container.add(panel7);

    }
}
