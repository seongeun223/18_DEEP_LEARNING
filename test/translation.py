from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

# 1. 번역 모델과 토크나이저 불러오기
model_name_translation = "facebook/mbart-large-50-many-to-many-mmt"
translation_model = MBartForConditionalGeneration.from_pretrained(model_name_translation)
translation_tokenizer = MBart50TokenizerFast.from_pretrained(model_name_translation)

def korean_to_english(input_text):
    translation_tokenizer.src_lang = "ko_KR"
    encoded_ko = translation_tokenizer(input_text, return_tensors="pt")
    generated_tokens = translation_model.generate(
        **encoded_ko,
        forced_bos_token_id=translation_tokenizer.lang_code_to_id["en_XX"]
    )
    output_text = translation_tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return output_text

def english_to_korean(input_text):
    translation_tokenizer.src_lang = "en_XX"
    encoded_en = translation_tokenizer(input_text, return_tensors="pt")
    generated_tokens = translation_model.generate(
        **encoded_en,
        forced_bos_token_id=translation_tokenizer.lang_code_to_id["ko_KR"]
    )
    output_text = translation_tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    
    translated_texts = [postprocess_translation(text) for text in output_text]
    return translated_texts

def postprocess_translation(text):
    corrections = {
        "KRW": "원",
        "営業": "영업",
        "Product Inquiry": "제품 문의",
        "Refund Inquiry": "환불 문의",
        "Shipping Inquiry": "배송 문의",
        "Order/Payment Inquiry": "주문/결제 문의",
        "refundable": "환불",
        "refunded": "환불",
        "교환과 교환": "교환 및 반품",
        "받아들여집니다.": "가능합니다.",
        "ご注文": "주문",
        "주문은 2-3일 내에 배달됩니다.": "주문 후 2-3일 내에 발송됩니다.",
        "다른 질문이 있다면": "추가 문의사항이 있다면 고객센터 1234-5678로 문의 부탁드립니다.",
        "배달": "배송"
    }
    
    for wrong, correct in corrections.items():
        text = text.replace(wrong, correct)
    
    return text
