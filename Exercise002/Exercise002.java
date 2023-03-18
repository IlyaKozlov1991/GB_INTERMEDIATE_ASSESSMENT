package Exercise002;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;


class Main {
    public static void main(String[] args) throws IOException {

        String name = "";
        Integer id = 0;
        Integer quantity = 0;
        Integer chance = 0;
        ArrayList innerList = new ArrayList<>();
        ArrayList<ArrayList<ArrayList<ArrayList>>> finalList = new ArrayList<>();
        ArrayList<Toy> toys = new ArrayList<>();

        /*
         * Open storage with draw set
         */
        File newFile = new File("Exercise002/toysList.txt");
        Scanner newScanner = new Scanner(newFile);
        while (newScanner.hasNextLine()) {
            String a = newScanner.nextLine();
            String[] alist = a.split(">");
            for (int i = 0; i < alist.length; i++) {
                String[] alist2 = alist[i].split("&");
                // String[] innerList2 = alist2;
                for (int j = 0; j < alist2.length; j++) {
                    innerList.add(alist2[j]);
                }
            }   
        }
        newScanner.close();
        /*
         * Converting recieved data to ArrayList<Toy> to work with it
         */
        int size = innerList.size();
        for (int i = 0; i < innerList.size(); i++) {
        }
        for (int k = 0; k < size / 4; k++) {
            for (int i = 0; i < 1; i++) {
                ArrayList cutList = new ArrayList<>();
                for (int j = 0; j < 4; j++) {
                    cutList.add(innerList.get(0));
                    innerList.remove(0);
                }
                finalList.add(cutList);
            }
        }

        /*
         * Adding new toys of class 'Toys' based on received data
         */
        int index = 0;
        for (int j = 1; j < finalList.size() + 1; j++) {
            for (int i = 0; i < 1; i++) {
                name = String.valueOf(finalList.get(i + index).get(0));
                String tempID = String.valueOf(finalList.get(i + index).get(1));
                id = Integer.parseInt(tempID);
                String tempQNT = String.valueOf(finalList.get(i + index).get(2));
                quantity = Integer.parseInt(tempQNT);
                String tempCHN = String.valueOf(finalList.get(i + index).get(3));
                chance = Integer.parseInt(tempCHN);
                Toy tempToy = new Toy(id, name, quantity, chance);
                toys.add(tempToy);
                index +=1;
            }
        }

        App myApp = new App(toys);
        myApp.setVisible(true);
    }
}
