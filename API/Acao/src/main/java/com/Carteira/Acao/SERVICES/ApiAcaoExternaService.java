package com.Carteira.Acao.SERVICES;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClientException;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.util.UriComponentsBuilder;

@Service
public class ApiAcaoExternaService {


    private final RestTemplate restTemplate;

    @Autowired
    public ApiAcaoExternaService(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    public String pegarNomeDasAcoes() {

        try {
            String url = "https://brapi.dev/api/available";
            return restTemplate.getForObject(url, String.class);
        } catch (RestClientException e) {
            throw new RuntimeException(e);
        }
    }

    public String pegarInfoDaAcao(String acao){

        try {
            String url = "https://brapi.dev/api/quote/"+acao+"?token=jhFurx6qDTaR892psxCNdT";

            return restTemplate.getForObject(url, String.class);
        }catch (RestClientException e){
            throw new RuntimeException(e);
        }
    }

    public String pegarInfoDaAcao30dias(String acao){

        try {

            String url = UriComponentsBuilder.fromHttpUrl( "https://brapi.dev/api/quote/"+acao+"?token=jhFurx6qDTaR892psxCNdT")
                    .queryParam("range", "1mo")
                    .queryParam("interval", "1d")
                    .toUriString();

            return restTemplate.getForObject(url, String.class);
        }catch (RestClientException e){
            throw new RuntimeException(e);
        }
    }
}
