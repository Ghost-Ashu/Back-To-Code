## GUI PROJECT

public import javax.swing.*;

public class gui {

    gui() {
        JFrame f = new JFrame("Table");

        String[][] data = {
                { "john", "10", "cse" },
                { "cena", "12", "it" }
        };
        String[] header = { "name", "id", "dept" };
        JTable t = new JTable(data, header);
        t.setBounds(30, 40, 200, 300);

        JScrollPane sp = new JScrollPane(t);
        f.add(sp);

        f.setSize(500, 200);

        f.setVisible(true);

    }

    public static void main(String[] args) {
        new gui();
    }

}

