package com.ohgiraffers.apirequest.test;

import com.ohgiraffers.apirequest.test.dto.RequestDTO;
import com.ohgiraffers.apirequest.test.dto.ResponseDTO;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/ask_question")
@Slf4j
public class QaController {

    private final QaService qaService;

    public QaController(QaService qaService) {
        this.qaService = qaService;
    }

    @PostMapping
    public ResponseDTO questionTest(@RequestBody RequestDTO requestDTO) {

        log.info("번역[RestTemplate] Controller 요청 들어옴...");
        log.info("question: {}", requestDTO.getQuestion());

        ResponseDTO result = qaService.translateText(requestDTO);

        return result;
    }
}
