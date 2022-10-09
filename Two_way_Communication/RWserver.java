import java.net.*;
import java.io.*;

class RWserver {
    public static void main(String args[]) throws Exception {
        ServerSocket ss = new ServerSocket(7657);
        Socket s = ss.accept();
        DataInputStream datain = new DataInputStream(s.getInputStream());
        DataOutputStream dataout = new DataOutputStream(s.getOutputStream());
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String message = "", reply = "";
        while (!message.equals("stop")) {
            message = datain.readUTF();
            System.out.println("client says: " + message);
            reply = br.readLine();
            dataout.writeUTF(reply);
            dataout.flush();
        }
        datain.close();
        s.close();
        ss.close();
    }
}