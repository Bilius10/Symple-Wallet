package com.Carteira.Acao.DTO;

import jakarta.validation.constraints.NotBlank;

public record LoginDTO(@NotBlank String cpf,
                       @NotBlank String senha) {
}
