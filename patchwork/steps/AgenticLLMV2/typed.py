from typing_extensions import Annotated, Any, Dict, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class AgenticLLMV2Inputs(TypedDict, total=False):
    base_path: str
    prompt_value: Dict[str, Any]
    system_prompt: str
    user_prompt: str
    max_agent_calls: Annotated[int, StepTypeConfig(is_config=True)]
    google_api_key: str
    anthropic_api_key: str
    openai_api_key: str
    strategy_model: str
    agent_model: str
    agent_system_prompt: str
    example_json: Dict


class AgenticLLMV2Outputs(TypedDict):
    request_tokens: int
    response_tokens: int
