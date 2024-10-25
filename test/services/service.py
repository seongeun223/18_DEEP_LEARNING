from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
from services.translation_service import korean_to_english, english_to_korean

# QA 모델 설정
model_name = "deepset/roberta-base-squad2"
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# context를 유지하는 텍스트
context = """
Order/Payment Inquiry: For order/payment-related inquiries regarding overseas purchase agency products, please contact our customer service center at 1234-5678.
Shipping Inquiry: Your order will be shipped within 2-3 business days of payment, and it will take approximately 3-5 business days to arrive. However, shipping may be delayed during weekends and holidays. 
You can track your order on our website.
Product Exchange/Return Inquiry: Product exchanges and returns are accepted within 7 days of receipt. However, if the product is damaged or has been used, it cannot be exchanged or returned. 
You can request an exchange or return by visiting our website, and you will be charged for round-trip international shipping costs (30,000 KRW).
Refund Inquiry: Refunds are accepted within 7 days of receipt. However, if the product is damaged or has been used, it cannot be refunded. 
You can request a refund by visiting our website, and you will be refunded the amount paid minus international shipping costs (30,000 KRW).
Product Inquiry: For product-related inquiries, please visit our website. 
You can find detailed information about the product, including size, color, and material, on the product page. If you have any additional questions, please contact our customer service center at 1234-5678.
Other Inquiry: If you have any other questions, please contact our customer service center at 1234-5678.
"""

async def answer_question(question: str):
    # 1. 한글 질문을 영어로 번역
    translated_question = korean_to_english(question)[0]

    # 2. QA 파이프라인 설정 및 실행
    nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
    QA_input = {
        'question': translated_question,
        'context': context
    }
    res = nlp(QA_input)
    en_answer = res['answer']

    # 3. 영어로 된 답변을 한국어로 번역
    answer = english_to_korean(en_answer)[0]

    # 4. 번역된 답변 반환
    return {"translated_question": translated_question, "english_answer": en_answer, "korean_answer": answer}
