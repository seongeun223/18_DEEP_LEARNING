package com.ohgiraffers.apirequest.test.dto;

import lombok.*;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@ToString
public class QaResponseDTO {

    private String translated_question;
    private String english_answer;
    private String korean_answer;
}
