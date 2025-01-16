package com.Carteira.Acao.DTO;

import jakarta.validation.constraints.NotBlank;

public record MelhorPiorAcao(@NotBlank String melhorAcao,
                             @NotBlank String piorAcao) {
}
