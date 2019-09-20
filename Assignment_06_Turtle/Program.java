import java.util.Scanner;

public class Program{

	public static void main(String[] args){

		int sides;
		int angle;
		int x;
		int y;

		Scanner in = new Scanner(System.in);	
		System.out.println("Enter a number of sides: ");
		sides=in.nextInt();
		angle=(((sides - 2) * 180) / sides);
		angle=(180-angle);
		Turtle bro;
		bro=new Turtle();
		turtleShape(sides,angle,bro);

	}
	public static void turtleShape(int x,int y,Turtle bro){
			if (x <= 0){
				return;
			} else {
				bro.forward(100);
				bro.left(y);
				turtleShape(x - 1,y,bro);		
		}
	}
}
