package com.Carteira.Acao.ENTITY;

import jakarta.persistence.*;
import lombok.*;

import java.io.Serial;
import java.io.Serializable;

@Entity
@ToString
@AllArgsConstructor
@NoArgsConstructor
public class Acoes implements Serializable {

    @Serial
    private static final long serialVersionUID = 2L;

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long idAcao;
    private String codigo;
    private String Nome;
    private Double Valor;
    private Long quantidade;

    @ManyToOne
    @JoinColumn(name = "Login_idLogin", nullable = false)
    private Login login;

    public Long getIdAcao() {
        return idAcao;
    }

    public void setIdAcao(Long idAcao) {
        this.idAcao = idAcao;
    }

    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public String getNome() {
        return Nome;
    }

    public void setNome(String nome) {
        Nome = nome;
    }

    public Double getValor() {
        return Valor;
    }

    public void setValor(Double valor) {
        Valor = valor;
    }

    public Long getQuantidade() {
        return quantidade;
    }

    public void setQuantidade(Long quantidade) {
        this.quantidade = quantidade;
    }

    public Login getLogin() {
        return login;
    }

    public void setLogin(Login login) {
        this.login = login;
    }
}
