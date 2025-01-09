package com.Carteira.Acao.SERVICES;

import com.Carteira.Acao.REPOSITORY.LoginRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

@Service
public class AuthenticationService implements UserDetailsService {

    @Autowired
    private LoginRepository loginRepository;

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {

        try {
            return loginRepository.findUserDetailsByName(username);
        } catch (UsernameNotFoundException u) {
            throw new RuntimeException(u);
        }


    }
}
