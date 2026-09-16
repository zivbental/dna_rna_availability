# 20-nt target / 8-nt seed demonstration

| Transcript | 20-nt target | Full-site P | Best 8-nt seed P | Seed coordinates | Full-site opening kcal/mol | Seed opening kcal/mol |
| --- | --- | --- | --- | --- | --- | --- |
| CCW12 | 85–104 | 6.19043e-06 | 0.0219824 | 87–94 | 7.391 | 2.353 |
| CCW12 | 56–75 | 0.00138981 | 0.0943533 | 56–63 | 4.055 | 1.455 |
| RPL41A | 101–120 | 4.81902e-06 | 0.0178501 | 113–120 | 7.546 | 2.481 |
| RPL41A | 83–102 | 1.05482e-06 | 0.00284219 | 83–90 | 8.482 | 3.614 |

These are unconditioned full-transcript predictions for oligo-style recognition. Best-seed P refers to one selected 8-nt segment, rather than the union of all possible seeds. PARS measurements do not directly validate joint opening or oligo binding.

[CCW12 report](CCW12/seed_20nt/REPORT.md) · [RPL41A report](RPL41A/seed_20nt/REPORT.md)

Reproduce from the repository root:

```bash
.venv/bin/python validation/controls_2010/run_seed_demo.py
```
