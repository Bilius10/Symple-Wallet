package com.Carteira.Acao.REPOSITORY;

import com.Carteira.Acao.ENTITY.Acoes;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface AcaoRepository extends JpaRepository<Acoes, Long> {
}
