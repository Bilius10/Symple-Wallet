package com.Carteira.Acao.DTO.Recebimento;

import jakarta.validation.constraints.NotBlank;

public record LoginDTO(@NotBlank String cpf,
                       @NotBlank String senha) {
}
