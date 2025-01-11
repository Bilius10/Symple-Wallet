package com.Carteira.Acao.DTO.Recebimento;

import jakarta.validation.constraints.Negative;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;

public record AcaoDTO(@NotBlank String codigo,
                      @NotBlank String Nome,
                      @NotNull @Negative Double Valor,
                      @NotNull @Negative Integer quantidade,
                      @NotNull Long idUsuario) {
}
