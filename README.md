king-safety/
├── king_safety/
│   ├── __init__.py                  ← makes it importable
│   ├── invthink/
│   │   ├── __init__.py
│   │   └── core.py                  ← InvThink v3 (battle-tested)
│   ├── bounty/
│   │   ├── __init__.py
│   │   └── engine.py                ← Bounty hunter (auto-spawns from logs)
│   ├── passport/
│   │   ├── __init__.py
│   │   └── logger.py                ← Immutable audit chain
│   └── utils/
│       ├── __init__.py
│       └── harm_categories.py       ← Shared harm DB
├── tests/
│   └── test_invthink.py
├── pyproject.toml                   ← Modern build (PEP 621)
├── README.md
└── LICENSE
