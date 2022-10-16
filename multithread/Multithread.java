class MultiThreadingDemo extends Thread{
	public void run(){
		try{
			//displaying the thread that is running
			System.out.println("Thread "+Thread.currentThread().getId()+" is running");
		}
		catch(Exception e){
			//throwing an exception
			System.out.println("Exception is caught");
		}
	}
}
public class Multithread{
	public static void main(String[] args) {
		int n = 8;
		for(int i=0;i<n;i++){
			MultiThreadingDemo m = new MultiThreadingDemo();
			m.start();
		}
	}
}