from celery import shared_task
import os
import json
from openai import OpenAI
from apps.authentication.models import StudentProfile

@shared_task
def generate_three_paths_task(profile_id):
    try:
        profile = StudentProfile.objects.get(id=profile_id)
        # Fetch their latest marks to give context to the AI
        marks = profile.marks.filter(year=2026).select_related('subject')
        marks_summary = ", ".join([f"{m.subject.get_name_display()}: {m.percentage}%" for m in marks])
        
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
        # Inject hyper-localized South African parameters
        system_prompt = (
            "You are a South African tertiary education expert. Analyze the student's high school marks "
            "and generate exactly 3 highly specific career/educational pathways tailored for South Africa. "
            "Path 1: Traditional University Route. Path 2: TVET College / Artisanal Route. "
            "Path 3: Scarcity Skills / Direct-to-Market Tech/Venture Route. "
            "Take APS scores, NSFAS eligibility variables, and local job market demand into consideration. "
            "Return the output STRICTLY as raw JSON with keys: 'path_1', 'path_2', 'path_3'."
        )
        
        user_prompt = f"Student is in Grade {profile.grade} living in {profile.get_province_display()}. Current Marks: {marks_summary}."
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        
        result_json = json.loads(response.choices[0].message.content)
        
        # Save output to a CareerResult model cache (Model not shown here for brevity)
        # cache_result(profile, result_json)
        return result_json

    except Exception as e:
        return {"error": str(e)}