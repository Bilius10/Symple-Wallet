package com.Carteira.Acao.CONTROLLER;

import com.Carteira.Acao.DTO.Devolucao.ErroDTO;
import com.Carteira.Acao.DTO.Recebimento.LoginDTO;
import com.Carteira.Acao.DTO.Recebimento.RegistroDTO;
import com.Carteira.Acao.ENTITY.Login;
import com.Carteira.Acao.EXCEPTIONS.RegraNegocioException;
import com.Carteira.Acao.SERVICES.LoginService;
import jakarta.validation.Valid;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/auth")
public class AuthController {

    @Autowired
    private LoginService loginService;

    @PostMapping("/registro")
    public ResponseEntity<Object> registro(@RequestBody @Valid RegistroDTO registroDTO) throws RegraNegocioException {

        try {

            Login recebeDTO = new Login();

            BeanUtils.copyProperties(registroDTO, recebeDTO);

            return ResponseEntity.status(HttpStatus.OK).body(loginService.criarConta(recebeDTO));

        } catch (Exception | RegraNegocioException error) {
            ErroDTO erroDTO = new ErroDTO(error.getMessage());
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(erroDTO);
        }

    }

    @PostMapping("/login")
    public ResponseEntity<Object> login(@RequestBody @Valid LoginDTO loginDTO) throws RegraNegocioException{

        try {

            Login recebeDTO = new Login();

            BeanUtils.copyProperties(loginDTO, recebeDTO);

            return ResponseEntity.status(HttpStatus.OK).body(loginService.login(recebeDTO));

        } catch (Exception | RegraNegocioException error) {
            ErroDTO erroDTO = new ErroDTO(error.getMessage());
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(erroDTO);
        }

    }
}
