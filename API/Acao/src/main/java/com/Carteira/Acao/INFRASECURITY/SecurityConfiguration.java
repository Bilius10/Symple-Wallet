package com.Carteira.Acao.INFRASECURITY;

import com.Carteira.Acao.SERVICES.AuthenticationService;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpMethod;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.config.annotation.authentication.configuration.AuthenticationConfiguration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configurers.AbstractHttpConfigurer;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    private final SecurityFIlter securityFilter;
    private final AuthenticationService authenticationService;

    public SecurityConfiguration(SecurityFIlter securityFilter, AuthenticationService authenticationService) {
        this.securityFilter = securityFilter;
        this.authenticationService = authenticationService;
    }

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity httpSecurity) throws Exception {
        return httpSecurity
                .csrf(AbstractHttpConfigurer::disable)
                .sessionManagement(session -> session.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
                .authorizeHttpRequests(authorize -> authorize
                        .requestMatchers(HttpMethod.POST, "/auth/registro").permitAll()
                        .requestMatchers(HttpMethod.POST, "/auth/login").permitAll()
                        .requestMatchers(HttpMethod.GET, "/external/API/nomes").permitAll()
                        .requestMatchers(HttpMethod.GET, "/external/API/{nome}").permitAll()
                        .requestMatchers(HttpMethod.GET, "/external/API/30dias/{acao}").permitAll()
                        .requestMatchers(HttpMethod.POST, "/acao/save").hasRole("NORMAL")
                        .requestMatchers(HttpMethod.GET, "/acao/infoAcao/{idUsuario}").hasRole("NORMAL")
                        .requestMatchers(HttpMethod.GET, "/acao/usuario/{idUsuario}").hasRole("NORMAL")
                        .anyRequest().authenticated()
                )
                .addFilterBefore(securityFilter, UsernamePasswordAuthenticationFilter.class)
                .build();
        }

        @Bean
        public AuthenticationManager authenticationManager(AuthenticationConfiguration authenticationConfiguration) throws Exception {
            return authenticationConfiguration.getAuthenticationManager();
        }

        @Bean
        public PasswordEncoder passwordEncoder() {
            return new BCryptPasswordEncoder();
        }
}
