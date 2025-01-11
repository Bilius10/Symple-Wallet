package com.Carteira.Acao.SERVICES;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClientException;
import org.springframework.web.client.RestTemplate;

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
}
