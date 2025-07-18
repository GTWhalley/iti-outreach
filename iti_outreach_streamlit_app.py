import streamlit as st

# -----------------------------
# Simple password protection
# -----------------------------
PASSWORD = "iti2025"

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    pw = st.text_input("Enter password to continue", type="password")
    if pw == PASSWORD:
        st.session_state["authenticated"] = True
        st.rerun()
    elif pw:
        st.error("Incorrect password")
    st.stop()

# -----------------------------
# Data
# -----------------------------
industries = [
    "Food & Beverage", "General Manufacturing", "Life Sciences",
    "Power & Utilities", "Nuclear", "Oil & Gas", "Warehousing & Logistics"
]
personas = [
    "Operations Manager", "Continuous Improvement Manager", "Plant Manager",
    "Director of Manufacturing", "IT/OT Manager", "Quality Manager",
    "Maintenance Manager", "Engineering Manager", "Automation Lead",
    "Production Supervisor"
]
tones = [
    "Warm & Collaborative", "Professional & Credible",
    "Technical & Insightful", "Strategic & Visionary"
]
company_sizes = [
    "Single Site / SMB", "Multi-Site / Mid-Market", "Global Enterprise"
]
solutions = [
    "OEE Performance Monitoring", "Track & Trace", "Scheduling & Planning",
    "Quality Management", "Maintenance Management", "Inventory Tracking",
    "ERP Integration", "SCADA & IIoT Integration", "Unspecified"
]

industry_snippets = {
    "Food & Beverage": "This sector prioritizes traceability, batch control, and minimizing downtime in high-throughput environments. ITI helps enable compliant, responsive operations across diverse product lines.",
    "Life Sciences": "Pharma and biotech operations demand precision, traceability, and validated systems. ITI supports digital manufacturing with SCADA, MES, and Track & Trace solutions designed for GxP environments.",
    "General Manufacturing": "Manufacturers often face legacy system fragmentation, unplanned downtime, and lack of real-time visibility. ITI helps bridge IT/OT gaps and deploy modular solutions to improve throughput.",
    "Power & Utilities": "In high-availability environments, reliability and control are paramount. ITI delivers integrated SCADA, historian, and maintenance systems tailored for critical infrastructure.",
    "Nuclear": "With strict regulatory standards, nuclear operations require validated, failsafe integration. ITI has experience delivering safety-critical automation and real-time monitoring solutions.",
    "Oil & Gas": "Oil & gas clients require robust integration across upstream/downstream operations. ITI supports these with SCADA, maintenance tracking, and safety system modernization.",
    "Warehousing & Logistics": "Visibility into inventory and scheduling is key in logistics environments. ITI enables better flow and traceability through MES, IIoT, and ERP integration."
}

persona_snippets = {
    "Operations Manager": "Operations Managers focus on improving uptime, streamlining workflows, and reducing production bottlenecks. ITI enables real-time visibility, actionable KPIs, and alerts that keep operations running smoothly.",
    "Continuous Improvement Manager": "Continuous Improvement professionals are data-driven and lean-focused. ITI empowers them with granular analytics, OEE metrics, and tools to act on performance gaps.",
    "Plant Manager": "Plant Managers oversee total site performance. ITI supports with systems that integrate data across departments and deliver insights for yield, availability, and downtime.",
    "Director of Manufacturing": "Directors of Manufacturing coordinate across multiple facilities and long-term strategy. ITI provides enterprise-wide tools to optimize production, standardize KPIs, and monitor assets at scale.",
    "IT/OT Manager": "IT/OT Managers bridge tech and ops. ITI provides secure, modular integrations to unify MES, SCADA, and ERP environments—reducing manual work and data silos.",
    "Quality Manager": "Quality Managers want traceability, audit readiness, and zero defects. ITI offers SPC, quality checks, and batch genealogy to keep output compliant and consistent.",
    "Maintenance Manager": "Maintenance Managers reduce unplanned downtime. ITI equips them with preventive maintenance tools, machine condition alerts, and historical repair data.",
    "Engineering Manager": "Engineering Managers lead technical delivery and reliability. ITI supports them with scalable control systems, performance tracking, and integration readiness.",
    "Automation Lead": "Automation Leads focus on streamlining manual processes and controls. ITI helps design and implement connected control systems using best-in-class platforms.",
    "Production Supervisor": "Production Supervisors keep lines running smoothly. ITI’s visibility tools provide clear KPIs, downtime logs, and performance views right from the shop floor."
}

def get_prompt_header(lead, company, location, title, persona, size, industry, tone, solution):
    if solution == "Unspecified":
        return f"""
Create a first-touch outreach email for {lead} at {company}, located in {location}, who works as {title}. This person fits the persona of a {persona} at a {size} organization in the {industry} sector. You are required to do a preliminary internet search to try and find as much information about this company as possible, specifically in the {location} area. Optional: return additional information about {lead} if certainty is 100% that this individual is the target lead.

Use a {tone} tone. Focus the email around how ITI Group can help them improve their plant operations through digital transformation. While no specific solution has been chosen, highlight our capabilities in performance visibility, traceability, system integration, and smart manufacturing. The goal is to open the door to a broader conversation around modernizing operations and uncovering opportunities.

This is for internal use as an LLM input prompt to generate subject and email body ONLY. Return the subject line first, then the body, clearly separated. Do not return instructions or metadata. Output must:

- NOT include em dashes (—)
- AVOID all typical LLM tropes like 3-item lists or generic flattery
- Be specific, helpful, and rooted in ITI Group’s value proposition
- Present ITI as a trusted systems integrator, not a product pusher
- Be brief and not trigger spam filters
- Mention the company name in the body
- Assume the outreach is starting with a wide lens to discover fit
- Use full sentences. Avoid excessive line breaks. Avoid clichés or filler language

Context: The writer is in business development at ITI Group, focused on helping manufacturers and industrial firms improve operations through digital solutions like MES, SCADA, OEE, and system integration.
"""
    else:
        return f"""
Create a first-touch outreach email for {lead} at {company}, located in {location}, who works as {title}. This person fits the persona of a {persona} at a {size} organization in the {industry} sector. You are required to do a preliminary internet search to try and find as much information about this company as possible, specifically in the {location} area. Optional: return additional information about {lead} if certainty is 100% that this individual is the target lead.

Use a {tone} tone. Focus the email around how ITI Group can help them through our {solution} solution. Make sure to speak to their likely operational priorities given their role, industry, and company size.

This is for internal use as an LLM input prompt to generate subject and email body ONLY. Return the subject line first, then the body, clearly separated. Do not return instructions or metadata. Output must:

- NOT include em dashes (—)
- AVOID all typical LLM tropes like 3-item lists or generic flattery
- Be specific, helpful, and rooted in ITI Group’s value proposition
- Present ITI as a trusted systems integrator, not a product pusher
- Be brief and not trigger spam filters
- Mention the company name in the body
- Assume the outreach is centered around the {solution} solution
- Use full sentences. Avoid excessive line breaks. Avoid clichés or filler language

Context: The writer is in business development at ITI Group, focused on helping manufacturers and industrial firms improve operations through digital solutions like MES, SCADA, OEE, and system integration.
"""

# -----------------------------
# App UI
# -----------------------------
st.title("ITI Outreach Prompt Generator")

with st.form("prompt_form"):
    col1, col2 = st.columns(2)
    with col1:
        company = st.text_input("Company Name")
        lead = st.text_input("Lead Name")
        title = st.text_input("Job Title")
        location = st.text_input("Location")

    with col2:
        industry = st.selectbox("Industry", industries)
        persona = st.selectbox("Persona", personas)
        size = st.selectbox("Company Size", company_sizes)
        tone = st.selectbox("Tone", tones)
        solution = st.selectbox("Solution", solutions)

    submitted = st.form_submit_button("Generate Prompt")

if submitted:
    header = get_prompt_header(lead, company, location, title, persona, size, industry, tone, solution)
    industry_context = industry_snippets.get(industry, "")
    persona_context = persona_snippets.get(persona, "")
    final_prompt = header.strip()
    final_prompt += f"\n\n{industry_context}\n\n{persona_context}"

    st.success("Prompt generated below:")
    # Display the generated prompt in a selectable text area
    st.text_area("Generated Prompt", value=final_prompt, height=400, key="output")

    # Add a helpful hint for the user to select/copy
    st.markdown("✅ Select all and press **Ctrl+C** (or Cmd+C on Mac) to copy the generated prompt. Paste it into ChatGPT or your LLM of choice.")


