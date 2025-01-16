package com.Carteira.Acao.DTO.Devolucao;

import com.Carteira.Acao.ENTITY.Acoes;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;

import java.util.List;

public record InfoAcaoDTO(@NotNull Double somaValor,
                          @NotBlank List<Acoes> InfoAcoes,
                          @NotNull Long somaQuantidade,
                          @NotNull String melhorAcao,
                          @NotNull String piorAcao) {
}
