# YOR201C
Status: ok. Length: 1324 nt. Measured usable bases: 717. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 717 | 0.4403 | 0.4260 |
| rnafold | ok | 717 | 0.3389 | 0.3436 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 150 | -0.4051 | -0.5857 |
| seed_p | 150 | -0.5971 | -0.6128 |
| seed_p_vs_seed_pars | 117 | -0.7871 | -0.8495 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
