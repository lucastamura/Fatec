package PROVA_JAVA.domain;

public abstract class Pessoa { //CLASSE ABSTRATA
    private String nome; //EMCAPSULAMENTO
    private String dataDeNascimento; //EMCAPSULAMENTO
    private String documento; //EMCAPSULAMENTO


    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getDataDeNascimento() {
        return dataDeNascimento;
    }
    public void setDataDeNascimento(String dataDeNascimento) {
        this.dataDeNascimento = dataDeNascimento;
    }
    public String getDocumento() {
        return documento;
    }
    public void setDocumento(String documento) {
        this.documento = documento;
    }

    
}
