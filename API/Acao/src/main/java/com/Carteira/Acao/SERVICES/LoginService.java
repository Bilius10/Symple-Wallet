package com.Carteira.Acao.SERVICES;

import com.Carteira.Acao.ENTITY.Login;
import com.Carteira.Acao.EXCEPTIONS.RegraNegocioException;
import com.Carteira.Acao.INFRASECURITY.TokenService;
import com.Carteira.Acao.REPOSITORY.LoginRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class LoginService {

    @Autowired
    private LoginRepository loginRepository;
    @Autowired
    private AuthenticationManager authenticationManager;
    @Autowired
    private TokenService tokenService;

    public Login criarConta(Login login) throws RegraNegocioException {

        Optional<Login> jaExiste = loginRepository.findLoginByCpf(login.getCpf());

        if(jaExiste.isPresent()){
            new RegraNegocioException("Já existe alguem com esse cpf");
        }

        String encryptedPassword = new BCryptPasswordEncoder().encode(login.getSenha());
        login.setSenha(encryptedPassword);

        return loginRepository.save(login);
    }

    public String login(Login login) throws RegraNegocioException{

        Optional<Login> encontreUsuario = loginRepository.findLoginByCpf(login.getCpf());

        if(encontreUsuario.isEmpty()){
            new RegraNegocioException("Cpf incorreto");
        }

        var usernamePasswordAuthenticationToken = new UsernamePasswordAuthenticationToken(login.getUsername(), login.getPassword());
        System.out.println(usernamePasswordAuthenticationToken.getCredentials());
        var auth = this.authenticationManager.authenticate(usernamePasswordAuthenticationToken);
        System.out.println(3);
        var token = tokenService.generateToken((Login) auth.getPrincipal());

        return token;
    }
}
