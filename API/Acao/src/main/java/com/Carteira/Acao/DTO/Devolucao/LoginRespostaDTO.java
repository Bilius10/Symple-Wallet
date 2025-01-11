package com.Carteira.Acao.DTO.Devolucao;

import jakarta.validation.constraints.NotBlank;

public record LoginRespostaDTO(@NotBlank String token,
                               @NotBlank Long idLogin,
                               @NotBlank String login,
                               @NotBlank String cpf) {
}
