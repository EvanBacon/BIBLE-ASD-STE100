# BIBLE-ASD-STE100

The full Bible (66 books, 31,102 verses) in [ASD-STE100](https://www.asd-ste100.org/) Simplified Technical English: short sentences, active voice, simple tenses, and plain words.

## Files

| Path | Contents |
|---|---|
| `BIBLE-ASD-STE100.md` | The complete text in one file, with scope and conformance notes |
| `books/` | One file per book, `01-genesis.md` to `66-revelation.md` |
| `tools/ste_lint.py` | Pattern checks for the STE grammar rules |

## Source

Each verse is a new rendering of the meaning of the King James Version (public domain). Chapter and verse numbers follow the KJV.

## Rules applied

- Sentences: 25 words max (descriptive), 20 words max (instructions)
- Verbs: simple present, past and future only; active voice; no `-ing` forms
- Modal verbs: `can`, `could`, `must`, `will` only
- Technical names: proper names and religious terms with no STE equivalent (covenant, altar, Sabbath)

## Check

```sh
python3 tools/ste_lint.py books/*.md
```

The two verses it flags (Exodus 3:14 "I AM", Numbers 15:3 "burnt offerings") are names, not passive verbs.

## Limits

Vocabulary is not checked against the official ASD-STE100 dictionary, so some words may not be approved STE words. This project is not certified by, affiliated with, or endorsed by ASD.
