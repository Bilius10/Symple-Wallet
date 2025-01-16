package com.Carteira.Acao.Utils;

import com.Carteira.Acao.CONTROLLER.ApiAcaoExterna;
import com.Carteira.Acao.DTO.MelhorPiorAcao;
import com.Carteira.Acao.ENTITY.Acoes;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.util.List;
import java.util.Map;

public class Utilidades {

    private ApiAcaoExterna apiAcaoExterna;

    //fazer
    public MelhorPiorAcao MelhorePiorAcao(List<Acoes> acoes) throws JsonProcessingException {

        ObjectMapper objectMapper = new ObjectMapper();
        String Melhor = "";
        String Pior = "";

        for (int i = 0; i <= acoes.size() ; i++) {
            String infoAcao30 = String.valueOf(apiAcaoExterna.pegarInfoAcao30dias(acoes.get(i).getCodigo()));
            var map = objectMapper.readValue(infoAcao30, Map.class);

        }

        return null;
    }
}
