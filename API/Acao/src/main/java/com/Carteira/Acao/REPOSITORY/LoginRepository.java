package com.Carteira.Acao.REPOSITORY;

import com.Carteira.Acao.ENTITY.Login;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.security.core.userdetails.UserDetails;

public interface LoginRepository extends JpaRepository<Login, Long> {

    @Query("SELECT l FROM Login l WHERE l.Login = :login")
    UserDetails findUserDetailsByName(String login);
}
