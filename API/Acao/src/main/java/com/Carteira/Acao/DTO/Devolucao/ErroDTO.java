package com.Carteira.Acao.DTO.Devolucao;

import jakarta.validation.constraints.NotBlank;

public record ErroDTO(@NotBlank String Mensagem) {
}
