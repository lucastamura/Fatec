package PROVA_JAVA.domain;

public class Passageiro extends Pessoa { //HERANÇA//
    private int numeroDoCartao;

    public int getNumeroDoCartao() {
        return numeroDoCartao;
    }

    public void setNumeroDoCartao(int numeroDoCartao) {
        this.numeroDoCartao = numeroDoCartao;
    }
}
