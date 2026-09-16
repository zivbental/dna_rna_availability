# YKL016C
Status: ok. Length: 663 nt. Measured usable bases: 516. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 516 | 0.2969 | 0.2735 |
| rnafold | ok | 516 | 0.2214 | 0.1793 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 432 | 0.0685 | 0.0228 |
| seed_p | 432 | -0.2775 | -0.2754 |
| seed_p_vs_seed_pars | 349 | -0.3959 | -0.4064 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
