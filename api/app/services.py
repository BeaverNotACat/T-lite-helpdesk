from transformers import AutoModelForCausalLM, AutoTokenizer
from app.schemas import Responce


class AssistService:
    """TLite interface"""

    def __init__(self, model, tokenizer):
        self.model = model
        self.tokenizer = tokenizer

    @staticmethod
    def _generate_prompt(query):
        """Generate model prompt"""
        return [
            {"role": "user", "content": query},
        ]

    def _tokenize_input(self, query):
        """Creates chat-like tokenised input for llvm"""
        input_ids = self.tokenizer.apply_chat_template(
            self._generate_prompt(query),
            add_generation_prompt=True,
            return_tensors="pt",
        ).to(self.model.device)

    def _get_eos_tokens(self):
        """Get eos tokens for llvm generation"""
        return [
            self.tokenizer.eos_token_id,
            self.tokenizer.convert_tokens_to_ids("<|eot_id|>"),
        ]

    def assist(self, query):
        "Generate models output"
        outputs = self.model.generate(
            self._tokenize_input(query),
            max_new_tokens=256,
            eos_token_id=self._get_eos_tokens(),
        )

        return Responce(self.tokenizer.decode(outputs[0], skip_special_tokens=True)) # TODO Add responce serialisation
