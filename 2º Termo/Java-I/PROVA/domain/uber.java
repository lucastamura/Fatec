package PROVA_JAVA.domain;
import PROVA_JAVA.repositorio.*;


public class uber{
public static void main(String[] args){

    
    Chamar c = new Chamar();
    Calculadora cl = new Calculadora();

    Motorista carlos = new Motorista();
        
    carlos.setNome("Carlos Andrade Silva");
    carlos.setDataDeNascimento("25/04/1978");
    carlos.setDocumento("521.521.465-14");
    carlos.setChn(254124582);
    carlos.setPlaca("EDA-5248");
    carlos.setCarro("Corola preto 2019");

    Passageiro ana = new Passageiro();

    ana.setNome("Ana Carla Silva Santos");
    ana.setDataDeNascimento("19/02/2001");
    ana.setDocumento("524.559.652-54");
    ana.setNumeroDoCartao(236581324);


    c.chamar(carlos, ana);
    cl.informacoes("Rua Leonor", "Avenida Brasil", 5.4);








    }
}
