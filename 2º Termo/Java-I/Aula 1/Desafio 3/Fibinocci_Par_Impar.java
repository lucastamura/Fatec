public class Fibonacci{
    public static void main(String[] args){
        int numero = 1;
        int anterior = 1;
        int resultado = 0;
        
        System.out.println("Resultado "+ numero +" impar");
        System.out.println("Resultado "+ anterior +" impar");

        for (int i = 3; i <= 30; i++){
            resultado = numero + anterior;
            if (resultado % 2 != 0){
                System.out.println("Resultado "+ resultado +" impar");
            }
            else{
                System.out.println("Resultado "+ resultado +" par"); 
            }
            anterior = numero;
            numero = resultado;
        }
    }
}
