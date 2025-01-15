package com.Carteira.Acao.REPOSITORY;

import com.Carteira.Acao.ENTITY.Acoes;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface AcaoRepository extends JpaRepository<Acoes, Long> {

    @Query("select a from Acoes a where a.login.idLogin = :idLogin")
    List<Acoes> findAcoesByLoginIdLogin(Long idLogin);

    @Query("select sum(a.quantidade)from Acoes a where a.login.idLogin = :idLogin")
    Long findSumQuantidadeAcoesByLoginIdLogin(Long idLogin);

    @Query("select sum(a.Valor*a.quantidade)from Acoes a where a.login.idLogin = :idLogin")
    Double findSumValorAcoesByLoginIdLogin(Long idLogin);


}
