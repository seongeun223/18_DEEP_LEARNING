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
        "배달": "배송",
        "7 days of receipt": "수령 후 7일",
        "size" : "사이즈",
        "color": "색상",
        "material": "재질"
    }
    
    text_lower = text.lower()
    for wrong, correct in corrections.items():
        text_lower = text_lower.replace(wrong, correct)

    print(f"Postprocessed text: {text_lower}")
    
    return text_lower
