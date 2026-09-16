# YIR012W
Status: ok. Length: 2480 nt. Measured usable bases: 1143. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1143 | 0.3362 | 0.3285 |
| rnafold | ok | 1143 | 0.3099 | 0.3008 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 788 | 0.0631 | -0.0985 |
| seed_p | 788 | -0.3016 | -0.1769 |
| seed_p_vs_seed_pars | 640 | -0.3560 | -0.2343 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
