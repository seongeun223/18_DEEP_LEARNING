package com.ohgiraffers.apirequest.test;

import com.ohgiraffers.apirequest.test.dto.RequestDTO;
import com.ohgiraffers.apirequest.test.dto.ResponseDTO;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClientException;
import org.springframework.web.client.RestTemplate;

@Service
@Slf4j
public class QaService {

    private final RestTemplate restTemplate;

    private final String FAST_API_SERVER_URL = "http://localhost:8000/ask_question/";

    public QaService(RestTemplate restTemplate) {
        this.restTemplate = new RestTemplate();
    }

    public ResponseDTO translateText(RequestDTO requestDTO) {

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<RequestDTO> entity = new HttpEntity<>(requestDTO, headers);

        try {
            ResponseEntity<ResponseDTO> response = restTemplate.exchange(
                    FAST_API_SERVER_URL,
                    HttpMethod.POST,
                    entity,
                    ResponseDTO.class
            );

            log.info("=== 서비스 응답 데이터 ===");
            log.info("결과 : {}", response.getBody().getTranslated_question(), response.getBody().getEnglish_answer(), response.getBody().getKorean_answer());

            return response.getBody();
        } catch (RestClientException e) {
            throw new RuntimeException(e);
        }
    }
}
