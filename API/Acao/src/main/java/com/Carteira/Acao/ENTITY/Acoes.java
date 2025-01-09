package com.Carteira.Acao.ENTITY;

import jakarta.persistence.*;
import lombok.*;

import java.io.Serial;
import java.io.Serializable;

@Entity
@Getter
@Setter
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
}
