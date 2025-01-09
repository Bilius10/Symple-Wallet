package com.Carteira.Acao.ENTITY;

import com.Carteira.Acao.ENUM.NivelPermissao;
import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import java.io.Serial;
import java.io.Serializable;
import java.util.Collection;
import java.util.List;

@Entity
@AllArgsConstructor
@ToString
public class Login implements UserDetails, Serializable {

    @Serial
    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long idLogin;
    private String login;
    private String senha;
    private String cpf;

    @OneToMany(mappedBy = "login")
    @JsonIgnore
    private List<Acoes> acoes;

    @Enumerated(EnumType.STRING)
    private NivelPermissao nivelPermissao;

    private boolean accountNonExpired;
    private boolean accountNonLocked;
    private boolean credentialsNonExpired;
    private boolean enabled;

    public Login() {
        this.nivelPermissao = NivelPermissao.NORMAL;
        this.accountNonExpired = true;
        this.accountNonLocked = true;
        this.credentialsNonExpired = true;
        this.enabled = true;

    }

    public Long getIdLogin() {
        return idLogin;
    }

    public void setIdLogin(Long idLogin) {
        this.idLogin = idLogin;
    }

    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
        if(this.nivelPermissao == NivelPermissao.ADMIN){
            return List.of(new SimpleGrantedAuthority("ROLE_ADMIN"),
                    new SimpleGrantedAuthority("ROLE_NORMAL"));
        }else{
            return List.of(new SimpleGrantedAuthority("ROLE_NORMAL"));
        }
    }

    @Override
    public String getPassword() {
        return this.senha;
    }

    @Override
    public String getUsername() {
        return this.cpf;
    }

    @Override
    public boolean isAccountNonExpired() {
        return this.accountNonExpired;
    }

    @Override
    public boolean isAccountNonLocked() {
        return this.accountNonLocked;
    }

    @Override
    public boolean isCredentialsNonExpired() {
        return this.credentialsNonExpired;
    }

    @Override
    public boolean isEnabled() {
        return this.enabled;
    }
}
