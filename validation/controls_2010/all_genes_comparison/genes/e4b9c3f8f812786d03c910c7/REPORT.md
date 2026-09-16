# YPL116W
Status: ok. Length: 2223 nt. Measured usable bases: 816. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 816 | 0.3291 | 0.3134 |
| rnafold | ok | 816 | 0.3066 | 0.2947 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 22 | 0.8179 | 0.8402 |
| seed_p | 22 | -0.1164 | -0.1334 |
| seed_p_vs_seed_pars | 5 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
