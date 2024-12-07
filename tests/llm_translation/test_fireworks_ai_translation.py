import os
import sys

import pytest

sys.path.insert(
    0, os.path.abspath("../..")
)  # Adds the parent directory to the system path

from litellm.llms.fireworks_ai.chat.fireworks_ai_transformation import FireworksAIConfig
from base_llm_unit_tests import BaseLLMChatTest

fireworks = FireworksAIConfig()


def test_map_openai_params_tool_choice():
    # Test case 1: tool_choice is "required"
    result = fireworks.map_openai_params({"tool_choice": "required"}, {}, "some_model")
    assert result == {"tool_choice": "any"}

    # Test case 2: tool_choice is "auto"
    result = fireworks.map_openai_params({"tool_choice": "auto"}, {}, "some_model")
    assert result == {"tool_choice": "auto"}

    # Test case 3: tool_choice is not present
    result = fireworks.map_openai_params(
        {"some_other_param": "value"}, {}, "some_model"
    )
    assert result == {}

    # Test case 4: tool_choice is None
    result = fireworks.map_openai_params({"tool_choice": None}, {}, "some_model")
    assert result == {"tool_choice": None}


class TestFireworksAIChatCompletion(BaseLLMChatTest):
    def get_base_completion_call_args(self) -> dict:
        return {
            "model": "fireworks_ai/accounts/fireworks/models/llama-v3p2-11b-vision-instruct"
        }

    def test_tool_call_no_arguments(self, tool_call_no_arguments):
        """Test that tool calls with no arguments is translated correctly. Relevant issue: https://github.com/BerriAI/litellm/issues/6833"""
        pass

    def test_multilingual_requests(self):
        """
        Fireworks AI raises a 500 BadRequest error when the request contains invalid utf-8 sequences.
        """
        pass
