package com.Carteira.Acao.CONTROLLER;

import com.Carteira.Acao.DTO.Devolucao.ErroDTO;
import com.Carteira.Acao.SERVICES.ApiAcaoExternaService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/external/API")
public class ApiAcaoExterna {

    @Autowired
    private ApiAcaoExternaService apiAcaoExternaService;

    @GetMapping("/nomes")
    public ResponseEntity<Object> pegarNomeDasAcoes(){

        try {
            return ResponseEntity.status(HttpStatus.OK).body(apiAcaoExternaService.pegarNomeDasAcoes());
        } catch (RuntimeException e) {
            ErroDTO erroDTO = new ErroDTO(e.getMessage());
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(erroDTO);
        }
    }

    @GetMapping("/{acao}")
    public ResponseEntity<Object> pegarInfoAcao(@PathVariable String acao) {

        try {

            return ResponseEntity.status(HttpStatus.OK).body(apiAcaoExternaService.pegarInfoDaAcao(acao));

        } catch (RuntimeException e) {
            ErroDTO erroDTO = new ErroDTO(e.getMessage());
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(erroDTO);
        }
    }
}
