package com.Carteira.Acao.REPOSITORY;

import com.Carteira.Acao.ENTITY.Login;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.security.core.userdetails.UserDetails;

import java.util.Optional;

public interface LoginRepository extends JpaRepository<Login, Long> {

    @Query("SELECT l FROM Login l WHERE l.Login = :login")
    UserDetails findUserDetailsByName(String login);

    @Query("SELECT l.cpf FROM Login l WHERE l.cpf = :cpf")
    Optional<Login> findLoginByCpf(String cpf);
}
