package com.Carteira.Acao.SERVICES;

import com.Carteira.Acao.ENTITY.Acoes;
import com.Carteira.Acao.REPOSITORY.AcaoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class AcaoService {

    @Autowired
    private AcaoRepository acaoRepository;

    public Acoes saveAcao(Acoes acoes){
        return acaoRepository.save(acoes);
    }

}
