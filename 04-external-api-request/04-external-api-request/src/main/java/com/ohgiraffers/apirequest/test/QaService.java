package com.ohgiraffers.apirequest.test;

import com.ohgiraffers.apirequest.test.dto.QaRequestDTO;
import com.ohgiraffers.apirequest.test.dto.QaResponseDTO;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClientException;
import org.springframework.web.client.RestTemplate;

@Service
@Slf4j
public class QaService {

    private final RestTemplate restTemplate;

    private final String FAST_API_SERVER_URL = "http://localhost:8000/ask_question";

    public QaService(RestTemplate restTemplate) {
        this.restTemplate = new RestTemplate();
    }

    public QaResponseDTO translateText(QaRequestDTO qaRequestDTO) {

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<QaRequestDTO> entity = new HttpEntity<>(qaRequestDTO, headers);

        try {
            ResponseEntity<QaResponseDTO> response = restTemplate.exchange(
                    FAST_API_SERVER_URL,
                    HttpMethod.POST,
                    entity,
                    QaResponseDTO.class
            );

            log.info("=== 서비스 응답 데이터 ===");
            log.info("결과 : {}", response.getBody());

            return response.getBody();
        } catch (RestClientException e) {
            throw new RuntimeException(e);
        }
    }
}
