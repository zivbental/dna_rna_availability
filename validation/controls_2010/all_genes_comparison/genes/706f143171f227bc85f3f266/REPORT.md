# YIR036C
Status: ok. Length: 837 nt. Measured usable bases: 556. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 556 | 0.3285 | 0.2781 |
| rnafold | ok | 556 | 0.2702 | 0.2313 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 290 | 0.3155 | 0.0085 |
| seed_p | 290 | -0.0728 | 0.0169 |
| seed_p_vs_seed_pars | 223 | -0.0616 | -0.0001 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
