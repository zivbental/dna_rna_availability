# YPL252C
Status: ok. Length: 625 nt. Measured usable bases: 409. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 409 | 0.3955 | 0.3642 |
| rnafold | ok | 409 | 0.3301 | 0.3035 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 239 | -0.3780 | -0.4948 |
| seed_p | 239 | -0.2709 | -0.2803 |
| seed_p_vs_seed_pars | 184 | -0.2067 | -0.3599 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
