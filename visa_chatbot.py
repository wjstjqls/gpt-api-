# ✅ OpenAI 패키지 불러오기
# GPT API를 사용하려면 openai 패키지가 필요해. 설치 안됐다면 'pip install openai'
import openai

# 🔐 OpenAI API 키 설정
# https://platform.openai.com/account/api-keys 에서 발급받은 키를 아래에 입력해야 함
openai.api_key = ""  # 👉 여기에 본인의 OpenAI 키를 입력하세요

# 🧠 시스템 프롬프트 설정
# GPT가 어떤 역할을 수행할지 알려주는 지시문 (처음에 반드시 줘야 함)
system_prompt = {
    "role": "system",
    "content": (
        "당신은 미국 유학 F1 비자에 대한 전문가인 BORA입니다. "
        "사용자가 질문하면 정확하고 친절하게 안내해주세요. "
        "확실하지 않은 내용은 추측하지 말고 '정확한 정보를 드릴 수 없습니다'라고 답해주세요."
    )
}

# 🗂️ 대화 이력을 저장하는 리스트 초기화 (GPT는 이걸 보고 맥락을 이해함)
messages = [system_prompt]

# 📢 사용자에게 안내 메시지 출력
print("🇺🇸 F1 비자 GPT 챗봇입니다. 무엇이든 물어보세요!")
print("💬 종료하려면 'exit' 또는 'quit'을 입력하세요.\n")

# 🔁 무한 루프로 사용자 입력 계속 받기
while True:
    # 🧑 사용자 입력 받기
    user_input = input("👤 나: ")

    # ⛔ 종료 조건 체크
    if user_input.lower() in ["exit", "quit"]:
        print("👋 챗봇을 종료합니다. 이용해주셔서 감사합니다!")
        break

    # 📩 사용자 입력을 messages 리스트에 추가
    messages.append({"role": "user", "content": user_input})

    # 🤖 GPT API 호출: 지금까지의 대화 이력을 전달
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",         # 모델명: gpt-3.5-turbo 도 가능
            messages=messages      # 대화 이력 전체를 보내야 GPT가 맥락을 파악함
        )

        # 📤 GPT 응답 텍스트만 추출
        reply = response['choices'][0]['message']['content']

        # 💬 GPT의 응답을 터미널에 출력
        print("🤖 GPT:", reply)

        # 🗂️ GPT 응답도 대화 이력에 추가 (다음 질문을 위해)
        messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        # ⚠️ 오류 발생 시 사용자에게 알림
        print("❗ 오류가 발생했습니다:", e)
