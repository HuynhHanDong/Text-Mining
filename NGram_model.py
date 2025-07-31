import re
import random
from collections import defaultdict, Counter

def preprocess_text(text):
    # Lowercase and remove non-alphanumeric characters except spaces
    return re.sub(r'[^a-zA-Z\s]', '', text.lower())

def build_ngram_model(text, n):
    words = text.split()
    model = defaultdict(Counter)

    for i in range(len(words) - n + 1):
        # Get the context (first n-1 words)
        context = tuple(words[i:i+n-1])
        # Get the next word
        next_word = words[i+n-1]
        # Add to model
        model[context][next_word] += 1
    
    return dict(model)

def generate_text(model, seed, length):
    # Preprocess seed and split into words
    seed_words = preprocess_text(seed).split()
    result = seed_words.copy()

    # Determine n-gram order from model
    n_order  = len(next(iter(model))) + 1 if model else 1

    # Generate text
    for _ in range(length):
        # Get current context (last n-1 words)
        if len(result) >= n_order - 1:
            context = tuple(result[-(n_order-1):])
        else:
            # If we don't have enough context, use what we have
            context = tuple(result)

        # Find possible next words
        if context in model:
            next_words = model[context]
            # Create weighted list for random selection
            words = list(next_words.keys())
            weights = list(next_words.values())
            
            # Randomly select next word based on probability
            next_word = random.choices(words, weights=weights)[0]
            result.append(next_word)
        else:
            # If context not found, try with shorter context or pick random word
            found = False
            for i in range(1, len(context)):
                shorter_context = context[i:]
                if shorter_context in model:
                    next_words = model[shorter_context]
                    words = list(next_words.keys())
                    weights = list(next_words.values())
                    next_word = random.choices(words, weights=weights)[0]
                    result.append(next_word)
                    found = True
                    break
            
            if not found:
                # Pick a random word from all possible words in the model
                all_words = []
                for counter in model.values():
                    all_words.extend(counter.keys())
                if all_words:
                    next_word = random.choice(all_words)
                    result.append(next_word)
                else:
                    break

    return ' '.join(result)

def main():
    with open('dataset/ngram.txt', 'r') as file:
        text_data = file.read()

    processed_text = preprocess_text(text_data)
    model = build_ngram_model(processed_text, n=3)
    seeds = ['natural', 'language', 'data']  # Starting word or phrase
    length = 100  # Length of the generated text

    # Generate and print text
    for seed in seeds:
        print(f"Seed: '{seed}'")
        print(f"Length: {length} words")
        generated = generate_text(model, seed, length)
        print(generated)
        print("-" * 30)

if __name__ == "__main__":
    main()