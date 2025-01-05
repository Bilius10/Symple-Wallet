package com.Carteira.Acao.CONTROLLER;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/teste")
public class testeController {

    @GetMapping("/{n1}/{n2}")
    public ResponseEntity<Integer> soma(@PathVariable int n1, @PathVariable int n2){
        return ResponseEntity.status(HttpStatus.OK).body(n1+n2);
    }

}
