package com.Carteira.Acao.DTO.Recebimento;


import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;

public record AcaoDTO(@NotBlank String codigo,
                      @NotBlank String Nome,
                      @NotNull Double Valor,
                      @NotNull Long quantidade,
                      @NotNull Long idUsuario) {
}
