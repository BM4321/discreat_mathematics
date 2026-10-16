# Discrete Mathematics: Obsidian Notes

An [Obsidian](https://obsidian.md) vault of discrete mathematics notes. Every topic note has:

- **Core concepts**, with definitions, tables and theorems
- **Worked examples** in Obsidian callouts
- A **mind map** (Mermaid `mindmap`)
- **Workflow** diagrams (Mermaid flowcharts and state diagrams)
- **Real-life examples**
- **Python** programs that apply the topic
- **Test cases** (plain `assert`-based `test_*` functions)
- **Practice problems**, with answers you can fold away
- A **summary**

## Contents

Start with [`Discrete Mathematics/00 - Discrete Mathematics MOC.md`](Discrete%20Mathematics/00%20-%20Discrete%20Mathematics%20MOC.md).

| # | Topic |
|---|-------|
| 01 | Propositional Logic |
| 02 | Predicate Logic and Quantifiers |
| 03 | Proof Techniques |
| 04 | Sets |
| 05 | Relations |
| 06 | Functions |
| 07 | Mathematical Induction and Recursion |
| 08 | Counting and Combinatorics |
| 09 | Discrete Probability |
| 10 | Number Theory and Cryptography |
| 11 | Recurrence Relations |
| 12 | Graph Theory |
| 13 | Trees |
| 14 | Boolean Algebra |
| 15 | Finite Automata and Regular Languages |

## Using it in Obsidian

1. Clone this repository.
2. In Obsidian, choose **Open folder as vault** and select the repository folder.
3. Mermaid diagrams render in Reading view and Live Preview. Wikilinks such as `[[04 - Sets]]` connect the notes, and the Graph view shows how they link.

## Running the Python in the notes

The script extracts every `python` code block from each note, runs them, and then runs each note's `test_*` functions:

```bash
python scripts/verify_notes.py
```

It needs Python 3.9 or later and only the standard library.
