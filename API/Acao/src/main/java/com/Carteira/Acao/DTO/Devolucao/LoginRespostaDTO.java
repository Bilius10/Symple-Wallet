package com.Carteira.Acao.DTO.Devolucao;

import jakarta.validation.constraints.NotBlank;

public record LoginRespostaDTO(@NotBlank String token,
                               @NotBlank String login) {
}
