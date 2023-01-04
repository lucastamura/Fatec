package PROVA_JAVA.repositorio;
import PROVA_JAVA.domain.*;

public class Calculadora implements viagem{
    private double valor;

    public double getValor() {
        return valor;
    }


    public void setValor(double valor) {
        this.valor = valor;
    }

    @Override
    public void informacoes(String partida, String chegada, double Distancia) {
        setValor(Distancia *2.5);
        System.out.println("O trajeto " + partida + " a " + chegada + " será no valor de R$" + getValor()); 
    }


}