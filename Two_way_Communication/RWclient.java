import java.net.*;
import java.io.*;

class RWclient {
    public static void main(String args[]) throws Exception {
        Socket s = new Socket("localhost", 7657);
        DataInputStream datain = new DataInputStream(s.getInputStream());
        DataOutputStream dataout = new DataOutputStream(s.getOutputStream());
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String message = "", reply = "";
        while (!message.equals("stop")) {
            message = br.readLine();
            dataout.writeUTF(message);
            dataout.flush();
            reply = datain.readUTF();
            System.out.println("Server says: " + reply);
        }

        dataout.close();
        s.close();
    }
}