def postprocess_translation(text):
    print("postprocess_translation 함수가 호출되었습니다.")
    print(f"Postprocess input text: {text}")
    corrections = {
        r"(\d+)\s*days of receipt": r"수령 후 \1일",  # 숫자 처리 (7일 후 배달 -> 수령 후 7일)
        r"Order/Payment Inquiry": "주문/결제 문의",
        r"Shipping Inquiry": "배송 문의",
        r"Product Exchange/Return Inquiry": "상품 교환/반품 문의",
        r"Refund Inquiry": "환불 문의",
        r"Product Inquiry": "상품 문의",
        r"Other Inquiry": "기타 문의",
        r"order/payment[-\s]related inquiries": "주문/결제 관련 문의",
        r"2-3 business days of payment": "결제 후 2-3 영업일 이내",
        r"shipping may be delayed": "배송이 지연될 수 있습니다.",
        r"Product exchanges and returns are accepted within 7 days of receipt":
            "상품의 교환 및 반품은 수령 후 7일 이내에 가능합니다",
        r"Refunds are accepted within 7 days of receipt":
            "환불은 수령 후 7일 이내에 가능합니다",
        r"You can request a refund by visiting our website":
            "환불 요청은 당사 웹사이트에서 할 수 있습니다",
        r"You can find detailed information about the product":
            "상품 페이지에서 사이즈, 색상, 재질 등의 상세 정보를 확인할 수 있습니다",
        r"please contact our customer service center at 1234-5678":
            "고객 서비스 센터 1234-5678로 문의해 주세요",
        r"7 days of receipt": "수령 후 7일",
        r"7일 후 배달": "수령 후 7일",
        r"KRW": "원",
        r"size": "사이즈",
        r"color": "색상",
        r"material": "재질",
        r"product": "상품",
        r"제품": "상품",
        r"재질는": "재질은",
        r"代理": "대행",
        r"refundable": "환불",
        r"회신": "반품"
    }
    
    for wrong, correct in corrections.items():
        text = text.replace(wrong, correct)

    print(f"Postprocessed text: {text}")
    return text
