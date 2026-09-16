# YKL207W
Status: ok. Length: 837 nt. Measured usable bases: 692. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 692 | 0.2857 | 0.2742 |
| rnafold | ok | 692 | 0.2101 | 0.2023 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 620 | 0.0349 | -0.2677 |
| seed_p | 620 | -0.0620 | -0.1446 |
| seed_p_vs_seed_pars | 568 | -0.1840 | -0.1507 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
