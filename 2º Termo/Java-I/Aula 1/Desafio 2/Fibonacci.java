public class Fibonacci{
    public static void main(String[] args){

        int numero = 1;
        int anterior = 1;
        int resultado = 0;
               
        System.out.println(numero);
        System.out.println(anterior);
        
        for (int i = 3; i <= 30; i++){
            resultado = numero + anterior;
            System.out.println(resultado);
            anterior = numero;
            numero = resultado; 
        }
    }
}
