package com.Carteira.Acao.ENUM;

public enum NivelPermissao {


    ADMIN("admin"),
    NORMAL("normal");

    private String nivel;

    NivelPermissao(String nivel) {
        this.nivel = nivel;
    }

    public String getNivel() {
        return nivel;
    }
}
