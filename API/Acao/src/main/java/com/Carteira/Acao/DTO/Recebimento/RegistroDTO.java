package com.Carteira.Acao.DTO.Recebimento;

import jakarta.validation.constraints.NotBlank;

public record RegistroDTO(@NotBlank String login,
                          @NotBlank String senha,
                          @NotBlank String cpf) {
}
