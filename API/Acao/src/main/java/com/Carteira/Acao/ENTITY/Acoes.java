package com.Carteira.Acao.ENTITY;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.io.Serial;
import java.io.Serializable;

@Entity
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class Acoes implements Serializable {

    @Serial
    private static final long serialVersionUID = 2L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long idAcao;
    private String codigo;
    private String Nome;
    private Double Valor;
    private Long quantidade;

    @ManyToOne
    @JoinColumn(name = "Login_idLogin", nullable = false)
    private Login login;
}
