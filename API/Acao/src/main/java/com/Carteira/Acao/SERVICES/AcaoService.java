package com.Carteira.Acao.SERVICES;

import com.Carteira.Acao.DTO.Devolucao.InfoAcaoDTO;
import com.Carteira.Acao.DTO.MelhorPiorAcao;
import com.Carteira.Acao.ENTITY.Acoes;
import com.Carteira.Acao.ENTITY.Login;
import com.Carteira.Acao.EXCEPTIONS.RegraNegocioException;
import com.Carteira.Acao.REPOSITORY.AcaoRepository;
import com.Carteira.Acao.REPOSITORY.LoginRepository;
import com.Carteira.Acao.Utils.Utilidades;
import com.fasterxml.jackson.core.JsonProcessingException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class AcaoService {

    @Autowired
    private AcaoRepository acaoRepository;
    @Autowired
    private LoginRepository loginRepository;
    @Autowired
    private Utilidades utilidades;

    public Acoes saveAcao(Acoes acoes, Long idUsuario) throws RegraNegocioException{

        Optional<Login> usuarioExiste = loginRepository.findById(idUsuario);

        if(usuarioExiste.isEmpty()){
            throw new RegraNegocioException("Houve um erro com seu id de usuario");
        }

        Optional<Acoes> acaoExiste = acaoRepository.findAcoesByCodigo(acoes.getCodigo());

        if(acaoExiste.isPresent()){
            acaoExiste.get().setValor(acoes.getValor());
            acaoExiste.get().setQuantidade(acoes.getQuantidade()+acaoExiste.get().getQuantidade());

            return acaoRepository.save(acaoExiste.get());
        }

        acoes.setLogin(usuarioExiste.get());

        return acaoRepository.save(acoes);
    }

    public InfoAcaoDTO infoAcao(Long idUsuario) throws RegraNegocioException, JsonProcessingException {

        Optional<Login> usuarioExiste = loginRepository.findById(idUsuario);

        if(usuarioExiste.isEmpty()){
            throw new RegraNegocioException("Houve um erro com seu id de usuario");
        }

        Double somaValor = acaoRepository.findSumValorAcoesByLoginIdLogin(idUsuario);
        Long somaQuantidade = acaoRepository.findSumQuantidadeAcoesByLoginIdLogin(idUsuario);
        List<Acoes> listaAcoes = acaoRepository.findAcoesByLoginIdLogin(idUsuario);
        MelhorPiorAcao melhorPiorAcao = utilidades.MelhorePiorAcao(listaAcoes);
        InfoAcaoDTO infoAcaoDTO = new InfoAcaoDTO(somaValor, listaAcoes, somaQuantidade, melhorPiorAcao.melhorAcao(), melhorPiorAcao.piorAcao());
        return infoAcaoDTO;
    }

}
