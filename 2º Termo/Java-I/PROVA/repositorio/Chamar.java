package PROVA_JAVA.repositorio;
import PROVA_JAVA.domain.*;

public class Chamar {
    public void chamar(Motorista m, Passageiro p){
        System.out.println("O motorista " +m.getNome()+ " irá transportar o passageiro "+ p.getNome()); //POLIMORFISMO
    }
}
