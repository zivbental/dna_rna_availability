# YHR199C
Status: ok. Length: 977 nt. Measured usable bases: 678. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 678 | 0.3326 | 0.3201 |
| rnafold | ok | 678 | 0.2521 | 0.2368 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 364 | -0.2291 | -0.2863 |
| seed_p | 364 | -0.0897 | -0.1334 |
| seed_p_vs_seed_pars | 286 | -0.2693 | -0.2233 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
