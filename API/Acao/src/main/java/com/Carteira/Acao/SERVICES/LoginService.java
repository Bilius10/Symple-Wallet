package com.Carteira.Acao.SERVICES;

import com.Carteira.Acao.ENTITY.Login;
import com.Carteira.Acao.EXCEPTIONS.RegraNegocioException;
import com.Carteira.Acao.REPOSITORY.LoginRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class LoginService {

    @Autowired
    private LoginRepository loginRepository;

    public Login criarConta(Login login) throws RegraNegocioException {
        System.out.println(1);
        Optional<Login> jaExiste = loginRepository.findLoginByCpf(login.getCpf());
        System.out.println(2);
        if(jaExiste.isPresent()){
            new RegraNegocioException("Já existe alguem com esse cpf");
        }
        System.out.println(3);
        String encryptedPassword = new BCryptPasswordEncoder().encode(login.getSenha());
        login.setSenha(encryptedPassword);
        System.out.println(4);
        return loginRepository.save(login);
    }
}
