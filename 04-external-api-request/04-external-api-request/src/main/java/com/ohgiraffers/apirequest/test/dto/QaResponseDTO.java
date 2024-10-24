package com.ohgiraffers.apirequest.test.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class QaResponseDTO {

    private String translated_question;
    private String english_answer;
    private String korean_answer;
}
