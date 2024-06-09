from transformers import PreTrainedTokenizerFast, BartForConditionalGeneration
import pandas as pd

class TextSummarizer:
    def __init__(self, model_name="ainize/bart-base-cnn"):
        self.model_name = model_name
        self.tokenizer = PreTrainedTokenizerFast.from_pretrained(model_name)
        self.model = BartForConditionalGeneration.from_pretrained(model_name)

    def summarize(self, df, text_column='text', summary_column='summary'):
        # Ensure the summary column exists in the DataFrame
        if summary_column not in df.columns:
            df[summary_column] = ""

        # Infer BART model
        for i, row in df.iterrows():
            sequence = row[text_column]
            input_ids = self.tokenizer.encode(sequence, return_tensors="pt")
            # Generate Summary Text Ids
            summary_tokens = self.model.generate(
                input_ids=input_ids,
                bos_token_id=self.model.config.bos_token_id,
                eos_token_id=self.model.config.eos_token_id,
                length_penalty=2.0,
                max_length=100,
                min_length=1,
                num_beams=4,
            )
            summary = self.tokenizer.decode(summary_tokens[0], skip_special_tokens=True)
            df.at[i, summary_column] = summary
        return df
