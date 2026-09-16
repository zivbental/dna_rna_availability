# YIL108W
Status: ok. Length: 2313 nt. Measured usable bases: 1044. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1044 | 0.3773 | 0.3643 |
| rnafold | ok | 1044 | 0.3694 | 0.3460 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 132 | 0.1231 | 0.4197 |
| seed_p | 132 | 0.1047 | 0.1386 |
| seed_p_vs_seed_pars | 74 | 0.2749 | 0.3103 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
