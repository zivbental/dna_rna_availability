# YEL036C
Status: ok. Length: 1682 nt. Measured usable bases: 1061. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1061 | 0.2950 | 0.2937 |
| rnafold | ok | 1061 | 0.2725 | 0.2789 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 522 | -0.0682 | -0.0278 |
| seed_p | 522 | -0.3070 | -0.2307 |
| seed_p_vs_seed_pars | 412 | -0.2459 | -0.2394 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
