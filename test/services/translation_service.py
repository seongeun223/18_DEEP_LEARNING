from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
from utils.postprocess import postprocess_translation

# 번역 모델 및 토크나이저 설정
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
    return translation_tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

def english_to_korean(input_text):
    translation_tokenizer.src_lang = "en_XX"
    encoded_en = translation_tokenizer(input_text, return_tensors="pt")
    generated_tokens = translation_model.generate(
        **encoded_en,
        forced_bos_token_id=translation_tokenizer.lang_code_to_id["ko_KR"]
    )
    output_text = translation_tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

    # 번역 후 결과 출력
    print(f"Before postprocess: {output_text}")

    # postprocess_translation 적용
    processed_text = [postprocess_translation(text) for text in output_text]

    # 후처리 후 결과 출력
    print(f"After postprocess: {processed_text}")

    return processed_text