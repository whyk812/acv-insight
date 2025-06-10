# modules/llm.py
import os
import openai
from dotenv import load_dotenv

# .env에서 OPENAI_API_KEY 불러오기
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_insights(stats: dict, chart_paths: list) -> str:
    """
    stats: {컬럼명: {'mean':…, 'std':…, 'min':…, 'max':…}, …}
    chart_paths: ['outputs/score_hist.png', …]
    이 두 정보를 토대로, OpenAI에 요약을 요청하고
    반환된 자연어 인사이트 텍스트를 돌려줍니다.
    """
    # 1) 통계 텍스트 만들기
    stats_lines = []
    for col, vals in stats.items():
        stats_lines.append(
            f"- '{col}' 평균 {vals['mean']:.2f}, 표준편차 {vals['std']:.2f}, "
            f"최솟값 {vals['min']:.2f}, 최댓값 {vals['max']:.2f}"
        )
    stats_text = "\n".join(stats_lines)

    # 2) 차트 정보 문자열
    charts_text = "\n".join(f"- {path}" for path in chart_paths)

    # 3) 프롬프트 구성
    prompt = (
        "아래는 CSV 데이터의 주요 통계치와 시각화된 차트 파일 목록입니다.\n\n"
        "【통계치】\n"
        f"{stats_text}\n\n"
        "【차트 파일】\n"
        f"{charts_text}\n\n"
        "위 정보를 참고하여, 데이터에 대한 주요 인사이트를 "
        "친절한 한국어 문장 3~4문장으로 요약해 주세요."
    )

    # 4) OpenAI API 호출
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
        temperature=0.5,
    )
    return response.choices[0].message.content.strip()
