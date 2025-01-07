package com.Carteira.Acao.DTO;

import jakarta.validation.constraints.NotBlank;

public record RegistroDTO(@NotBlank String Login,
                          @NotBlank String senha,
                          @NotBlank String cpf) {
}
