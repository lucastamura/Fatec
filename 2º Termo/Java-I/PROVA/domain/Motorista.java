package PROVA_JAVA.domain;

public class Motorista extends Pessoa {//HERANÇA
    private int chn;
    private String placa;
    private String carro;

    public int getChn() {
        return chn;
    }
    public void setChn(int chn) {
        this.chn = chn;
    }
    public String getPlaca() {
        return placa;
    }
    public void setPlaca(String placa) {
        this.placa = placa;
    }
    public String getCarro() {
        return carro;
    }
    public void setCarro(String carro) {
        this.carro = carro;
    }
}
