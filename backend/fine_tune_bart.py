from transformers import BartForConditionalGeneration, BartTokenizer, Trainer, TrainingArguments
import torch
from datasets import Dataset

# Load dataset
from data_preprocessor import load_tickets, prepare_dataset

# Load and preprocess data
df = load_tickets()
dataset = prepare_dataset(df)

# Convert to Hugging Face dataset
hf_dataset = Dataset.from_list(dataset)

# Load tokenizer and model
MODEL_NAME = "facebook/bart-large"
tokenizer = BartTokenizer.from_pretrained(MODEL_NAME)
model = BartForConditionalGeneration.from_pretrained(MODEL_NAME)

# Tokenization function
def preprocess_function(examples):
    model_inputs = tokenizer(examples["input"], max_length=512, truncation=True, padding="max_length")
    labels = tokenizer(examples["output"], max_length=128, truncation=True, padding="max_length")
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

# Tokenize dataset
tokenized_dataset = hf_dataset.map(preprocess_function, batched=True)

# Training arguments
training_args = TrainingArguments(
    output_dir="./bart_fine_tuned",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    logging_dir="./logs",
    num_train_epochs=3
)

# Trainer setup
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    eval_dataset=tokenized_dataset
)

# Train model
trainer.train()
model.save_pretrained("fine_tuned_bart")
tokenizer.save_pretrained("fine_tuned_bart")
