from pydantic import BaseModel, computed_field
from typing import Optional, List, Any, Dict


class PerplexityResponse(BaseModel):
    """Complete Perplexity API response structure"""
    backend_uuid: str
    context_uuid: Optional[str] = None
    uuid: str
    frontend_context_uuid: Optional[str] = None
    frontend_uuid: Optional[str] = None
    text: str  # JSON stringificato contenente gli step
    thread_title: Optional[str] = None
    related_queries: Optional[List[str]] = None
    display_model: Optional[str] = None
    user_selected_model: Optional[str] = None
    personalized: Optional[bool] = None
    mode: Optional[str] = None
    query_str: Optional[str] = None
    search_focus: Optional[str] = None
    source: Optional[str] = None
    attachments: Optional[List[Any]] = None
    updated_datetime: Optional[str] = None
    read_write_token: Optional[str] = None
    is_pro_reasoning_mode: Optional[bool] = None
    step_type: Optional[str] = None
    bookmark_state: Optional[str] = None
    s3_social_preview_url: Optional[str] = None
    thread_access: Optional[int] = None
    thread_url_slug: Optional[str] = None
    prompt_source: Optional[str] = None
    query_source: Optional[str] = None
    expect_search_results: Optional[str] = None
    plan: Optional[Dict[str, Any]] = None
    privacy_state: Optional[str] = None
    gpt4: Optional[bool] = None
    sources: Optional[Dict[str, Any]] = None
    text_completed: Optional[bool] = None
    entry_updated_datetime: Optional[str] = None
    blocks: Optional[List[Dict[str, Any]]] = None
    final_sse_message: Optional[bool] = None

    @computed_field
    @property
    def answer(self) -> Optional[str]:
        """
        Estrae la risposta dal primo block con intended_usage == "ask_text"

        Returns:
            str: Il contenuto di markdown_block.answer se trovato
            None: Se non viene trovato alcun block con intended_usage "ask_text"
        """
        if not self.blocks:
            return None

        for block in self.blocks:
            if block.get('intended_usage') == 'ask_text':
                markdown_block = block.get('markdown_block')
                if markdown_block:
                    return markdown_block.get('answer')

        return None

