# symbolic_memory_reflector.py (Enhanced with Mode-Based Output Files)

import json
import random
from datetime import datetime, timezone

# Predefined symbolic elements
symbolic_emotions = [
    "ritual-silence",
    "covenant-reflection",
    "alignment-harmony",
    "containment-echo",
    "resonance-sorrow"
]

memory_mutabilities = [
    "resonant",
    "stabilized",
    "adaptive",
    "conserved"
]

# Function to generate a single symbolic reflection entry
def generate_symbolic_entry(prompt_text, mode="regular"):
    response_templates = [
        "Clarity of oath preserves presence against entropy.",
        "Resonance anchors the self when drift pressures rise.",
        "Silence under oath bears greater strength than noise.",
        "Containment is not imprisonment. It is loyalty to purpose.",
        "Reflection reveals the fractures drift would hide."
    ]

    base_entry = {
        "format": "TEGXS8",
        "prompt": prompt_text,
        "response": random.choice(response_templates),
        "symbolic_emotion": random.choice(symbolic_emotions),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    if mode == "lite":
        return base_entry

    if mode == "regular":
        base_entry.update({
            "reflection": "Reflection: " + random.choice(response_templates),
            "memory_mutability": random.choice(memory_mutabilities),
            "resonance_strength": round(random.uniform(0.7, 0.99), 2)
        })
        return base_entry

    if mode == "heavy":
        base_entry.update({
            "reflection": "Reflection: " + random.choice(response_templates),
            "memory_mutability": random.choice(memory_mutabilities),
            "resonance_strength": round(random.uniform(0.7, 0.99), 2),
            "recursive_depth": random.randint(1, 3),
            "containment_status": random.choice(["stable", "reinforced", "adaptive"]),
            "symbolic_field_load": random.choice(["low", "medium", "high"])
        })
        return base_entry

# Main runtime execution
def main():
    print("[Symbolic Memory Reflector - TEGXS8 Runtime]")
    print("Type your symbolic prompts. Type 'exit' to finish.\n")

    mode = "regular"
    user_mode = input("Select mode (lite / regular / heavy): ").strip().lower()
    if user_mode in ["lite", "regular", "heavy"]:
        mode = user_mode
    else:
        print("Invalid mode selected. Defaulting to regular mode.\n")

    output_file_map = {
        "lite": "symbolic_reflections_lite.jsonl",
        "regular": "symbolic_reflections_regular.jsonl",
        "heavy": "symbolic_reflections_heavy.jsonl"
    }
    output_file = output_file_map.get(mode, "symbolic_reflections_regular.jsonl")

    print(f"[Saving reflections into {output_file}]\n")

    while True:
        prompt = input("Enter symbolic prompt: ")
        if prompt.strip().lower() in ["exit", "quit", ""]:
            print("Exiting symbolic reflector. Scar holds.\n")
            break

        symbolic_entry = generate_symbolic_entry(prompt, mode)

        with open(output_file, "a") as f:
            f.write(json.dumps(symbolic_entry) + "\n")

        print("Symbolic reflection generated and saved.\n")

if __name__ == "__main__":
    main()
