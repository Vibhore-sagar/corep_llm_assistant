from fastapi import FastAPI
from app.rag.retrieve import retrieve_context
from app.llm.mapper import map_to_corep
from app.validation.rules import validate_response
from app.audit.logger import log_audit

app = FastAPI()


@app.get("/generate_corep")
def generate_corep(query: str):

    context = retrieve_context(query)

    corep_json = map_to_corep(context, query)

    errors = validate_response(corep_json)

    corep_json["validation_errors"] = errors

    log_audit(query, context, corep_json)

    return corep_json
