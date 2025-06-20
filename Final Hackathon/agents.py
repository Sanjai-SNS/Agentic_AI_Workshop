# agents.py
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

def feedback_agent(llm):
    prompt = PromptTemplate.from_template("""
You are a feedback summarizer.
Summarize pain points, requests, UX issues, and positives in:

{feedback}
""")
    return prompt | llm

def persona_agent(llm, persona):
    prompt = PromptTemplate.from_template(f"""
You are a {persona}.
Interpret feedback from your perspective:

Feedback:
{{feedback}}
""")
    return prompt | llm

def refinement_agent(llm):
    prompt = PromptTemplate.from_template("""
Refine this project idea based on feedback:

Idea: {idea}
Feedback: {feedback}
""")
    return prompt | llm

def analysis_agent(llm):
    prompt = PromptTemplate.from_template("""
Assess this idea strategically:

Idea: {idea}
Feedback: {feedback}
""")
    return prompt | llm
