
public class TesteOperadoresIncrementoDecremento1 {

	public static void main(String[] args) {
		
		int x = 5;
		System.out.println("x = "+ x);
		
		System.out.println("Pré-Fixado");
		System.out.println("++x = "+ ++x);
		System.out.println("x = "+ x); 
		System.out.println("--x = "+ --x);
		System.out.println("x = "+ x);
		
		System.out.println("Pós-Fixado");
		System.out.println("x++ = "+ x++);
		System.out.println("x = "+ x);
		System.out.println("x-- = "+ x--);
		System.out.println("x = "+ x);
		
	}

}
