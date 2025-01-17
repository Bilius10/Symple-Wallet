package com.Carteira.Acao.Utils;

import com.Carteira.Acao.CONTROLLER.ApiAcaoExterna;
import com.Carteira.Acao.DTO.MelhorPiorAcao;
import com.Carteira.Acao.ENTITY.Acoes;
import com.Carteira.Acao.SERVICES.ApiAcaoExternaService;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.util.List;

@Service
public class Utilidades {

    @Autowired
    private ApiAcaoExternaService apiAcaoExternaService;

    public MelhorPiorAcao MelhorePiorAcao(List<Acoes> acoes) throws JsonProcessingException {

        ObjectMapper objectMapper = new ObjectMapper();
        String melhor = "";
        String pior = "";
        BigDecimal ultimaDiferenca = BigDecimal.ZERO;

        for (int i = 0; i <= acoes.size() - 1; i++) {

            String infoAcao30 = String.valueOf(apiAcaoExternaService.pegarInfoDaAcao30dias(acoes.get(i).getCodigo()));
            JsonNode json = objectMapper.readTree(infoAcao30);
            JsonNode results = json.get("results");
            JsonNode historicalData = results.get(0).get("historicalDataPrice");
            JsonNode ultimoDia = historicalData.get(historicalData.size() - 1);

            BigDecimal fechamentoUltimoDia = BigDecimal.valueOf(ultimoDia.get("close").asDouble());

            JsonNode primeiroDia = historicalData.get(0);
            BigDecimal fechamentoPrimeirodiaDia = BigDecimal.valueOf(primeiroDia.get("close").asDouble());

            BigDecimal diferenca = fechamentoUltimoDia.subtract(fechamentoPrimeirodiaDia);

            if(i == 0 || diferenca.compareTo(ultimaDiferenca) > 0 ){
                melhor = acoes.get(i).getCodigo();
                ultimaDiferenca = diferenca;
            }

            if(i == 0 || diferenca.compareTo(ultimaDiferenca) < 0 ){
                pior = acoes.get(i).getCodigo();
                ultimaDiferenca = diferenca;
            }

        }
        MelhorPiorAcao melhorPiorAcao = new MelhorPiorAcao(melhor, pior);
        return melhorPiorAcao;
    }
}
